# __Adjoints of the Intertwiners of a Hermitian Algebra__

## Introduction

An intertwiner of a Hermitian algebra is an operator between two completions that commutes with the left multiplications, $T\bar L_x = \bar L'_xT$; and the adjoint of an intertwiner is again an intertwiner. That single statement makes the intertwiners a class closed under adjunction: the adjoint operation on intertwiners is the same operation as the involution on the algebra. The commutant, the modular transpose and the polar decomposition of intertwiners need the standard form and are operator theory, in *The Modular Structure of a Hermitian Algebra*.

The article fixes one consequence: the adjoint of an intertwiner of the left representations is an intertwiner of the left representations, so the class is closed under adjunction and the self-adjoint intertwiners form its real part. The further consequences — the commutant as the algebra of intertwiners, the **modular transpose** $T\mapsto T^{\flat} = \jmath T^{*}\jmath$, and the polar decomposition within the class — are operator theory on the completion and are in *The Modular Structure of a Hermitian Algebra*.

This article fixes the adjoint of an intertwiner and the closure of the class under adjunction.

The Hermitian algebra, its involution and its completion are *Hermitian Algebras*, *Hermitian Adjoints on a Hermitian Algebra* and *The Completion of a Hilbert Algebra*; the representations and the adjoints of the multiplications are *The Left and the Right Regular Representation* and *The Adjoint of the Left and the Right Multiplication*; the commutant, the modular transpose and the polar decomposition are *The Modular Structure of a Hermitian Algebra*. Those are cited. The algebras are $A$ and $A'$ with completions $H$ and $H'$, and the representations are $x\mapsto\bar L_x$ and $x\mapsto\bar L'_x$.

## Intertwiners and Their Adjoints

**Definition.** A bounded operator $T : H\to H'$ is an **intertwiner** of the left representations when

$$
T\,\bar L_x = \bar L'_x\,T \qquad \text{for every } x\in A .
$$

**Theorem (the adjoint of an intertwiner is an intertwiner).** If $T$ is an intertwiner then $T^{*} : H'\to H$ is an intertwiner of the left representations in the reverse direction,

$$
T^{*}\,\bar L'_x = \bar L_x\,T^{*} \qquad \text{for every } x\in A .
$$

**Proof.** Taking adjoints in $T\bar L_x = \bar L'_xT$ gives $\bar L_x^{*}T^{*} = T^{*}\bar L'_x{}^{*}$, which by $\bar L_y^{*} = \bar L_{y^{\dagger}}$ is $\bar L_{x^{\dagger}}T^{*} = T^{*}\bar L'_{x^{\dagger}}$; since the involution is of order two and runs over the algebra, the identity holds with $x$ in place of $x^{\dagger}$.

**Corollary (the class is self-adjoint).** The intertwiners of the left representations form a vector space closed under adjunction; the self-adjoint intertwiners $T = T^{*}$ form its real part, and every intertwiner is $T_1+iT_2$ with $T_1, T_2$ self-adjoint intertwiners.

**Proof.** The first statement is the theorem; the decomposition is $T_1 = \tfrac12(T+T^{*})$, $T_2 = \frac{1}{2i}(T-T^{*})$, which are intertwiners by the theorem and self-adjoint by construction.

**Proposition (the modular conjugation exchanges the two commutation properties).** For the standard representation, an operator $T$ commutes with all the left multiplications exactly when $\jmath T\jmath$ commutes with all the right multiplications; equivalently

$$
\{\bar R_x\}' = \jmath\,\{\bar L_x\}'\jmath .
$$

**Proof.** $\jmath\bar L_x\jmath = \bar R_{x^{\dagger}}$ and $\jmath\bar R_x\jmath = \bar L_{x^{\dagger}}$ by *The Adjoint of the Left and the Right Multiplication*. Conjugating $T\bar L_x = \bar L_xT$ by $\jmath$ gives $\jmath T\jmath\,\bar R_{x^{\dagger}} = \bar R_{x^{\dagger}}\jmath T\jmath$, so $\jmath T\jmath$ commutes with every right multiplication; the converse is the same computation applied to $\jmath S\jmath$.

**Remark (the two commutation properties are not the same).** The commutation with the left multiplications and the commutation with the right multiplications are different conditions, related by the conjugation with $\jmath$ and not equal: the smallest case is a right multiplication $\bar R_y$, which commutes with every right multiplication and commutes with the left ones only when $y$ is central. So the two conditions are exchanged by the modular conjugation, and each of the two commutants is recovered from the other by conjugating back.

The **commutant**, the **modular transpose** $T\mapsto T^{\flat}=\jmath T^{*}\jmath$ and the polar decomposition of intertwiners are operator theory on the completion and are in *The Modular Structure of a Hermitian Algebra* (Part II).

## Worked Cases

### Matrices

For $A = M_n(\mathbb{C})$ with the Hilbert–Schmidt form, the commutant of the left action is the right action, the modular conjugation is $J(u) = u^{*}$, and an intertwiner is a map $T$ with $T(a u) = a T(u)$ for all $a$; the adjoint is again such a map and the modular transpose is $T^{\flat}(u) = T^{*}(u^{*})^{*}$, the entrywise conjugate transpose operation.

### The Group Algebra

For $A = \mathbb{C}[G]$ with the standard form, the commutant of the left regular representation is the right regular representation, and the modular conjugation is the bounded antiunitary $J(g\xi) = g^{-1}\xi$; the adjoint on the commutant is $\bar R_g^{*} = \bar R_{g^{-1}}$, while the modular transpose is $\bar R_g^{\flat} = \bar L_g$, the left multiplication, so the two operations coincide on the commutant exactly for the central involutions.

### The Non-Tracial Case

When the modular operator is not the identity the adjoint of an intertwiner and its modular transpose are different operations, related by the modular operator: $T^{\flat} = \jmath T^{*}\jmath$, while $T^{*}$ is the Hermitian adjoint on $H$ and $T^{*} = \Delta^{1/2}\,S\,T^{\flat}S\,\Delta^{-1/2}$ with $S = \jmath\Delta^{1/2}$; both are intertwiners, and they agree exactly when the form is tracial.

## Summary

An **intertwiner** of the left representations satisfies $T\bar L_x = \bar L'_xT$, and its **adjoint** is again an intertwiner, $T^{*}\bar L'_x = \bar L_xT^{*}$, because the involution of the algebra is the adjoint of the multiplications; so the intertwiners form a $\ast$-closed class with a real form of self-adjoint intertwiners. The self-adjoint intertwiners form the real form of the class. The **commutant**, the **polar decomposition** of a closed intertwiner and the **modular transpose** $T\mapsto T^{\flat} = \jmath T^{*}\jmath$ are operator theory on the completion and are in *The Modular Structure of a Hermitian Algebra*. The representations and the adjoint identities are *The Left and the Right Regular Representation* and *The Adjoint of the Left and the Right Multiplication*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T\bar L_x = \bar L'_xT$ | Intertwiner of the left representations |
| $T^{*}\bar L'_x = \bar L_xT^{*}$ | The adjoint is an intertwiner |
| $\pi(A)'$ | Commutant, the intertwiners of $\pi$ with itself |
| $T = T^{*}$ | Self-adjoint intertwiner, real form |

## Further Reading

- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for intertwiners, commutants and the standard form.
- Serban Stratila and László Zsidó, *Lectures on von Neumann Algebras* (Abacus Press, 1979), for the commutant of a Hermitian algebra and its involution.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the polar decomposition of a closed operator and its invariance.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the modular conjugation and the self-duality of the standard form.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, vol. 1 (Springer, 1987), for intertwiners of the regular representation.
