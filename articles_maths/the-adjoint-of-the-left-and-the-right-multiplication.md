# __The Adjoint of the Left and the Right Multiplication__

## Introduction

The adjoint of the left multiplication of a Hilbert algebra is the left multiplication by the involution, $L_x^{*} = L_{x^{\dagger}}$, and the adjoint of the right multiplication is the right multiplication by the involution, $R_x^{*} = R_{x^{\dagger}}$. Both identities are the adjoint axiom in operator form, and together they say that the two regular representations are $\ast$-representations up to the passage from left to right. The content of the article is the explicit form of these adjoints and the way the modular conjugation ties them together.

The modular conjugation enters because the two representations are exchanged by it. On the standard form the **modular conjugation** $J$ is an antiunitary involution with $J\mathcal{M}J = \mathcal{M}'$, and through it the adjoint operation on the left multiplications becomes the right multiplication by the involution, $\jmath L_x \jmath = R_{x^{\dagger}}$: the exchange of left and right and the reversal of the involution are the same operation. This is the operator-theoretic reading of the adjoint axiom and the reason the modular conjugation is described as the map that turns the algebra into its commutant: adjunction and commutation are two names for the same reversal.

This article fixes the adjoints of the one-sided multiplications, their explicit form, and the modular conjugation as the operator implementing the exchange.

The adjoint axiom and the involution are *Hermitian Adjoints on a Hilbert Algebra* and *Hilbert Algebras*; the completion is *The Completion of a Hilbert Algebra*; the two representations are *The Left and the Right Regular Representation*; the modular conjugation is *The Modular Operator and Tomita-Takesaki Theory*; the standard form is *Von Neumann Algebras and the Hilbert Algebra Completeness*. Those are cited. The algebra is $A$, the completion $H$, the modular conjugation $\jmath$.

## The Adjoint of the Left Multiplication

**Theorem.** For every $x\in A$ the extended left multiplication satisfies

$$
\bar L_x^{*} = \bar L_{x^{\dagger}} \qquad \text{on } H .
$$

So the adjoint of the left multiplication by $x$ is the left multiplication by the involution of $x$, and the map $x\mapsto\bar L_x$ is a $\ast$-representation with the involution on the algebra and the Hilbert adjoint on the operators.

**Proof.** On $A$ the identity is the adjoint axiom, $\langle L_xy,z\rangle = \langle y,L_{x^{\dagger}}z\rangle$; both sides are bounded and agree on the dense set $A$, hence extend to the same operator on $H$.

**Proposition (the action on the cyclic vector).** With $\xi = \iota(1)$ the adjoint is determined at $\xi$: $\bar L_x^{*}\xi = \iota(x^{\dagger})$, whereas $\bar L_x\xi = \iota(x)$. So the adjoint moves the cyclic vector to the involution, which is the reason the involution is not a bounded map of $H$ in general.

**Proof.** $\bar L_{x^{\dagger}}\xi = \iota(x^{\dagger})$ and $\bar L_x\xi = \iota(x)$; the difference between the two orbits is the closure of the involution.

**Proposition (positivity of the adjoint pairing).** For every $x$ one has $\langle\bar L_x\bar L_x^{*}u,u\rangle = \|\bar L_x^{*}u\|^{2}\geq0$; so the operators $\bar L_x\bar L_x^{*}$ and $\bar L_x^{*}\bar L_x$ are positive, and the left multiplications form a $\ast$-closed family of operators whose positive parts are the ones of *Self-Adjoint Elements and the Positive Cone*.

**Proof.** The displayed identity is the definition of the Hilbert adjoint and the positivity of the norm.

## The Adjoint of the Right Multiplication

**Theorem.** For every $x\in A$ the extended right multiplication satisfies

$$
\bar R_x^{*} = \bar R_{x^{\dagger}} \qquad \text{on } H .
$$

**Proof.** The same computation read from the other side: $\langle R_xy,z\rangle = \langle yx,z\rangle = \langle y,zx^{\dagger}\rangle$ by the adjoint axiom applied with the roles of the two arguments exchanged, which is $\langle y,R_{x^{\dagger}}z\rangle$.

**Proposition (the adjoint is an antirepresentation).** The map $x\mapsto\bar R_x$ is an anti-$\ast$-representation: $\bar R_{xy} = \bar R_y\bar R_x$ and $\bar R_{x^{\dagger}} = \bar R_x^{*}$, so the adjoint operation reverses the order of the representation and of the product in the same way.

**Proof.** $R_{xy}z = zxy = R_yR_xz$ and the adjoint identity is the theorem.

**Remark (left and right adjoints are different operators).** The adjoint of the left multiplication is a left multiplication and the adjoint of the right multiplication is a right multiplication: adjunction respects the side. The exchange between the sides is not adjunction but conjugation by the modular operator, taken up next.

## The Modular Conjugation and the Exchange

**Theorem (the exchange).** Let $\jmath$ be the modular conjugation of the completion. Then

$$
\jmath\,\bar L_x\,\jmath = \bar R_{x^{\dagger}} , \qquad \jmath\,\bar R_x\,\jmath = \bar L_{x^{\dagger}} ,
$$

and consequently $\jmath\bar L_x^{*}\jmath = \bar R_x$: the modular conjugation turns the adjoint of a left multiplication into the right multiplication by the same element.

**Proof.** The modular conjugation satisfies $\jmath\mathcal{M}\jmath = \mathcal{M}^{c}$ and reverses products, by *The Modular Operator and Tomita-Takesaki Theory*; on the left multiplications this gives $\jmath\bar L_x\jmath = \bar R_{x^{\dagger}}$ as in *The Left and the Right Regular Representation*; applying the involution gives the second identity, and combining with the adjoint formula gives the third.

**Corollary (adjunction is the exchange of side).** For every $x$ the operator $\jmath\bar L_x^{*}\jmath$ is $\bar R_x$; so the Hilbert adjoint followed by the modular conjugation is the passage from the left representation to the right representation, and the two operations together generate the symmetry between an algebra and its commutant.

**Proof.** Substitute $\bar L_x^{*} = \bar L_{x^{\dagger}}$ into the theorem.

**Remark (three operations, one symmetry).** The involution reverses products; the Hilbert adjoint reverses the arrow; the modular conjugation exchanges the algebra with its commutant. On the left multiplications the three compose into the single symmetry between the left and the right regular representations, and this is why the modular conjugation is the natural home of the adjoint operation in a standard form.

## Worked Cases

### The Group Algebra

For $A = \mathbb{C}[G]$ the adjoint of the left multiplication by $g$ is the left multiplication by $g^{-1}$, and the modular conjugation exchanges the left and the right regular representations, $\jmath L_g\jmath = R_{g^{-1}}$.

### Matrices

For $A = M_n(\mathbb{C})$ with the Hilbert–Schmidt form, $\bar L_a^{*} = \bar L_{a^{*}}$ with $a^{*}$ the conjugate transpose, and the modular conjugation $J(u) = u^{*}$, the conjugate transpose, satisfies $JL_aJ = R_{a^{*}}$, which is the passage from the left-action copy of $M_n(\mathbb{C})$ to the right-action copy.

### The Tracial Case

When the form is tracial the modular conjugation is the operator $x\xi\mapsto x^{*}\xi$ extended, and the exchange theorem reads $JL_xJ = R_{x^{\dagger}}$ with $J$ simultaneously the modular conjugation and the involution: the two operations coincide and the symmetry is transparent.

## Summary

The adjoint of the **left multiplication** is the left multiplication by the involution, $\bar L_x^{*} = \bar L_{x^{\dagger}}$, and the adjoint of the **right multiplication** is the right multiplication by the involution, $\bar R_x^{*} = \bar R_{x^{\dagger}}$; both are the adjoint axiom in operator form, they show that the involution is simultaneously the adjoint operation and the product reversal $\bar R_{xy} = \bar R_y\bar R_x$, and they keep adjunction on the same side. The **modular conjugation** $\jmath$ implements the exchange between the sides, $\jmath\bar L_x\jmath = \bar R_{x^{\dagger}}$, whence $\jmath\bar L_x^{*}\jmath = \bar R_x$: adjunction followed by conjugation is the passage from the left to the right representation, and the involution, the adjoint and the conjugation are three descriptions of one symmetry between an algebra and its commutant. The involution and the adjoint axiom are *Hermitian Adjoints on a Hilbert Algebra*, the representations are *The Left and the Right Regular Representation*, and the conjugation is *The Modular Operator and Tomita-Takesaki Theory*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\bar L_x^{*} = \bar L_{x^{\dagger}}$ | Adjoint of the left multiplication |
| $\bar R_x^{*} = \bar R_{x^{\dagger}}$ | Adjoint of the right multiplication |
| $\bar L_x^{*}\xi = \iota(x^{\dagger})$ | The adjoint on the cyclic vector |
| $\bar L_x\bar L_x^{*}\geq0$ | Positivity of the adjoint products |
| $\jmath\bar L_x\jmath = \bar R_{x^{\dagger}}$ | The exchange by the modular conjugation |
| $\jmath\bar L_x^{*}\jmath = \bar R_x$ | Adjunction plus conjugation = passage to the right |
| $\jmath\mathcal{M}\jmath = \mathcal{M}^{c}$ | The commutant statement behind the exchange |

## Further Reading

- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the adjoints of the regular representations.
- Serban Stratila and László Zsidó, *Lectures on von Neumann Algebras* (Abacus Press, 1979), for the left and right representations and their adjoints.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 2 (Academic Press, 1986), for the modular conjugation and the standard form.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the exchange between the two regular representations.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, vol. 1 (Springer, 1987), for the standard form as a left–right symmetry.
