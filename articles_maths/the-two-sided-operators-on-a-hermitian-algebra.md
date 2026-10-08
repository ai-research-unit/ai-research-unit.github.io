# __The Two-Sided Operators on a Hermitian Algebra__

## Introduction

A **two-sided operator** of a Hermitian algebra is a sandwich $\Theta_x(y) = xyx^{\dagger}$, and the family of two-sided operators is closed under composition, adjunction and the passage to invertible parameters. The **modular conjugation** of the standard form, the invariance $\jmath\Theta_x\jmath = \Theta_x$, the standard form itself and its self-dual cone are operator theory on the completion and are in *The Modular Structure of a Hermitian Algebra*.

The sandwiches are the operators attached to an element and its involution: they are closed under composition, $\Theta_x\Theta_z = \Theta_{xz}$, and under adjunction, $\Theta_x^{*} = \Theta_{x^{\dagger}}$, and their invertible members are the inner automorphisms of the algebra. What makes them the operators of the **standard form** is their invariance under the modular conjugation, which exchanges the two factors without changing the operator; that statement, the standard form and the self-dual cone belong to the operator theory of the completion and are in *The Modular Structure of a Hermitian Algebra*.

This article fixes the two-sided operators, their closure under composition and adjunction, and their invertible and unitary members.

The sandwich and its adjoint are *The Adjoint of the Sandwich on a Hermitian Algebra*; the left and right multiplications are *The Adjoint of the Left and the Right Multiplication*; the modular conjugation, the standard form and the self-dual cone are *The Modular Structure of a Hermitian Algebra*. Those are cited. The algebra is $A$ with form $\langle\cdot,\cdot\rangle$.

## The Two-Sided Operators

**Definition.** The **two-sided operators** of $A$ are the sandwiches $\Theta_x(y) = xyx^{\dagger}$ for $x\in A$; they form the semigroup $\Theta = \{\Theta_x : x\in A\}$ closed under composition.

**Proposition (the structure of the family).** $\Theta$ is closed under composition, $\Theta_x\Theta_z = \Theta_{xz}$; closed under adjunction, $\Theta_x^{*} = \Theta_{x^{\dagger}}$; and the invertible two-sided operators are the inner automorphisms of the algebra implemented by invertible elements, with the unitary ones exactly the form-preserving inner automorphisms.

**Proof.** The composition law is associativity; the adjoint law is *The Adjoint of the Sandwich on a Hermitian Algebra*; the automorphism statement is the defining property of an inner automorphism and the unitarity condition is the isometry theorem.

The **modular conjugation**, the **standard form** $(\mathcal{M},H,\jmath,P)$ and the self-dual cone are operator theory on the completion and are in *The Modular Structure of a Hermitian Algebra* (Part II).

## Worked Cases

### The Group Algebra

For $A = \mathbb{C}[G]$ the two-sided operators are $\Theta_g(y) = gyg^{-1}$, the modular conjugation exchanges the left and the right regular representations, and the cone is the closure of the image of the positive cone of the group algebra under the cyclic vector; the form is tracial and the conjugation is the involution.

### Matrices

For $A = M_n(\mathbb{C})$ with the Hilbert–Schmidt form, $\Theta_a(b) = aba^{*}$ and $\jmath(u) = u^{*}$ satisfies $\jmath\Theta_a\jmath = \Theta_a$; the cone $P$ is the cone of positive matrices applied to the unit, and its self-duality is the statement that the positive matrices are exactly those pairing nonnegatively with the positive matrices.

### The Trivial Algebra

For $A = \mathbb{C}$ the only two-sided operator is the identity, the modular conjugation is $z\mapsto\bar z$ and the cone is the ray of the positive reals; the four data of the standard form are the algebra, its commutant, the conjugation and the cone, and all are one-dimensional.

## Summary

The **two-sided operators** $\Theta_x(y) = xyx^{\dagger}$ are closed under composition and adjunction, and their invertible members are the inner automorphisms, with the unitary members exactly the form-preserving ones. Their invariance under the **modular conjugation**, $\jmath\Theta_x\jmath = \Theta_x$, and the **standard form** $(\mathcal{M},H,\jmath,P)$ with its self-dual cone are operator theory on the completion and are in *The Modular Structure of a Hermitian Algebra*. The sandwich and its adjoint are *The Adjoint of the Sandwich on a Hermitian Algebra* and the multiplications are *The Adjoint of the Left and the Right Multiplication*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Theta_x$, $\Theta_x\Theta_z = \Theta_{xz}$ | Two-sided operators and their composition |
| $\jmath\bar L_x\jmath = \bar R_{x^{\dagger}}$ | The conjugation exchanges the factors |
| $\Theta_xP\subseteq P$ | Two-sided operators preserve the cone |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 2 (Academic Press, 1986), for the standard form and the self-dual cone.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the cone and the modular conjugation.
- Serban Stratila and László Zsidó, *Lectures on von Neumann Algebras* (Abacus Press, 1979), for the self-dual cone and the standard form.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, vol. 1 (Springer, 1987), for the two-sided operators and the modular structure.
- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the standard form and the two-sided operators.
