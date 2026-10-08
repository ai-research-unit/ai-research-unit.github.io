# __The Signed Adjoint on a Hermitian Module__

## Introduction

A Hermitian module over a graded Hermitian algebra carries the action of the algebra and the form for which the action is self-adjoint, $(x\cdot s,t) = (s,x^{\dagger}\cdot t)$; its **signed action** is the action of the twisted parameter, $\rho^{\alpha}(x) = \rho(\alpha(x))$, which on a homogeneous parameter is the scalar multiple $\rho^{\alpha}(x) = \varepsilon_x\rho(x)$ with $\varepsilon_x = (-1)^{|x|}$. This article computes the adjoint of the signed action and the self-adjointness condition it carries.

Two facts decide the computation. The first is that the dagger of a Hermitian algebra commutes with the grade involution, $\alpha(x)^{\dagger} = \alpha(x^{\dagger})$, so the adjoint of the signed action is the signed action of the involution,

$$
\rho^{\alpha}(x)^{*} = \rho^{\alpha}(x^{\dagger}) ,
$$

the sign passing through adjunction unchanged. The second is that the products $x^{\dagger}x$ and $xx^{\dagger}$ are even, so the operator products of the signed action are the unsigned ones, $\rho^{\alpha}(x)^{*}\rho^{\alpha}(x) = \rho(x^{\dagger}x)$; consequently **self-adjointness, normality, unitarity and the positivity of the products are governed by the same conditions as for the ordinary action**, and the sign is visible only in the value of the operator at a homogeneous element and in the parametrisation. This is the module form of the statement of *The Signed Adjoint of the Sandwich on a Hermitian Algebra* that the sign is a real scalar and adjunction does not see it.

This article fixes the signed action and its adjoint, the self-adjointness, normality and unitarity conditions, the module involution and the sign rule, and the behaviour under the modular objects.

The module, its form and the self-adjointness axiom are *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*; the adjoint of the action is *The Adjoint of the One-Sided Action with Hermitian Adjoint*; the module adjoint calculus and the induced involution are *The Hermitian Adjoint on a Hermitian Module*; the grading and the signed multiplications are *The Grading of a Hermitian Algebra with Signed Hermitian Adjoint* and *One-Sided Operators on a Hermitian Algebra with Signed Hermitian Adjoint*; the modular objects are *The Modular Operator and Tomita-Takesaki Theory*. Those are cited. The algebra is $A$ with involution $\dagger$, grade involution $\alpha$ commuting with $\dagger$, and form $\langle\cdot,\cdot\rangle$; the module is $M$ with form $(\cdot,\cdot)$ and action $x\cdot s$; the modular objects of the module are $\jmath_M$ and $\Delta_M$.

## The Signed Action and Its Adjoint

**Definition.** The **signed action** of the algebra on the module is

$$
\rho^{\alpha}(x)\,s = \alpha(x)\cdot s ,
$$

so that $\rho^{\alpha}(x) = \rho(\alpha(x))$; on a homogeneous $x$ it is $\rho^{\alpha}(x) = \varepsilon_x\rho(x)$.

**Theorem (the adjoint of the signed action).** For every $x$,

$$
\rho^{\alpha}(x)^{*} = \rho^{\alpha}(x^{\dagger}) .
$$

**Proof.** $\rho^{\alpha}(x)^{*} = \rho(\alpha(x))^{*} = \rho(\alpha(x)^{\dagger})$ by the adjoint of the action of *The Adjoint of the One-Sided Action with Hermitian Adjoint*, and $\alpha(x)^{\dagger} = \alpha(x^{\dagger})$ because the dagger is even; assembling gives the display.

**Corollary (the sign passes through adjunction).** For homogeneous $x$,

$$
\rho^{\alpha}(x)^{*} = \varepsilon_x\,\rho(x^{\dagger}) = \varepsilon_x\,\rho(x)^{*} ,
$$

so the signed action and the ordinary action have adjoints carrying the same sign; adjunction commutes with the grade involution.

**Proposition (the signed action is a reparametrisation).** The map $x\mapsto\rho^{\alpha}(x)$ is a representation of $A$, $\rho^{\alpha}(xz) = \rho^{\alpha}(x)\rho^{\alpha}(z)$, with the same image as the ordinary action: $\rho^{\alpha}(A) = \rho(A)$.

**Proof.** Multiplicativity is $\alpha(xz) = \alpha(x)\alpha(z)$ and multiplicativity of the action; the images agree because $\alpha$ is a bijection of $A$ onto itself.

**Proposition (the value on homogeneous parameters).** For homogeneous $x$ and every $s$,

$$
\rho^{\alpha}(x)\,s = \begin{cases} \ \ \rho(x)\,s , & x \text{ even}, \\ -\rho(x)\,s , & x \text{ odd}, \end{cases}
$$

so the signed action agrees with the ordinary action on the even part of the algebra and is its negative on the odd part.

**Proof.** $\alpha(x) = \varepsilon_xx$ for homogeneous $x$ and the scalar $\varepsilon_x$ acts on the module through the action of the scalars.

## Self-Adjointness, Normality and Unitarity

**Theorem (the criteria).** For $x\in A$:

1. $\rho^{\alpha}(x)$ is self-adjoint exactly when $x = x^{\dagger}$;
2. it is skew-adjoint exactly when $x^{\dagger} = -x$;
3. it is normal exactly when $xx^{\dagger} = x^{\dagger}x$;
4. it is unitary exactly when $xx^{\dagger} = x^{\dagger}x = 1$;
5. it is positive, for self-adjoint $x$, exactly when $x$ lies in the positive cone of the algebra.

**Proof.** By the theorem, $\rho^{\alpha}(x)^{*} = \rho^{\alpha}(x^{\dagger}) = \rho(\alpha(x^{\dagger}))$; the representation is faithful on the subalgebra generated by $x$ in the cases below, so equality of operators is equality of parameters. For normality, $\rho^{\alpha}(x)^{*}\rho^{\alpha}(x) = \rho^{\alpha}(x^{\dagger}x) = \rho(x^{\dagger}x)$ and $\rho^{\alpha}(x)\rho^{\alpha}(x)^{*} = \rho(xx^{\dagger})$, the equalities to the unsigned action holding because $x^{\dagger}x$ and $xx^{\dagger}$ are even; unitarity is the same with the value $\mathrm{id}$; positivity is $(x\cdot s,s)\geq0$ for self-adjoint $x$ in the cone.

**Corollary (the sign is invisible to every operator criterion).** Self-adjointness, skew-adjointness, normality, unitarity and the positivity of the operator products of the signed action are exactly those of the ordinary action; the signed action is therefore a rescaling of the ordinary action by a real sign and not a different operator family.

**Proof.** The criteria of the theorem depend only on the involution of the parameter and on the products $x^{\dagger}x$, $xx^{\dagger}$, which are even; the formulae of the proof show that the signed and unsigned operator products coincide.

**Remark (where the sign is visible on the module).** The sign is visible in the value $\rho^{\alpha}(x)s$ on an odd parameter and in the parametrisation of the family; it is invisible in the adjoint, in the modulus and in all the criteria. This is the module counterpart of the corresponding statement for the signed sandwich, and it is the reason the signed structure of the corpus can be described as the *same* operators with a graded bookkeeping.

## The Module Involution and the Sign Rule

**Definition.** Let $\xi$ be cyclic and separating for the action, so that $x\cdot\xi = 0$ forces $x = 0$, and let $S_M(x\cdot\xi) = x^{\dagger}\cdot\xi$ be the module involution of *The Hermitian Adjoint on a Hermitian Module*, with polar decomposition $\bar S_M = \jmath_M\Delta_M^{1/2}$.

**Proposition (the involution conjugates the signed action).** On the bimodule case, where the right action $\sigma$ of the algebra is defined, the module involution satisfies

$$
S_M\,\rho^{\alpha}(x)\,S_M = \sigma^{\alpha}(x^{\dagger}) \quad\text{on } A\cdot\xi ,
$$

where $\sigma^{\alpha}(y)$ is the signed right action, $s\mapsto s\cdot\alpha(y)$; so the conjugation by the module involution turns the signed left action into the signed right action of the involution.

**Proof.** $S_M\rho^{\alpha}(x)S_M(y\cdot\xi) = S_M(\alpha(x)y^{\dagger}\cdot\xi) = (\alpha(x)y^{\dagger})^{\dagger}\cdot\xi = y\alpha(x)^{\dagger}\cdot\xi = y\alpha(x^{\dagger})\cdot\xi = \sigma^{\alpha}(x^{\dagger})(y\cdot\xi)$, using that the dagger is even.

**Corollary (the sign rule is preserved by the conjugation).** For homogeneous $x$ the conjugation carries the scalar $\varepsilon_x$ across,

$$
S_M\,\rho^{\alpha}(x)\,S_M = \varepsilon_x\,S_M\,\rho(x)\,S_M = \sigma^{\alpha}(x^{\dagger}) ,
$$

so the sign rule and the exchange of sides are compatible; the sign is not disturbed by the exchange.

**Proof.** $\rho^{\alpha}(x) = \varepsilon_x\rho(x)$ for homogeneous $x$, and $S_M\rho(x)S_M = \sigma(x^{\dagger})$ by the module involution of *The Hermitian Adjoint on a Hermitian Module*; the definition of $\sigma^{\alpha}$ gives the claim.

**Proposition (the modular flow on the signed action).** The modular group of the module acts by

$$
\Delta_M^{it}\,\rho^{\alpha}(x)\,\Delta_M^{-it} = \rho^{\alpha}(\sigma_t(x)) ,
$$

with $\sigma_t$ the modular automorphism of the algebra; the flow preserves the parity, $\varepsilon_{\sigma_t(x)} = \varepsilon_x$, so it preserves the sign.

**Proof.** The modular flow acts on the coefficients of the action, as in *The Hermitian Adjoint on a Hermitian Module*, and the parity invariance is the even-ness of the modular automorphism of *The Grading of a Hermitian Algebra with Signed Hermitian Adjoint*.

**Remark (the modular objects and the sign).** The module involution, its polar decomposition and the modular flow are all defined by the form and the involution and do not involve the grade involution; they are therefore compatible with the signed action in the strong sense that they preserve its defining sign, and this is why the signed action may be used in place of the ordinary one whenever the parametrisation by parity is convenient.

## Worked Cases

### The Regular Module

For $M = A$ with the form $(s,t) = \langle s,t\rangle$ and $\xi = 1$, the signed action is the signed left multiplication $\Lambda^{\alpha}_x$ and the theorem is the identity $(\Lambda^{\alpha}_x)^{*} = \Lambda^{\alpha}_{x^{\dagger}}$; the conjugation by the module involution is $S\Lambda^{\alpha}_xS = \mathrm{P}^{\alpha}_{x^{\dagger}}$, the signed right multiplication.

### The Vector Module

For $M = \mathbb{C}^{n}$ over $A = M_n(\mathbb{C})$ with $\rho(x)s = xs$, the grading being given by an involution $\gamma$ of $\mathbb{C}^{n}$, the signed action of an odd matrix is minus the multiplication by it; the adjoint is the signed action of the conjugate transpose, and the criteria of the theorem reduce to the usual ones for matrices.

### An Odd Parameter

Let $u$ be odd with $u^{\dagger} = -u$. Then $\rho^{\alpha}(u) = -\rho(u)$ and $\rho^{\alpha}(u)^{*} = \rho^{\alpha}(u^{\dagger}) = -\rho^{\alpha}(u)$, so the signed action is skew-adjoint, and so is the ordinary action, $-\rho(u)$; the sign does not change the adjointness class, it only rescales the operator.

## Summary

The **signed action** on a Hermitian module is $\rho^{\alpha}(x) = \rho(\alpha(x))$, equal to $\varepsilon_x\rho(x)$ on a homogeneous parameter, and its **adjoint** is

$$
\rho^{\alpha}(x)^{*} = \rho^{\alpha}(x^{\dagger}) ,
$$

the sign passing through adjunction unchanged because the dagger is even, $\alpha(x)^{\dagger} = \alpha(x^{\dagger})$; for homogeneous $x$ the signed action is the ordinary one on the even part and its negative on the odd part. The **criteria** are those of the ordinary action: self-adjoint exactly when $x = x^{\dagger}$, skew-adjoint exactly when $x^{\dagger} = -x$, normal exactly when $xx^{\dagger} = x^{\dagger}x$, unitary exactly when $xx^{\dagger} = x^{\dagger}x = 1$, and positive for self-adjoint $x$ in the positive cone; the operator products agree, $\rho^{\alpha}(x)^{*}\rho^{\alpha}(x) = \rho(x^{\dagger}x)$, because $x^{\dagger}x$ is even, so the sign is invisible to every operator criterion and visible only in the value on an odd parameter and in the parametrisation. The **module involution** conjugates the signed action into the signed right action of the involution, $S_M\rho^{\alpha}(x)S_M = \sigma^{\alpha}(x^{\dagger})$, with the sign rule preserved, and the **modular flow** acts by $\Delta_M^{it}\rho^{\alpha}(x)\Delta_M^{-it} = \rho^{\alpha}(\sigma_t(x))$ with the parity preserved. The module and its axiom are *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*, the module involution is *The Hermitian Adjoint on a Hermitian Module*, the signed multiplications are *One-Sided Operators on a Hermitian Algebra with Signed Hermitian Adjoint*, and the modular objects are *The Modular Operator and Tomita-Takesaki Theory*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho^{\alpha}(x) = \rho(\alpha(x))$ | The signed action |
| $\rho^{\alpha}(x) = \varepsilon_x\rho(x)$ | Value on a homogeneous parameter |
| $\rho^{\alpha}(x)^{*} = \rho^{\alpha}(x^{\dagger})$ | The adjoint |
| $\alpha(x)^{\dagger} = \alpha(x^{\dagger})$ | The dagger is even |
| $\rho^{\alpha}(x)^{*}\rho^{\alpha}(x) = \rho(x^{\dagger}x)$ | The product is unsigned |
| $x = x^{\dagger}$, $x^{\dagger} = -x$, $xx^{\dagger} = x^{\dagger}x$, $xx^{\dagger} = x^{\dagger}x = 1$ | Self-adjoint, skew-adjoint, normal, unitary |
| $S_M\rho^{\alpha}(x)S_M = \sigma^{\alpha}(x^{\dagger})$ | Conjugation into the signed right action |
| $\Delta_M^{it}\rho^{\alpha}(x)\Delta_M^{-it} = \rho^{\alpha}(\sigma_t(x))$ | Modular flow |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for self-adjointness, normality and the adjoint calculus on a module.
- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for Hermitian modules and the induced involution.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutions commuting with an automorphism and the Hermitian forms they define.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the grade involution and its commutation with the involution of a Clifford algebra.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the modular flow on the coefficients of an action.
