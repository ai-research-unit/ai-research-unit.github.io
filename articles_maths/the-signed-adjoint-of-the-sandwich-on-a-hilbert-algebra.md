# __The Signed Adjoint of the Sandwich on a Hilbert Algebra__

## Introduction

The sandwich of a Hilbert algebra is $\Theta_x(y) = xyx^{\dagger}$, and its signed version is $\Theta^{\alpha}_x = \Lambda^{\alpha}_xR_{x^{\dagger}}$, the two-sided operator whose left factor carries the grade involution, $\Lambda^{\alpha}_x(y) = \alpha(x)y$; on a homogeneous element it is the scalar multiple $\Theta^{\alpha}_x = \varepsilon_x\Theta_x$ with $\varepsilon_x = (-1)^{|x|}$, so the signed sandwich is the Hermitian sandwich on the even part and its negative on the odd part. This article computes its **adjoint** and follows the sign through the computation.

The result is that the adjoint of the signed sandwich is the signed sandwich of the involution,

$$
\bigl(\Theta^{\alpha}_x\bigr)^{*} = \Theta^{\alpha}_{x^{\dagger}} ,
$$

with the sign preserved: adjacency commutes with the grade involution because the involution does not change the parity, $\varepsilon_{x^{\dagger}} = \varepsilon_x$. Three further facts complete the picture. Self-adjointness of the signed sandwich is again $x = x^{\dagger}$. The unitarity criterion is again $x^{\dagger}x = xx^{\dagger} = 1$, and here the sign drops out of the computation, because $x^{\dagger}x$ is even and $\varepsilon_{x^{\dagger}x} = +1$: the sign is visible in the operator and invisible in its modulus. And the modular conjugation leaves the signed sandwich invariant, $\jmath\bar\Theta^{\alpha}_x\jmath = \bar\Theta^{\alpha}_x$, because the sign is a real scalar and $\jmath$ is antilinear; so the signed sandwich sits in the same place as the unsigned one with respect to the exchange between the algebra and its commutant.

This article fixes the signed sandwich, its adjoint, the sign rule for adjunction, the self-adjointness and unitarity criteria, and the behaviour under the modular conjugation and the modular flow.

The grading, the sign rule and the signed multiplication operators are *The Grading of a Hilbert Algebra with Signed Hermitian Adjoint* and *One-Sided Operators on a Hilbert Algebra with Signed Hermitian Adjoint*; the unsigned two-sided operator and its adjoint are *The Adjoint of the Sandwich on a Hilbert Algebra* and *The Hermitian Sandwich on a Hilbert Algebra with Hermitian Adjoint*; the adjoints of the multiplications are *The Adjoint of the Left and the Right Multiplication*; the modular objects are *The Modular Operator and Tomita-Takesaki Theory*; the positivity and the cone are *Self-Adjoint Elements and the Positive Cone*. Those are cited. The algebra is $A$ with involution $\dagger$, parity grading and grade involution $\alpha$, form $\langle\cdot,\cdot\rangle$; a homogeneous element has parity $|x|$ and sign $\varepsilon_x = (-1)^{|x|}$.

## The Signed Sandwich and Its Adjoint

**Definition.** For $x\in A$ the **signed Hermitian sandwich** is

$$
\Theta^{\alpha}_x = \Lambda^{\alpha}_x\circ R_{x^{\dagger}} , \qquad \Lambda^{\alpha}_x(y) = \alpha(x)\,y , \qquad R_{x^{\dagger}}(y) = y\,x^{\dagger} ,
$$

the composition of the signed left multiplication and the dagger right multiplication; on a homogeneous $x$ it is $\Theta^{\alpha}_x = \varepsilon_x\Theta_x$ with $\Theta_x = L_xR_{x^{\dagger}}$ the unsigned sandwich.

**Theorem (the adjoint).** For every $x$,

$$
\bigl(\Theta^{\alpha}_x\bigr)^{*} = \Theta^{\alpha}_{x^{\dagger}} ,
$$

the adjoint being taken for the form; so the adjoint of the signed sandwich is the signed sandwich of the involution.

**Proof.** The adjoints of the two factors are $(\Lambda^{\alpha}_x)^{*} = \Lambda^{\alpha}_{x^{\dagger}}$ and $(R_{x^{\dagger}})^{*} = R_x$; the adjoint of a product reverses the order, so $(\Theta^{\alpha}_x)^{*} = R_x\Lambda^{\alpha}_{x^{\dagger}}$; and $R_x\Lambda^{\alpha}_{x^{\dagger}}(y) = \alpha(x^{\dagger})\,y\,x = \Theta^{\alpha}_{x^{\dagger}}(y)$, since the right factor of $\Theta^{\alpha}_{x^{\dagger}}$ is $(x^{\dagger})^{\dagger} = x$.

**Proposition (the adjoint products).** For every $x$,

$$
\bigl(\Theta^{\alpha}_x\bigr)^{*}\Theta^{\alpha}_x = \Theta^{\alpha}_{x^{\dagger}x} = \Theta_{x^{\dagger}x} , \qquad \Theta^{\alpha}_x\bigl(\Theta^{\alpha}_x\bigr)^{*} = \Theta^{\alpha}_{xx^{\dagger}} = \Theta_{xx^{\dagger}} ,
$$

the equalities to the unsigned sandwiches holding because $x^{\dagger}x$ and $xx^{\dagger}$ are even.

**Proof.** Multiplicativity of the sandwich family, $\Theta^{\alpha}_z\Theta^{\alpha}_w = \Theta^{\alpha}_{zw}$, applied to the two products; the parity of a product of an element with its involution is even because the involution preserves parity, so $\varepsilon_{x^{\dagger}x} = \varepsilon_{xx^{\dagger}} = +1$ and the signed member equals the unsigned one there.

**Corollary (the adjoint products are positive).** $\langle(\Theta^{\alpha}_x)^{*}\Theta^{\alpha}_xu,u\rangle\geq0$ for every $u$, so the signed sandwich is a bounded operator with positive modulus square, and the family of signed sandwiches is closed under adjunction.

**Proof.** The products are sandwiches of the positive elements $x^{\dagger}x$ and $xx^{\dagger}$, and the positivity of the sandwich of a positive element is the unsigned statement of *The Adjoint of the Sandwich on a Hilbert Algebra*.

**Remark (why the sign survives adjunction).** The sign of the signed sandwich is the parity sign $\varepsilon_x$ of the parameter. Adjunction replaces $x$ by $x^{\dagger}$, and the involution preserves the grading, so it preserves the sign; the parity is therefore the part of the parameter that adjunction does not see, and this is the sense in which the sign is compatible with the adjoint operation rather than disturbed by it.

## The Sign Rule

**Theorem (multiplicativity and the parity table).** For all $x, z$ one has $\Theta^{\alpha}_{xz} = \Theta^{\alpha}_x\Theta^{\alpha}_z$; for homogeneous parameters

$$
\Theta^{\alpha}_x\Theta^{\alpha}_z = \varepsilon_x\varepsilon_z\,\Theta_{xz} ,
$$

so the composite of two signed sandwiches is the ordinary sandwich exactly when the parameters have the same parity, and in particular when both are odd.

**Proof.** The dagger is an anti-automorphism and $\alpha$ an automorphism, giving multiplicativity; the parity-sign identity $\Theta^{\alpha}_x = \varepsilon_x\Theta_x$ and the multiplicativity of the unsigned family give the composite formula.

**Proposition (adjunction and the sign).** The adjoint operation commutes with the sign in the sense

$$
\bigl(\Theta^{\alpha}_x\bigr)^{*} = \varepsilon_x\,\bigl(\Theta_x\bigr)^{*} = \varepsilon_x\,\Theta_{x^{\dagger}} = \Theta^{\alpha}_{x^{\dagger}} ,
$$

so the adjoint of the signed family is obtained from the adjoint of the unsigned family by the *same* sign, and the parity table of the composition is unchanged by adjunction.

**Proof.** The first equality is $\Theta^{\alpha}_x = \varepsilon_x\Theta_x$ with the real scalar $\varepsilon_x$; the second is the adjoint of the unsigned sandwich; the third is $\varepsilon_{x^{\dagger}} = \varepsilon_x$.

| $x$ | $\Theta^{\alpha}_x$ | $\bigl(\Theta^{\alpha}_x\bigr)^{*}$ | self-adjoint? |
|---|---|---|---|
| even, $x = x^{\dagger}$ | $\Theta_x$ | $\Theta_x$ | yes |
| even, $x^{\dagger} = -x$ | $\Theta_x$ | $\Theta_{-x} = \Theta_x$ | yes |
| odd, $x = x^{\dagger}$ | $-\Theta_x$ | $-\Theta_x$ | yes |
| odd, $x^{\dagger} = -x$ | $-\Theta_x$ | $-\Theta_{-x} = -\Theta_x$ | yes |
| $x^{\dagger}\neq \pm x$ | $\varepsilon_x\Theta_x$ | $\varepsilon_x\Theta_{x^{\dagger}}$ | no |

**Corollary (self-adjointness).** For every $x$ the signed sandwich is self-adjoint exactly when $\Theta_{x^{\dagger}} = \Theta_x$, and this holds whenever $x^{\dagger} = \pm x$. In particular the signed sandwich of a self-adjoint parameter and the signed sandwich of an odd anti-self-adjoint parameter are both self-adjoint.

**Proof.** $\Theta^{\alpha}_{x^{\dagger}} = \varepsilon_{x^{\dagger}}\Theta_{x^{\dagger}} = \varepsilon_x\Theta_{x^{\dagger}}$ is compared with $\Theta^{\alpha}_x = \varepsilon_x\Theta_x$; the common real scalar $\varepsilon_x$ is nonzero, so equality is $\Theta_{x^{\dagger}} = \Theta_x$. The map $x\mapsto\Theta_x$ is even in the parameter, $\Theta_{-x} = L_{-x}R_{(-x)^{\dagger}} = L_xR_{x^{\dagger}} = \Theta_x$, so both $x^{\dagger} = x$ and $x^{\dagger} = -x$ give self-adjointness; the map is not injective, and self-adjointness of the operator therefore does not force $x = x^{\dagger}$.

## Unitarity and the Modular Conjugation

**Theorem (the unitarity criterion).** For every $x$ the following are equivalent: (1) $\Theta^{\alpha}_x$ is isometric for the form; (2) $(\Theta^{\alpha}_x)^{*}\Theta^{\alpha}_x = \mathrm{id}$; (3) $\Theta_{x^{\dagger}x} = \mathrm{id}$, which holds in particular when $x^{\dagger}x = 1$; and $\Theta^{\alpha}_x$ is unitary exactly when $x^{\dagger}x = xx^{\dagger} = 1$. The sign does not appear in the criterion.

**Proof.** $(\Theta^{\alpha}_x)^{*}\Theta^{\alpha}_x = \Theta_{x^{\dagger}x}$ by the adjoint-product proposition, and $\Theta_{x^{\dagger}x} = \mathrm{id}$ is the stated form of the criterion, implied by $x^{\dagger}x = 1$; the unitary statement adds the other side.

**Proposition (invariance under the modular conjugation).** The signed sandwich is invariant under the modular conjugation of the standard form,

$$
\jmath\,\bar\Theta^{\alpha}_x\,\jmath = \bar\Theta^{\alpha}_x ,
$$

because the sign is a real scalar and the modular conjugation is antilinear with $\jmath^{2} = \mathrm{id}$.

**Proof.** $\jmath\bar\Theta^{\alpha}_x\jmath = \varepsilon_x\,\jmath\bar\Theta_x\jmath = \varepsilon_x\bar\Theta_x = \bar\Theta^{\alpha}_x$, using the invariance of the unsigned sandwich of *The Adjoint of the Sandwich on a Hilbert Algebra*.

**Proposition (the modular flow on the signed family).** The modular automorphism $\sigma_t(x) = \Delta^{it}x\Delta^{-it}$ acts by

$$
\Delta^{it}\,\bar\Theta^{\alpha}_x\,\Delta^{-it} = \bar\Theta^{\alpha}_{\sigma_t(x)} ,
$$

and it preserves the parity, $\varepsilon_{\sigma_t(x)} = \varepsilon_x$, so it preserves the sign; the modular flow therefore acts on the family of signed sandwiches through its action on the parameters and commutes with the sign bookkeeping.

**Proof.** The modular group conjugates a sandwich into the sandwich of the conjugated parameter by *The Modular Operator and Tomita-Takesaki Theory*; the invariance of the parity is the even-ness of the modular automorphism for a graded Hilbert algebra, from *The Grading of a Hilbert Algebra with Signed Hermitian Adjoint*.

**Remark (the sign and the modular structure).** The sign is a real scalar attached to the parameter and preserved by the involution, by the modular conjugation and by the modular flow; so the signed sandwich is as modular as the unsigned one. What the sign changes is the value at the unit, $\Theta^{\alpha}_x(1) = \varepsilon_xxx^{\dagger}$, and the composition table; what it leaves alone is the adjoint operation, the operator products and the invariance under the modular objects.

## Worked Cases

### Odd and Even Parameters

In a graded Hilbert algebra let $u$ be an odd element with $u^{\dagger} = -u$, for instance $u = i\sigma_x$ with the grading $\alpha(a) = \gamma a\gamma$, $\gamma = \mathrm{diag}(1,-1)$, in $M_2(\mathbb{C})$. Then $\Theta^{\alpha}_u = -\Theta_u$ and $(\Theta^{\alpha}_u)^{*} = \Theta^{\alpha}_{u^{\dagger}} = \Theta^{\alpha}_{-u} = -\Theta_{-u} = -\Theta_u = \Theta^{\alpha}_u$, so the signed sandwich is self-adjoint although $u\neq u^{\dagger}$; the unsigned sandwich of the same element is self-adjoint too, $\Theta_u^{*} = \Theta_{u^{\dagger}} = \Theta_{-u} = \Theta_u$. This is the smallest case where self-adjointness fails to force the parameter to be self-adjoint. The involution preserves the parity, so the sign survives in both.

### A Group Algebra with Trivial Grading

If the involution and the parity are both trivial, $\alpha = \mathrm{id}$, then $\Theta^{\alpha}_x = \Theta_x$ and the article reduces to the unsigned case: the adjoint is the sandwich of the involution, the criteria are those of *The Adjoint of the Sandwich on a Hilbert Algebra*, and the sign does nothing.

### An Even Unitary Parameter

For an even unitary $x$, $\Theta^{\alpha}_x = \Theta_x = \mathrm{Ad}_x$ is an isometry and in fact unitary, and the adjoint is $\Theta_{x^{\dagger}} = \Theta_{x^{-1}}$, the inverse inner automorphism; the sign is $+1$ and the adjunction behaves as in the unsigned theory.

## Summary

The **signed Hermitian sandwich** is $\Theta^{\alpha}_x = \Lambda^{\alpha}_xR_{x^{\dagger}}$ with $\Lambda^{\alpha}_x(y) = \alpha(x)y$, equal to $\varepsilon_x\Theta_x$ on a homogeneous parameter, and its **adjoint** is

$$
\bigl(\Theta^{\alpha}_x\bigr)^{*} = \Theta^{\alpha}_{x^{\dagger}} ,
$$

the sign being preserved because the involution preserves the parity, $\varepsilon_{x^{\dagger}} = \varepsilon_x$. Its adjoint products are $\Theta_{x^{\dagger}x}$ and $\Theta_{xx^{\dagger}}$, which are unsigned because $x^{\dagger}x$ and $xx^{\dagger}$ are even, so the **unitarity criterion** is the unsigned one, $(\Theta^{\alpha}_x)^{*}\Theta^{\alpha}_x = \Theta_{x^{\dagger}x} = \mathrm{id}$ (in particular $x^{\dagger}x = 1$), and **self-adjointness** is $\Theta_{x^{\dagger}} = \Theta_x$, which holds for $x^{\dagger} = \pm x$. The **sign rule** of the composition is unchanged by adjunction, since adjunction multiplies both the operator and its adjoint by the same scalar, and the composite of two odd signed sandwiches is an ordinary sandwich. The **modular conjugation** leaves the signed sandwich invariant, $\jmath\bar\Theta^{\alpha}_x\jmath = \bar\Theta^{\alpha}_x$, and the **modular flow** acts by $\Delta^{it}\bar\Theta^{\alpha}_x\Delta^{-it} = \bar\Theta^{\alpha}_{\sigma_t(x)}$ with the parity and the sign preserved; so the sign lives in the parameter, in the value at the unit and in the composition table, and nowhere in the adjoint operation. The grading and the signed multiplications are *The Grading of a Hilbert Algebra with Signed Hermitian Adjoint* and *One-Sided Operators on a Hilbert Algebra with Signed Hermitian Adjoint*, the unsigned adjoint is *The Adjoint of the Sandwich on a Hilbert Algebra*, and the modular objects are *The Modular Operator and Tomita-Takesaki Theory*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Theta^{\alpha}_x = \Lambda^{\alpha}_xR_{x^{\dagger}}$ | Signed Hermitian sandwich |
| $\Theta^{\alpha}_x = \varepsilon_x\Theta_x$ | Parity sign, $\varepsilon_x = (-1)^{|x|}$ |
| $(\Theta^{\alpha}_x)^{*} = \Theta^{\alpha}_{x^{\dagger}}$ | The adjoint |
| $\varepsilon_{x^{\dagger}} = \varepsilon_x$ | Adjunction preserves the sign |
| $(\Theta^{\alpha}_x)^{*}\Theta^{\alpha}_x = \Theta_{x^{\dagger}x}$ | Adjoint product, unsigned |
| $x^{\dagger}x = xx^{\dagger} = 1$ | Unitarity criterion |
| $\jmath\bar\Theta^{\alpha}_x\jmath = \bar\Theta^{\alpha}_x$ | Invariance under the modular conjugation |
| $\Delta^{it}\bar\Theta^{\alpha}_x\Delta^{-it} = \bar\Theta^{\alpha}_{\sigma_t(x)}$ | Modular flow on the family |

## Further Reading

- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for two-sided operators on a Hilbert algebra and their adjoints.
- Serban Stratila and László Zsidó, *Lectures on von Neumann Algebras* (Abacus Press, 1979), for the sandwich operators and the modular conjugation.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the modular flow on the algebra of operators.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the grading and the grade involution of a Clifford algebra.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 2 (Academic Press, 1986), for the adjoint of a two-sided action and the modular structure.
