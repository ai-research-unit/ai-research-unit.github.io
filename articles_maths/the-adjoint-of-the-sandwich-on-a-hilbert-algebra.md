# __The Adjoint of the Sandwich on a Hilbert Algebra__

## Introduction

The two-sided operator, or **sandwich**, of a Hilbert algebra is $\Theta_x(y) = xyx^{\dagger}$, the composition of a left and a right multiplication, $\Theta_x = L_xR_{x^{\dagger}}$. Its adjoint for the form is again a sandwich, $\Theta_x^{*} = \Theta_{x^{\dagger}}$, so the sandwich is the natural two-sided operator of the theory and the family of sandwiches is closed under adjunction. The sandwich is normal, it preserves the positive cone in the appropriate sense, and its adjoint relation with its parameter is the sharpest form of the adjoint axiom for two-sided operators.

A sandwich has two unitarity properties, and they must not be confused. It is **self-adjoint** for the form exactly when $\Theta_{x^{\dagger}} = \Theta_x$, which holds in particular when the parameter is self-adjoint, $x = x^{\dagger}$; it is an **isometry** exactly when $\Theta_x^{*}\Theta_x = \Theta_{x^{\dagger}x}$ is the identity, which holds in particular when $x^{\dagger}x = 1$; and it is **unitary** exactly when $x^{\dagger}x = xx^{\dagger} = 1$, that is when $x$ is unitary in the algebra. So the unitarity of the sandwich is the unitarity of its parameter, and the unitary sandwiches are the norm-preserving two-sided operators of the algebra.

The **modular operator** enters when the two adjoints of a sandwich are compared. On the algebra the adjoint of $\Theta_x$ for the form is $\Theta_{x^{\dagger}}$; on the completion the Hilbert adjoint is $\Theta_{x^{*}}$, with $x^{*}$ the Hilbert adjoint of the parameter; the two parameters $x^{\dagger}$ and $x^{*}$ agree exactly when the standard form is tracial, and in general they differ by the modular operator through the Tomita operator $S = J\Delta^{1/2}$. So the modular operator describes the difference between the form-adjoint and the Hilbert-adjoint of the sandwich.

This article fixes the sandwich, its adjoint, the unitarity condition and the modular operator as the comparison between the two adjoints.

The Hilbert algebra and its involution are *Hilbert Algebras* and *Hermitian Adjoints on a Hilbert Algebra*; the multiplications and their adjoints are *The Adjoint of the Left and the Right Multiplication*; the completions and the modular objects are *The Completion of a Hilbert Algebra* and *The Modular Operator and Tomita-Takesaki Theory*. Those are cited. The algebra is $A$ with involution $\dagger$ and form $\langle\cdot,\cdot\rangle$, and the completion is $H$.

## The Sandwich and Its Adjoint

**Definition.** For $x\in A$ the **sandwich**, or two-sided operator, is

$$
\Theta_x : A\to A, \qquad \Theta_x(y) = x\,y\,x^{\dagger} .
$$

It is the composition $\Theta_x = L_xR_{x^{\dagger}} = R_{x^{\dagger}}L_x$ of a left and a right multiplication, and it is semilinear in the parameter up to the involution and linear in the argument.

**Theorem (the adjoint is the sandwich of the involution).** For every $x$,

$$
\Theta_x^{*} = \Theta_{x^{\dagger}} ,
$$

the adjoint being taken for the form.

**Proof.** By the adjoint axiom applied twice, $\langle \Theta_xy, z\rangle = \langle xyx^{\dagger}, z\rangle = \langle yx^{\dagger}, x^{\dagger}z\rangle = \langle y, x^{\dagger}z(x^{\dagger})^{\dagger}\rangle = \langle y,\Theta_{x^{\dagger}}z\rangle$.

**Proposition (positivity of the adjoint products).** $\Theta_x^{*}\Theta_x = \Theta_{x^{\dagger}x}$ and $\Theta_x\Theta_x^{*} = \Theta_{xx^{\dagger}}$; both are sandwiches of positive elements and hence are positive operators for the form, $\langle\Theta_{x^{\dagger}x}u,u\rangle\geq0$.

**Proof.** The composition law $\Theta_x\Theta_z = \Theta_{xz}$ holds by associativity, whence the two products; positivity is $\langle\Theta_{x^{\dagger}x}u,u\rangle = \langle x^{\dagger}x\,u, u\rangle = \langle x u, x u\rangle$ by the adjoint axiom.

**Proposition (normal and form-preserving maps).** $\Theta_x$ preserves the adjoint relation in the sense $\Theta_x(y^{\dagger}) = \Theta_{x^{\dagger}}(y)^{\dagger}$, and it maps the positive cone into itself when $x$ is such that $x^{\dagger}x\leq 1$.

**Proof.** $x y^{\dagger}x^{\dagger} = (xyx^{\dagger})^{\dagger}$ is the involution statement; the cone statement is the composition of the positivity of the two adjoint products with the stability of the cone under inner conjugation.

## The Unitarity Condition

**Theorem (the sandwich is an isometry exactly for unitary parameters).** For every $x$ the following are equivalent:

1. $\Theta_x$ is isometric for the form, $\langle\Theta_xy,\Theta_xz\rangle = \langle y,z\rangle$;
2. $\Theta_x^{*}\Theta_x = \mathrm{id}$, that is $\Theta_{x^{\dagger}x} = \mathrm{id}$;
3. $x^{\dagger}x = 1$ (when the left representation is faithful).

Similarly $\Theta_x$ is **unitary** exactly when $x^{\dagger}x = xx^{\dagger} = 1$, that is when $x$ is unitary.

**Proof.** The identity $\langle\Theta_xy,\Theta_xz\rangle = \langle\Theta_x^{*}\Theta_xy,z\rangle = \langle\Theta_{x^{\dagger}x}y,z\rangle$ gives the equivalence of 1 and 2; the faithfulness of the left representation identifies $\Theta_{x^{\dagger}x} = \mathrm{id}$ with $x^{\dagger}x = 1$; unitarity adds the inverse on the other side.

**Corollary (the unitary sandwiches form a group).** The parameters $x$ with $x^{\dagger}x = xx^{\dagger} = 1$ form a group, and $x\mapsto\Theta_x$ is a group homomorphism with $x\mapsto\Theta_{x^{\dagger}}$ for the inverse; the sandwiches realised are the two-sided operators preserving the form and the norm.

**Proof.** Multiplicativity of $\Theta$ is associativity, the inverse statement is the adjoint identity, and the preservation of the form is the theorem.

**Remark (self-adjointness against unitarity).** A sandwich is self-adjoint for the form exactly when $\Theta_{x^{\dagger}} = \Theta_x$; since the map $x\mapsto\Theta_x$ is even in the parameter, $\Theta_{-x} = \Theta_x$, this holds in particular for every self-adjoint parameter and every anti-self-adjoint one, and the parameter is recovered from the operator only up to sign. A sandwich is an isometry exactly when $\Theta_{x^{\dagger}x} = \mathrm{id}$, which holds in particular for a unitary parameter. The two conditions are independent, and a unitary parameter need not be self-adjoint. The self-adjoint sandwich of a positive parameter is the **Hermitian sandwich** of *The Hermitian Sandwich on a Hilbert Algebra with Hermitian Adjoint*, and its ordering properties are those of *Self-Adjoint Elements and the Positive Cone*.

## The Modular Operator

**Proposition (the sandwich commutes with the modular conjugation).** For every $x$ the sandwich is invariant under the modular conjugation of the standard form,

$$
\jmath\,\bar\Theta_x\,\jmath = \bar\Theta_x .
$$

So the two-sided operator is unchanged by the modular conjugation, which exchanges its two factors: $\jmath\bar L_x\jmath = \bar R_{x^{\dagger}}$ and $\jmath\bar R_{x^{\dagger}}\jmath = \bar L_x$.

**Proof.** Compose the two exchange identities of *The Adjoint of the Left and the Right Multiplication*.

**Corollary (the sandwich is an inner automorphism exactly for invertible parameters).** A sandwich $\Theta_x$ with $x$ invertible is the inner automorphism $\mathrm{Ad}_x$ of the algebra, and it preserves the form exactly when $x$ is unitary, in which case $x^{-1} = x^{\dagger}$; the correspondence $x\mapsto\Theta_x$ is a homomorphism of the unitary group onto the group of inner automorphisms of the form-preserving kind.

**Proof.** Multiplicativity is associativity of the product; preservation of the form is the unitarity condition; the inverse of a unitary element is its involution.

**Proposition (the modular flow).** The modular automorphism group $\sigma_t(a) = \Delta^{it}a\Delta^{-it}$ is implemented by the powers of the modular operator, and the modular conjugation inverts it, $\jmath\Delta^{it}\jmath = \Delta^{-it}$. The flow is generally **outer**: a sandwich realises an automorphism of the algebra only through an element of the algebra, and $\Delta^{it}$ is not such an element unless the algebra contains it.

**Proof.** The inversion is the modular conjugation theorem of *The Modular Operator and Tomita-Takesaki Theory*; the outerness is that $\Delta^{it}$ is defined through the modular operator and not through an element of the algebra.

**Remark (where the two theories of operators meet).** The sandwiches are the two-sided operators implemented by elements, that is, the inner automorphisms; the modular flow is implemented by the modular operator and is generally outer. The two theories meet at the invariance of the sandwich under the modular conjugation, which is the operator form of the exchange between the algebra and its commutant, and they separate at the outerness of the flow.

## Worked Cases

### The Group Algebra

For $A = \mathbb{C}[G]$ with the tracial standard form, $\Theta_g(y) = gyg^{-1}$ and $\Theta_g^{*} = \Theta_{g^{-1}}$, with $\Theta_g$ unitary for every $g$; the form-adjoint and the Hilbert adjoint coincide.

### Matrices

For $A = M_n(\mathbb{C})$ with the Hilbert–Schmidt form, $\Theta_a(y) = aya^{*}$ and $\Theta_a^{*} = \Theta_{a^{*}}$; the sandwich is unitary exactly when $a$ is unitary, and the discrepancy between the two adjoints vanishes because the form is tracial.

### The Density Matrix Picture

For the algebra of matrices with the form $\langle a,b\rangle = \mathrm{tr}(b^{*}a)$ the sandwich is $\Theta_a(b) = aba^{*}$, its adjoint is $\Theta_{a^{*}} = \Theta_{a^{\dagger}}$ because the form is tracial, and the modular conjugation $J(u) = u^{*}$ commutes with the sandwich; the sandwiches are exactly the inner automorphisms.

## Summary

The **sandwich** $\Theta_x(y) = xyx^{\dagger}$ is the composition $\Theta_x = L_xR_{x^{\dagger}}$ of a left and a right multiplication, its **adjoint for the form** is $\Theta_x^{*} = \Theta_{x^{\dagger}}$, and the adjoint products $\Theta_{x^{\dagger}x}$ and $\Theta_{xx^{\dagger}}$ are sandwiches of positive elements, hence positive. The **unitarity condition** is that $\Theta_x$ is an isometry exactly when $x^{\dagger}x = 1$ and unitary exactly when $x^{\dagger}x = xx^{\dagger} = 1$, so the unitary sandwiches are the two-sided form-preserving operators and the map $x\mapsto\Theta_x$ is a homomorphism of the unitary group of the algebra. The sandwich is **invariant under the modular conjugation**, $\jmath\bar\Theta_x\jmath = \bar\Theta_x$, so the two-sided operators are the inner automorphisms compatible with the exchange between the algebra and its commutant; the **modular flow** $\sigma_t = \mathrm{Ad}\,\Delta^{it}$ is implemented by the modular operator and is generally outer, so the sandwich produces the inner automorphisms and the modular operator produces the rest. The involution is *Hermitian Adjoints on a Hilbert Algebra*, the multiplications and their adjoints are *The Adjoint of the Left and the Right Multiplication*, the modular data is *The Modular Operator and Tomita-Takesaki Theory*, and the Hermitian case is *The Hermitian Sandwich on a Hilbert Algebra with Hermitian Adjoint*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Theta_x(y) = xyx^{\dagger}$ | The sandwich, or two-sided operator |
| $\Theta_x = L_xR_{x^{\dagger}}$ | Composition of a left and a right multiplication |
| $\Theta_x^{*} = \Theta_{x^{\dagger}}$ | Adjoint for the form |
| $\Theta_{x^{\dagger}x}\geq0$ | Positivity of the adjoint products |
| $\Theta_x$ unitary $\iff$ $x^{\dagger}x = xx^{\dagger} = 1$ | The unitarity condition |
| $\jmath\bar\Theta_x\jmath = \bar\Theta_x$ | Invariance under the modular conjugation |
| $\sigma_t = \mathrm{Ad}\,\Delta^{it}$ | Modular flow, generally outer |
| $\jmath\Delta^{it}\jmath = \Delta^{-it}$ | The conjugation inverts the flow |

## Further Reading

- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for two-sided operators on a Hilbert algebra.
- Serban Stratila and László Zsidó, *Lectures on von Neumann Algebras* (Abacus Press, 1979), for the sandwich and the regular representations.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 2 (Academic Press, 1986), for the modular operator and the adjoint of a two-sided action.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the modular comparison of the two adjoints.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, vol. 1 (Springer, 1987), for the standard form and the sandwich operators.
