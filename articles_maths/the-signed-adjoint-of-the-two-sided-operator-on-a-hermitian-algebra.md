# __The Signed Adjoint of the Two-Sided Operator on a Hermitian Algebra__

## Introduction

The two-sided operator of a Hermitian algebra is $\mathrm{Sd}_x(y) = xyx^{\dagger}$, and its signed version is $\mathrm{Sd}^{\alpha}_x = \Lambda^{\alpha}_xR_{x^{\dagger}}$, the two-sided operator whose left factor carries the grade involution, $\Lambda^{\alpha}_x(y) = \alpha(x)y$; on a homogeneous element it is the scalar multiple $\mathrm{Sd}^{\alpha}_x = \varepsilon_x\mathrm{Sd}_x$ with $\varepsilon_x = (-1)^{|x|}$, so the signed two-sided operator is the Hermitian pair on the even part and its negative on the odd part. This article computes its **adjoint** and follows the sign through the computation.

The result is that the adjoint of the signed two-sided operator is the signed two-sided operator of the involution,

$$
\bigl(\mathrm{Sd}^{\alpha}_x\bigr)^{*} = \mathrm{Sd}^{\alpha}_{x^{\dagger}} ,
$$

with the sign preserved: adjacency commutes with the grade involution because the involution does not change the parity, $\varepsilon_{x^{\dagger}} = \varepsilon_x$. Three further facts complete the picture. Self-adjointness of the signed two-sided operator is again $x = x^{\dagger}$. The unitarity criterion is again $x^{\dagger}x = xx^{\dagger} = 1$, and here the sign drops out of the computation, because $x^{\dagger}x$ is even and $\varepsilon_{x^{\dagger}x} = +1$: the sign is visible in the operator and invisible in its modulus. And the modular conjugation leaves the signed two-sided operator invariant, $\jmath\bar\mathrm{Sd}^{\alpha}_x\jmath = \bar\mathrm{Sd}^{\alpha}_x$, because the sign is a real scalar and $\jmath$ is antilinear; so the signed two-sided operator sits in the same place as the unsigned one with respect to the exchange between the algebra and its commutant.

This article fixes the signed two-sided operator, its adjoint, the sign rule for adjunction, the self-adjointness and unitarity criteria, and the behaviour under the modular conjugation and the modular flow.

The grading, the sign rule and the signed multiplication operators are *The Grading of a Hermitian Algebra with Signed Hermitian Adjoint* and *One-Sided Operators on a Hermitian Algebra with Signed Hermitian Adjoint*; the unsigned two-sided operator and its adjoint are *The Adjoint of the Two-Sided Operator on a Hermitian Algebra* and *The Hermitian Pair of Operators on a Hermitian Algebra with Hermitian Adjoint*; the adjoints of the multiplications are *The Adjoint of the Left and the Right Multiplication*; the modular objects are *The Modular Operator and Tomita-Takesaki Theory*; the positivity and the cone are *Self-Adjoint Elements and the Positive Cone*. Those are cited. The algebra is $A$ with involution $\dagger$, parity grading and grade involution $\alpha$, form $\langle\cdot,\cdot\rangle$; a homogeneous element has parity $|x|$ and sign $\varepsilon_x = (-1)^{|x|}$.

## The Signed Two-Sided Operator and Its Adjoint

**Definition.** For $x\in A$ the **signed Hermitian pair** is

$$
\mathrm{Sd}^{\alpha}_x = \Lambda^{\alpha}_x\circ R_{x^{\dagger}} , \qquad \Lambda^{\alpha}_x(y) = \alpha(x)\,y , \qquad R_{x^{\dagger}}(y) = y\,x^{\dagger} ,
$$

the composition of the signed left multiplication and the dagger right multiplication; on a homogeneous $x$ it is $\mathrm{Sd}^{\alpha}_x = \varepsilon_x\mathrm{Sd}_x$ with $\mathrm{Sd}_x = L_xR_{x^{\dagger}}$ the unsigned two-sided operator.

**Theorem (the adjoint).** For every $x$,

$$
\boxed{\;\bigl(\mathrm{Sd}^{\alpha}_x\bigr)^{*} = \mathrm{Sd}^{\alpha}_{x^{\dagger}}\;} ,
$$

the adjoint being taken for the form; so the adjoint of the signed two-sided operator is the signed two-sided operator of the involution.

**Proof.** The adjoints of the two factors are $(\Lambda^{\alpha}_x)^{*} = \Lambda^{\alpha}_{x^{\dagger}}$ and $(R_{x^{\dagger}})^{*} = R_x$; the adjoint of a product reverses the order, so $(\mathrm{Sd}^{\alpha}_x)^{*} = R_x\Lambda^{\alpha}_{x^{\dagger}}$; and $R_x\Lambda^{\alpha}_{x^{\dagger}}(y) = \alpha(x^{\dagger})\,y\,x = \mathrm{Sd}^{\alpha}_{x^{\dagger}}(y)$, since the right factor of $\mathrm{Sd}^{\alpha}_{x^{\dagger}}$ is $(x^{\dagger})^{\dagger} = x$.

**Proposition (the adjoint products).** For every $x$,

$$
\bigl(\mathrm{Sd}^{\alpha}_x\bigr)^{*}\mathrm{Sd}^{\alpha}_x = \mathrm{Sd}^{\alpha}_{x^{\dagger}x} = \mathrm{Sd}_{x^{\dagger}x} , \qquad \mathrm{Sd}^{\alpha}_x\bigl(\mathrm{Sd}^{\alpha}_x\bigr)^{*} = \mathrm{Sd}^{\alpha}_{xx^{\dagger}} = \mathrm{Sd}_{xx^{\dagger}} ,
$$

the equalities to the unsigned two-sided operators holding because $x^{\dagger}x$ and $xx^{\dagger}$ are even.

**Proof.** Multiplicativity of the two-sided family, $\mathrm{Sd}^{\alpha}_z\mathrm{Sd}^{\alpha}_w = \mathrm{Sd}^{\alpha}_{zw}$, applied to the two products; the parity of a product of an element with its involution is even because the involution preserves parity, so $\varepsilon_{x^{\dagger}x} = \varepsilon_{xx^{\dagger}} = +1$ and the signed member equals the unsigned one there.

**Corollary (the adjoint products are positive).** $\langle(\mathrm{Sd}^{\alpha}_x)^{*}\mathrm{Sd}^{\alpha}_xu,u\rangle\geq0$ for every $u$, so the signed two-sided operator is a bounded operator with positive modulus square, and the family of signed two-sided operators is closed under adjunction.

**Proof.** The products are two-sided operators of the positive elements $x^{\dagger}x$ and $xx^{\dagger}$, and the positivity of the two-sided operator of a positive element is the unsigned statement of *The Adjoint of the Two-Sided Operator on a Hermitian Algebra*.

**Remark (why the sign survives adjunction).** The sign of the signed two-sided operator is the parity sign $\varepsilon_x$ of the parameter. Adjunction replaces $x$ by $x^{\dagger}$, and the involution preserves the grading, so it preserves the sign; the parity is therefore the part of the parameter that adjunction does not see, and this is the sense in which the sign is compatible with the adjoint operation rather than disturbed by it.

## The Sign Rule

**Theorem (multiplicativity and the parity table).** For all $x, z$ one has $\mathrm{Sd}^{\alpha}_{xz} = \mathrm{Sd}^{\alpha}_x\mathrm{Sd}^{\alpha}_z$; for homogeneous parameters

$$
\boxed{\;\mathrm{Sd}^{\alpha}_x\mathrm{Sd}^{\alpha}_z = \varepsilon_x\varepsilon_z\,\mathrm{Sd}_{xz}\;} ,
$$

so the composite of two signed two-sided operators is the ordinary two-sided operator exactly when the parameters have the same parity, and in particular when both are odd.

**Proof.** The dagger is an anti-automorphism and $\alpha$ an automorphism, giving multiplicativity; the parity-sign identity $\mathrm{Sd}^{\alpha}_x = \varepsilon_x\mathrm{Sd}_x$ and the multiplicativity of the unsigned family give the composite formula.

**Proposition (adjunction and the sign).** The adjoint operation commutes with the sign in the sense

$$
\bigl(\mathrm{Sd}^{\alpha}_x\bigr)^{*} = \varepsilon_x\,\bigl(\mathrm{Sd}_x\bigr)^{*} = \varepsilon_x\,\mathrm{Sd}_{x^{\dagger}} = \mathrm{Sd}^{\alpha}_{x^{\dagger}} ,
$$

so the adjoint of the signed family is obtained from the adjoint of the unsigned family by the *same* sign, and the parity table of the composition is unchanged by adjunction.

**Proof.** The first equality is $\mathrm{Sd}^{\alpha}_x = \varepsilon_x\mathrm{Sd}_x$ with the real scalar $\varepsilon_x$; the second is the adjoint of the unsigned two-sided operator; the third is $\varepsilon_{x^{\dagger}} = \varepsilon_x$.

| $x$ | $\mathrm{Sd}^{\alpha}_x$ | $\bigl(\mathrm{Sd}^{\alpha}_x\bigr)^{*}$ | self-adjoint? |
|---|---|---|---|
| even, $x = x^{\dagger}$ | $\mathrm{Sd}_x$ | $\mathrm{Sd}_x$ | yes |
| even, $x^{\dagger} = -x$ | $\mathrm{Sd}_x$ | $\mathrm{Sd}_{-x} = \mathrm{Sd}_x$ | yes |
| odd, $x = x^{\dagger}$ | $-\mathrm{Sd}_x$ | $-\mathrm{Sd}_x$ | yes |
| odd, $x^{\dagger} = -x$ | $-\mathrm{Sd}_x$ | $-\mathrm{Sd}_{-x} = -\mathrm{Sd}_x$ | yes |
| $x^{\dagger}\neq \pm x$ | $\varepsilon_x\mathrm{Sd}_x$ | $\varepsilon_x\mathrm{Sd}_{x^{\dagger}}$ | no |

**Corollary (self-adjointness).** For every $x$ the signed two-sided operator is self-adjoint exactly when $\mathrm{Sd}_{x^{\dagger}} = \mathrm{Sd}_x$, and this holds whenever $x^{\dagger} = \pm x$. In particular the signed two-sided operator of a self-adjoint parameter and the signed two-sided operator of an odd anti-self-adjoint parameter are both self-adjoint.

**Proof.** $\mathrm{Sd}^{\alpha}_{x^{\dagger}} = \varepsilon_{x^{\dagger}}\mathrm{Sd}_{x^{\dagger}} = \varepsilon_x\mathrm{Sd}_{x^{\dagger}}$ is compared with $\mathrm{Sd}^{\alpha}_x = \varepsilon_x\mathrm{Sd}_x$; the common real scalar $\varepsilon_x$ is nonzero, so equality is $\mathrm{Sd}_{x^{\dagger}} = \mathrm{Sd}_x$. The map $x\mapsto\mathrm{Sd}_x$ is even in the parameter, $\mathrm{Sd}_{-x} = L_{-x}R_{(-x)^{\dagger}} = L_xR_{x^{\dagger}} = \mathrm{Sd}_x$, so both $x^{\dagger} = x$ and $x^{\dagger} = -x$ give self-adjointness; the map is not injective, and self-adjointness of the operator therefore does not force $x = x^{\dagger}$.

## Unitarity and the Modular Conjugation

**Theorem (the unitarity criterion).** For every $x$ the following are equivalent: (1) $\mathrm{Sd}^{\alpha}_x$ is isometric for the form; (2) $(\mathrm{Sd}^{\alpha}_x)^{*}\mathrm{Sd}^{\alpha}_x = \mathrm{id}$; (3) $\mathrm{Sd}_{x^{\dagger}x} = \mathrm{id}$, which holds in particular when $x^{\dagger}x = 1$; and $\mathrm{Sd}^{\alpha}_x$ is unitary exactly when $x^{\dagger}x = xx^{\dagger} = 1$. The sign does not appear in the criterion.

**Proof.** $(\mathrm{Sd}^{\alpha}_x)^{*}\mathrm{Sd}^{\alpha}_x = \mathrm{Sd}_{x^{\dagger}x}$ by the adjoint-product proposition, and $\mathrm{Sd}_{x^{\dagger}x} = \mathrm{id}$ is the stated form of the criterion, implied by $x^{\dagger}x = 1$; the unitary statement adds the other side.

**Proposition (invariance under the modular conjugation).** The signed two-sided operator is invariant under the modular conjugation of the standard form,

$$
\jmath\,\bar\mathrm{Sd}^{\alpha}_x\,\jmath = \bar\mathrm{Sd}^{\alpha}_x ,
$$

because the sign is a real scalar and the modular conjugation is antilinear with $\jmath^{2} = \mathrm{id}$.

**Proof.** $\jmath\bar\mathrm{Sd}^{\alpha}_x\jmath = \varepsilon_x\,\jmath\bar\mathrm{Sd}_x\jmath = \varepsilon_x\bar\mathrm{Sd}_x = \bar\mathrm{Sd}^{\alpha}_x$, using the invariance of the unsigned two-sided operator of *The Adjoint of the Two-Sided Operator on a Hermitian Algebra*.

**Proposition (the modular flow on the signed family).** The modular automorphism $\sigma_t(x) = \Delta^{it}x\Delta^{-it}$ acts by

$$
\boxed{\;\Delta^{it}\,\bar\mathrm{Sd}^{\alpha}_x\,\Delta^{-it} = \bar\mathrm{Sd}^{\alpha}_{\sigma_t(x)}\;} ,
$$

and it preserves the parity, $\varepsilon_{\sigma_t(x)} = \varepsilon_x$, so it preserves the sign; the modular flow therefore acts on the family of signed two-sided operators through its action on the parameters and commutes with the sign bookkeeping.

**Proof.** The modular group conjugates a two-sided operator into the two-sided operator of the conjugated parameter by *The Modular Operator and Tomita-Takesaki Theory*; the invariance of the parity is the even-ness of the modular automorphism for a graded Hermitian algebra, from *The Grading of a Hermitian Algebra with Signed Hermitian Adjoint*.

**Remark (the sign and the modular structure).** The sign is a real scalar attached to the parameter and preserved by the involution, by the modular conjugation and by the modular flow; so the signed two-sided operator is as modular as the unsigned one. What the sign changes is the value at the unit, $\mathrm{Sd}^{\alpha}_x(1) = \varepsilon_xxx^{\dagger}$, and the composition table; what it leaves alone is the adjoint operation, the operator products and the invariance under the modular objects.

## Worked Cases

### Odd and Even Parameters

In a graded Hermitian algebra let $u$ be an odd element with $u^{\dagger} = -u$, for instance $u = i\sigma_x$ with the grading $\alpha(a) = \gamma a\gamma$, $\gamma = \mathrm{diag}(1,-1)$, in $M_2(\mathbb{C})$. Then $\mathrm{Sd}^{\alpha}_u = -\mathrm{Sd}_u$ and $(\mathrm{Sd}^{\alpha}_u)^{*} = \mathrm{Sd}^{\alpha}_{u^{\dagger}} = \mathrm{Sd}^{\alpha}_{-u} = -\mathrm{Sd}_{-u} = -\mathrm{Sd}_u = \mathrm{Sd}^{\alpha}_u$, so the signed two-sided operator is self-adjoint although $u\neq u^{\dagger}$; the unsigned two-sided operator of the same element is self-adjoint too, $\mathrm{Sd}_u^{*} = \mathrm{Sd}_{u^{\dagger}} = \mathrm{Sd}_{-u} = \mathrm{Sd}_u$. This is the smallest case where self-adjointness fails to force the parameter to be self-adjoint. The involution preserves the parity, so the sign survives in both.

### A Group Algebra with Trivial Grading

If the involution and the parity are both trivial, $\alpha = \mathrm{id}$, then $\mathrm{Sd}^{\alpha}_x = \mathrm{Sd}_x$ and the article reduces to the unsigned case: the adjoint is the two-sided operator of the involution, the criteria are those of *The Adjoint of the Two-Sided Operator on a Hermitian Algebra*, and the sign does nothing.

### An Even Unitary Parameter

For an even unitary $x$, $\mathrm{Sd}^{\alpha}_x = \mathrm{Sd}_x = \mathrm{Ad}_x$ is an isometry and in fact unitary, and the adjoint is $\mathrm{Sd}_{x^{\dagger}} = \mathrm{Sd}_{x^{-1}}$, the inverse inner automorphism; the sign is $+1$ and the adjunction behaves as in the unsigned theory.

## Summary

The **signed Hermitian pair** is $\mathrm{Sd}^{\alpha}_x = \Lambda^{\alpha}_xR_{x^{\dagger}}$ with $\Lambda^{\alpha}_x(y) = \alpha(x)y$, equal to $\varepsilon_x\mathrm{Sd}_x$ on a homogeneous parameter, and its **adjoint** is

$$
\bigl(\mathrm{Sd}^{\alpha}_x\bigr)^{*} = \mathrm{Sd}^{\alpha}_{x^{\dagger}} ,
$$

the sign being preserved because the involution preserves the parity, $\varepsilon_{x^{\dagger}} = \varepsilon_x$. Its adjoint products are $\mathrm{Sd}_{x^{\dagger}x}$ and $\mathrm{Sd}_{xx^{\dagger}}$, which are unsigned because $x^{\dagger}x$ and $xx^{\dagger}$ are even, so the **unitarity criterion** is the unsigned one, $(\mathrm{Sd}^{\alpha}_x)^{*}\mathrm{Sd}^{\alpha}_x = \mathrm{Sd}_{x^{\dagger}x} = \mathrm{id}$ (in particular $x^{\dagger}x = 1$), and **self-adjointness** is $\mathrm{Sd}_{x^{\dagger}} = \mathrm{Sd}_x$, which holds for $x^{\dagger} = \pm x$. The **sign rule** of the composition is unchanged by adjunction, since adjunction multiplies both the operator and its adjoint by the same scalar, and the composite of two odd signed two-sided operators is an ordinary two-sided operator. The **modular conjugation** leaves the signed two-sided operator invariant, $\jmath\bar\mathrm{Sd}^{\alpha}_x\jmath = \bar\mathrm{Sd}^{\alpha}_x$, and the **modular flow** acts by $\Delta^{it}\bar\mathrm{Sd}^{\alpha}_x\Delta^{-it} = \bar\mathrm{Sd}^{\alpha}_{\sigma_t(x)}$ with the parity and the sign preserved; so the sign lives in the parameter, in the value at the unit and in the composition table, and nowhere in the adjoint operation. The grading and the signed multiplications are *The Grading of a Hermitian Algebra with Signed Hermitian Adjoint* and *One-Sided Operators on a Hermitian Algebra with Signed Hermitian Adjoint*, the unsigned adjoint is *The Adjoint of the Two-Sided Operator on a Hermitian Algebra*, and the modular objects are *The Modular Operator and Tomita-Takesaki Theory*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Sd}^{\alpha}_x = \Lambda^{\alpha}_xR_{x^{\dagger}}$ | Signed Hermitian pair |
| $\mathrm{Sd}^{\alpha}_x = \varepsilon_x\mathrm{Sd}_x$ | Parity sign, $\varepsilon_x = (-1)^{|x|}$ |
| $(\mathrm{Sd}^{\alpha}_x)^{*} = \mathrm{Sd}^{\alpha}_{x^{\dagger}}$ | The adjoint |
| $\varepsilon_{x^{\dagger}} = \varepsilon_x$ | Adjunction preserves the sign |
| $(\mathrm{Sd}^{\alpha}_x)^{*}\mathrm{Sd}^{\alpha}_x = \mathrm{Sd}_{x^{\dagger}x}$ | Adjoint product, unsigned |
| $x^{\dagger}x = xx^{\dagger} = 1$ | Unitarity criterion |
| $\jmath\bar\mathrm{Sd}^{\alpha}_x\jmath = \bar\mathrm{Sd}^{\alpha}_x$ | Invariance under the modular conjugation |
| $\Delta^{it}\bar\mathrm{Sd}^{\alpha}_x\Delta^{-it} = \bar\mathrm{Sd}^{\alpha}_{\sigma_t(x)}$ | Modular flow on the family |

## Further Reading

- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for two-sided operators on a Hermitian algebra and their adjoints.
- Serban Stratila and László Zsidó, *Lectures on von Neumann Algebras* (Abacus Press, 1979), for the two-sided operators and the modular conjugation.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the modular flow on the algebra of operators.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the grading and the grade involution of a Clifford algebra.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 2 (Academic Press, 1986), for the adjoint of a two-sided action and the modular structure.
