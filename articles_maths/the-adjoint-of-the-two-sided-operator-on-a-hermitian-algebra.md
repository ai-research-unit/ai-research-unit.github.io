# __The Adjoint of the Two-Sided Operator on a Hermitian Algebra__

## Introduction

The **two-sided operator** of a Hermitian algebra is $\mathrm{Sd}_x(y) = xyx^{\dagger}$, the composition of a left and a right multiplication, $\mathrm{Sd}_x = L_xR_{x^{\dagger}}$. Its adjoint for the form is again a two-sided operator, $\mathrm{Sd}_x^{*} = \mathrm{Sd}_{x^{\dagger}}$, so the two-sided operator is the natural two-sided operator of the theory and the family of two-sided operators is closed under adjunction. The two-sided operator is normal, it preserves the positive cone in the appropriate sense, and its adjoint relation with its parameter is the sharpest form of the adjoint axiom for two-sided operators.

A two-sided operator has two unitarity properties, and they must not be confused. It is **self-adjoint** for the form exactly when $\mathrm{Sd}_{x^{\dagger}} = \mathrm{Sd}_x$, which holds in particular when the parameter is self-adjoint, $x = x^{\dagger}$; it is an **isometry** exactly when $\mathrm{Sd}_x^{*}\mathrm{Sd}_x = \mathrm{Sd}_{x^{\dagger}x}$ is the identity, which holds in particular when $x^{\dagger}x = 1$; and it is **unitary** exactly when $x^{\dagger}x = xx^{\dagger} = 1$, that is when $x$ is unitary in the algebra. So the unitarity of the two-sided operator is the unitarity of its parameter, and the unitary two-sided operators are the norm-preserving two-sided operators of the algebra.

The comparison of the form-adjoint $\mathrm{Sd}_{x^{\dagger}}$ with the Hermitian adjoint $\mathrm{Sd}_{x^{*}}$ of the two-sided operator, and the modular operator that measures their difference, are operator theory on the completion and are in *The Modular Structure of a Hermitian Algebra*.

This article fixes the two-sided operator, its adjoint and the unitarity condition.

The Hermitian algebra and its involution are *Hermitian Algebras* and *Hermitian Adjoints on a Hermitian Algebra*; the multiplications and their adjoints are *The Adjoint of the Left and the Right Multiplication*; the completion-level comparison of the two adjoints and the modular objects are *The Modular Structure of a Hermitian Algebra*. Those are cited. The algebra is $A$ with involution $\dagger$ and form $\langle\cdot,\cdot\rangle$.

## The Two-Sided Operator and Its Adjoint

**Definition.** For $x\in A$ the **two-sided operator**, $\mathrm{Sd}_x(y)=xyx^{\dagger}$, is

$$
\boxed{\;\mathrm{Sd}_x : A\to A, \qquad \mathrm{Sd}_x(y) = x\,y\,x^{\dagger}\;} .
$$

It is the composition $\mathrm{Sd}_x = L_xR_{x^{\dagger}} = R_{x^{\dagger}}L_x$ of a left and a right multiplication, and it is semilinear in the parameter up to the involution and linear in the argument.

**Theorem (the adjoint is the two-sided operator of the involution).** For every $x$,

$$
\boxed{\;\mathrm{Sd}_x^{*} = \mathrm{Sd}_{x^{\dagger}}\;} ,
$$

the adjoint being taken for the form.

**Proof.** By the adjoint axiom applied twice, $\langle \mathrm{Sd}_xy, z\rangle = \langle xyx^{\dagger}, z\rangle = \langle yx^{\dagger}, x^{\dagger}z\rangle = \langle y, x^{\dagger}z(x^{\dagger})^{\dagger}\rangle = \langle y,\mathrm{Sd}_{x^{\dagger}}z\rangle$.

**Proposition (positivity of the adjoint products).** $\mathrm{Sd}_x^{*}\mathrm{Sd}_x = \mathrm{Sd}_{x^{\dagger}x}$ and $\mathrm{Sd}_x\mathrm{Sd}_x^{*} = \mathrm{Sd}_{xx^{\dagger}}$; both are two-sided operators of positive elements and hence are positive operators for the form, $\langle\mathrm{Sd}_{x^{\dagger}x}u,u\rangle\geq0$.

**Proof.** The composition law $\mathrm{Sd}_x\mathrm{Sd}_z = \mathrm{Sd}_{xz}$ holds by associativity, whence the two products; positivity is $\langle\mathrm{Sd}_{x^{\dagger}x}u,u\rangle = \langle x^{\dagger}x\,u, u\rangle = \langle x u, x u\rangle$ by the adjoint axiom.

**Proposition (normal and form-preserving maps).** $\mathrm{Sd}_x$ preserves the adjoint relation in the sense $\mathrm{Sd}_x(y^{\dagger}) = \mathrm{Sd}_{x^{\dagger}}(y)^{\dagger}$, and it maps the positive cone into itself when $x$ is such that $x^{\dagger}x\leq 1$.

**Proof.** $x y^{\dagger}x^{\dagger} = (xyx^{\dagger})^{\dagger}$ is the involution statement; the cone statement is the composition of the positivity of the two adjoint products with the stability of the cone under inner conjugation.

## The Unitarity Condition

**Theorem (the two-sided operator is an isometry exactly for unitary parameters).** For every $x$ the following are equivalent:

1. $\mathrm{Sd}_x$ is isometric for the form, $\langle\mathrm{Sd}_xy,\mathrm{Sd}_xz\rangle = \langle y,z\rangle$;
2. $\mathrm{Sd}_x^{*}\mathrm{Sd}_x = \mathrm{id}$, that is $\mathrm{Sd}_{x^{\dagger}x} = \mathrm{id}$;
3. $x^{\dagger}x = 1$ (when the left representation is faithful).

Similarly $\mathrm{Sd}_x$ is **unitary** exactly when $x^{\dagger}x = xx^{\dagger} = 1$, that is when $x$ is unitary.

**Proof.** The identity $\langle\mathrm{Sd}_xy,\mathrm{Sd}_xz\rangle = \langle\mathrm{Sd}_x^{*}\mathrm{Sd}_xy,z\rangle = \langle\mathrm{Sd}_{x^{\dagger}x}y,z\rangle$ gives the equivalence of 1 and 2; the faithfulness of the left representation identifies $\mathrm{Sd}_{x^{\dagger}x} = \mathrm{id}$ with $x^{\dagger}x = 1$; unitarity adds the inverse on the other side.

**Corollary (the unitary two-sided operators form a group).** The parameters $x$ with $x^{\dagger}x = xx^{\dagger} = 1$ form a group, and $x\mapsto\mathrm{Sd}_x$ is a group homomorphism with $x\mapsto\mathrm{Sd}_{x^{\dagger}}$ for the inverse; the two-sided operators realised are the two-sided operators preserving the form and the norm.

**Proof.** Multiplicativity of $\mathrm{J}$ is associativity, the inverse statement is the adjoint identity, and the preservation of the form is the theorem.

**Remark (self-adjointness against unitarity).** A two-sided operator is self-adjoint for the form exactly when $\mathrm{Sd}_{x^{\dagger}} = \mathrm{Sd}_x$; since the map $x\mapsto\mathrm{Sd}_x$ is even in the parameter, $\mathrm{Sd}_{-x} = \mathrm{Sd}_x$, this holds in particular for every self-adjoint parameter and every anti-self-adjoint one, and the parameter is recovered from the operator only up to sign. A two-sided operator is an isometry exactly when $\mathrm{Sd}_{x^{\dagger}x} = \mathrm{id}$, which holds in particular for a unitary parameter. The two conditions are independent, and a unitary parameter need not be self-adjoint. The self-adjoint two-sided operator of a positive parameter is the **two-sided operator** of *The Hermitian Pair of Operators on a Hermitian Algebra with Hermitian Adjoint*, and its ordering properties are those of *Self-Adjoint Elements and the Positive Cone*.

The **modular operator** and the comparison of the form-adjoint with the Hermitian adjoint of the two-sided operator are operator theory on the completion and are in *The Modular Structure of a Hermitian Algebra* (Part II).

## Worked Cases

### The Group Algebra

For $A = \mathbb{C}[G]$ with the tracial standard form, $\mathrm{Sd}_g(y) = gyg^{-1}$ and $\mathrm{Sd}_g^{*} = \mathrm{Sd}_{g^{-1}}$, with $\mathrm{Sd}_g$ unitary for every $g$; the form-adjoint and the Hermitian adjoint coincide.

### Matrices

For $A = M_n(\mathbb{C})$ with the Hilbert–Schmidt form, $\mathrm{Sd}_a(y) = aya^{*}$ and $\mathrm{Sd}_a^{*} = \mathrm{Sd}_{a^{*}}$; the two-sided operator is unitary exactly when $a$ is unitary, and the discrepancy between the two adjoints vanishes because the form is tracial. At $n=2$ the two-sided operator with the Hermitian $\sigma_1$ is self-adjoint and it reverses $\sigma_3$:

$$
a=\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad a^{*}=a,\qquad \mathrm{Sd}_a(\sigma_3)=\sigma_1\sigma_3\sigma_1=-\sigma_3,\qquad \mathrm{Sd}_a^{*}=\mathrm{Sd}_{a^{*}}=\mathrm{Sd}_a .
$$

### The Density Matrix Picture

For the algebra of matrices with the form $\langle a,b\rangle = \mathrm{tr}(b^{*}a)$ the two-sided operator is $\mathrm{Sd}_a(b) = aba^{*}$, its adjoint is $\mathrm{Sd}_{a^{*}} = \mathrm{Sd}_{a^{\dagger}}$ because the form is tracial, and the modular conjugation $J(u) = u^{*}$ commutes with the two-sided operator; the two-sided operators are exactly the inner automorphisms.

## Summary

The **two-sided operator** $\mathrm{Sd}_x(y) = xyx^{\dagger}$ is the composition $\mathrm{Sd}_x = L_xR_{x^{\dagger}}$ of a left and a right multiplication, its **adjoint for the form** is $\mathrm{Sd}_x^{*} = \mathrm{Sd}_{x^{\dagger}}$, and the adjoint products $\mathrm{Sd}_{x^{\dagger}x}$ and $\mathrm{Sd}_{xx^{\dagger}}$ are two-sided operators of positive elements, hence positive. The **unitarity condition** is that $\mathrm{Sd}_x$ is an isometry exactly when $x^{\dagger}x = 1$ and unitary exactly when $x^{\dagger}x = xx^{\dagger} = 1$, so the unitary two-sided operators are the two-sided form-preserving operators and the map $x\mapsto\mathrm{Sd}_x$ is a homomorphism of the unitary group of the algebra. The invariance of the two-sided operator under the modular conjugation and the modular flow are operator theory on the completion and are in *The Modular Structure of a Hermitian Algebra*. The involution is *Hermitian Adjoints on a Hermitian Algebra*, the multiplications and their adjoints are *The Adjoint of the Left and the Right Multiplication*, and the Hermitian case is *The Hermitian Pair of Operators on a Hermitian Algebra with Hermitian Adjoint*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Sd}_x(y) = xyx^{\dagger}$ | The Hermitian pair |
| $\mathrm{Sd}_x = L_xR_{x^{\dagger}}$ | Composition of a left and a right multiplication |
| $\mathrm{Sd}_x^{*} = \mathrm{Sd}_{x^{\dagger}}$ | Adjoint for the form |
| $\mathrm{Sd}_{x^{\dagger}x}\geq0$ | Positivity of the adjoint products |
| $\mathrm{Sd}_x$ unitary $\iff$ $x^{\dagger}x = xx^{\dagger} = 1$ | The unitarity condition |
| $\sigma_t = \mathrm{Ad}\,\Delta^{it}$ | Modular flow, generally outer |
| $\jmath\Delta^{it}\jmath = \Delta^{-it}$ | The conjugation inverts the flow |

## Further Reading

- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for two-sided operators on a Hermitian algebra.
- Serban Stratila and László Zsidó, *Lectures on von Neumann Algebras* (Abacus Press, 1979), for the two-sided operator and the regular representations.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 2 (Academic Press, 1986), for the modular operator and the adjoint of a two-sided action.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the modular comparison of the two adjoints.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, vol. 1 (Springer, 1987), for the standard form and the two-sided operators.
