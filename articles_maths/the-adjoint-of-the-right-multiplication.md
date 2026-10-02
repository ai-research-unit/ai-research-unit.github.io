
# __The Adjoint of the Right Multiplication on a Clifford Algebra__

## Introduction

The right multiplication $R_a(x)=xa$ is the mirror of the left multiplication, and its adjoint for the standard form is again a right multiplication,

$$
R_a^{*} = R_{\hat a} , \qquad \hat a=\alpha(\tilde a) ,
$$

with the Clifford conjugate in the parameter. The interesting feature is the interaction with the sign: the right multiplications are **anti**-multiplicative, $R_aR_c=R_{ca}$, so the map $a\mapsto R_a$ is an anti-isomorphism, and the adjoint carries it to the anti-isomorphism by the conjugated parameters. Both one-sided families are therefore **closed under the adjoint**, each in itself, and the commutant of the left family — which is the right family in the central-simple case — is a $*$-subalgebra for the adjoint. The article states this and the geometric consequences, with the mirror facts quoted from *The Adjoint of the Left Multiplication on a Clifford Algebra*.

**The boundaries.** The operator and its anti-multiplicativity are *The Left and Right Multiplication Operators on a Clifford Algebra*; the form and the conjugation are *The Twisted Adjoint on a Clifford Algebra*; the mirror article is *The Adjoint of the Left Multiplication on a Clifford Algebra*; the two-sided operators are *The Adjoint of the Sandwich* and *The Adjoint of the Two-Sided Multiplication Operator*; the commutant pair is *The Left and Right Multiplication Operators on a Clifford Algebra*. The base is a field $F$ of characteristic not $2$ with a non-degenerate $q$, $q(u)=B(u,u)$, $uv+vu=2B(u,v)$.

## The Adjoint

**Theorem.** For every $a$, $R_a^*=R_{\hat a}$; the map $a\mapsto R_a$ is an anti-isomorphism of the algebra onto the right-multiplication family, $R_aR_c=R_{ca}$, and the adjoint $R_a\mapsto R_{\hat a}$ is an anti-isomorphism of the family, so the family is closed under the adjoint.

**Proof.** $\langle xa,y\rangle=\operatorname{Sc}(\widehat{xa}y)=\operatorname{Sc}(\hat a\hat xy)=\operatorname{Sc}(\hat xy\hat a)=\langle x,y\hat a\rangle$, using the anti-automorphism property and the cyclic invariance of the scalar part, so $R_a^*=R_{\hat a}$; the anti-multiplicativity is $R_aR_c(x)=xca=R_{ca}(x)$; the closure is the conjunction of the two, since $\hat a$ ranges over the algebra as $a$ does.

**Proposition (self-adjointness and orthogonality).** $R_a$ is self-adjoint exactly when $\hat a=a$, and orthogonal exactly when $a\hat a=1$; the two conditions are the mirror of the conditions for the left multiplication, with the order of the factors reversed.

**Proof.** $R_a^*=R_a$ is equivalent to $\hat a=a$ by the faithfulness of the right family; $R_a^*R_a=R_{\hat a}R_a=R_{a\hat a}$, which is the identity exactly when $a\hat a=1$. The reversal of the order relative to the left case is the anti-multiplicativity.

**Remark (the commutant).** The commutant of the left family is $\{R_b\}$ in the central-simple case, and the adjoint computation shows it is a $*$-subalgebra: the adjoint of an element of the commutant is again a right multiplication, hence again in the commutant. More generally, the adjoint of an element of the commutant of a $*$-invariant family is in the same commutant, because the adjoint operation reverses the order and preserves the family; this is the algebraic reason the commutant pair survives the transition to the adjoint.

## Worked Cases

### The Quaternions

For $\mathrm{Cl}\cong\mathbb H$ the right multiplication by a pure quaternion unit is skew-adjoint, $R_{e_1}^*=-R_{e_1}$, exactly as for the left multiplication; the right family is the opposite action of the quaternions, and the adjoint carries it to itself.

### The Scalar Case

For $a=\lambda$ central the right multiplication is $\lambda\operatorname{id}$, self-adjoint, and orthogonal only for $\lambda^2=1$; the centre of the algebra acts by scalars on both sides, and the adjoint fixes them.

### A Unit with $\hat a=a^{-1}$

For a unit with $\hat a=a^{-1}$ the right multiplication is orthogonal, $R_a^*R_a=R_{a\hat a}=\operatorname{id}$, and the left multiplication by the same element is orthogonal too; the two conditions coincide even though the two families are opposite, because the conjugation is an involution.

## Summary

The adjoint of the **right multiplication** is $R_a^*=R_{\hat a}$ for the standard form, with the Clifford conjugate in the parameter; the right family is anti-multiplicative, so the adjoint carries it to itself and the family is **closed under the adjoint**. The conditions mirror those of the left multiplication with the order of the factors reversed: $R_a$ is **self-adjoint** exactly when $\hat a=a$ and **orthogonal** exactly when $a\hat a=1$. The commutant of the left family — the right family in the central-simple case — is a $*$-subalgebra for the adjoint; this is the algebraic reason the commutant pair is stable under the adjoint operation. The operator is *The Left and Right Multiplication Operators on a Clifford Algebra*, the form and the conjugation are *The Twisted Adjoint on a Clifford Algebra*, and the mirror article is *The Adjoint of the Left Multiplication on a Clifford Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R_a(x)=xa$ | Right multiplication |
| $R_aR_c=R_{ca}$ | Anti-multiplicativity |
| $R_a^*=R_{\hat a}$ | Adjoint for the standard form |
| $\hat a=\alpha(\tilde a)$ | Clifford conjugation |
| $\hat a=a$ | Self-adjointness condition |
| $a\hat a=1$ | Orthogonality condition |
| $\{L_a\}'=\{R_b\}$ | Commutant pair in the central-simple case; a $*$-subalgebra |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the
  right multiplications and the conjugation in the low-dimensional algebras.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced
  Mathematics 50 (Cambridge University Press, 1995), for the anti-isomorphisms of the two one-sided
  families and the commutant.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the
  double centraliser theorem and the $*$-structure of the commutant.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for
  the two one-sided actions and their adjoints.
