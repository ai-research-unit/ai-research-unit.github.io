# __Adjoints of the Signed Action of a Hermitian Algebra__

## Introduction

The signed action of a graded Hermitian algebra on itself is the pair of one-sided operators $\Lambda^{\alpha}_x(y) = \alpha(x)y$ and $\mathrm{P}^{\alpha}_x(y) = y\alpha(x)$, the signed left action and the signed right action, which on a homogeneous parameter are the scalar multiples $\Lambda^{\alpha}_x = \varepsilon_xL_x$ and $\mathrm{P}^{\alpha}_x = \varepsilon_xR_x$. This article computes their adjoints and follows the sign through the computation, together with the way the modular operator and the modular conjugation act on them.

The result has three parts. First, both signed actions are $\ast$-representations with respect to the involution: $(\Lambda^{\alpha}_x)^{*} = \Lambda^{\alpha}_{x^{\dagger}}$ and $(\mathrm{P}^{\alpha}_x)^{*} = \mathrm{P}^{\alpha}_{x^{\dagger}}$, the sign being preserved because the involution does not change the parity. Second, the Tomita operator conjugates each signed action into the signed action of the involution on the other side, $S\Lambda^{\alpha}_xS = \mathrm{P}^{\alpha}_{x^{\dagger}}$ and $S\mathrm{P}^{\alpha}_xS = \Lambda^{\alpha}_{x^{\dagger}}$, so the adjoint of a signed action is the signed action of the involution and the adjoint of a signed right action is the signed left action; the same identities hold with the modular conjugation in place of $S$, $\jmath\Lambda^{\alpha}_x\jmath = \mathrm{P}^{\alpha}_{x^{\dagger}}$. Third, the modular flow carries the signed action into the signed action of the modular image of the parameter, $\Delta^{it}\Lambda^{\alpha}_x\Delta^{-it} = \Lambda^{\alpha}_{\sigma_t(x)}$, and it commutes with adjunction, so the sign rule is modular-invariant.

This article fixes the adjoints of the signed left and right actions, the sign rule of adjunction, the conjugation identities for the Tomita operator and the modular conjugation, and the self-adjointness, skew-adjointness and unitarity criteria.

The sign, the parity and the signed one-sided operators are *The Grading of a Hermitian Algebra with Signed Hermitian Adjoint*, *The Graded Multiplication Operators* and *One-Sided Operators on a Hermitian Algebra with Signed Hermitian Adjoint*; the adjoints of the unsigned multiplications are *The Adjoint of the Left and the Right Multiplication* and *The Adjoint of the Left Multiplication on a Hermitian Algebra*; the graded adjoint operation is *Adjoints of the Graded Operators of a Hermitian Algebra*; the modular objects are *The Modular Operator and Tomita-Takesaki Theory*; the positivity is *Self-Adjoint Elements and the Positive Cone*. Those are cited. The algebra is $A$ with involution $\dagger$, form $\langle\cdot,\cdot\rangle$, grade involution $\alpha$ and parity $|x|$, with $\varepsilon_x = (-1)^{|x|}$; the completion is $H$ and the Tomita operator is $S = \jmath\Delta^{1/2}$.

## The Signed Action and Its Adjoints

**Definition.** The **signed left action** and the **signed right action** of $A$ on itself are

$$
\Lambda^{\alpha}_x(y) = \alpha(x)\,y , \qquad \mathrm{P}^{\alpha}_x(y) = y\,\alpha(x) ,
$$

so that $\Lambda^{\alpha}_x = \varepsilon_xL_x$ and $\mathrm{P}^{\alpha}_x = \varepsilon_xR_x$ for homogeneous $x$.

**Theorem (the adjoints).** For every $x$,

$$
\bigl(\Lambda^{\alpha}_x\bigr)^{*} = \Lambda^{\alpha}_{x^{\dagger}} , \qquad \bigl(\mathrm{P}^{\alpha}_x\bigr)^{*} = \mathrm{P}^{\alpha}_{x^{\dagger}} ,
$$

the adjoints being taken for the form; so the signed actions are $\ast$-representations with the involution of the algebra.

**Proof.** $\Lambda^{\alpha}_x = \varepsilon_xL_x$ for homogeneous $x$ and $L_x^{*} = L_{x^{\dagger}}$ by *The Adjoint of the Left and the Right Multiplication*, so $(\Lambda^{\alpha}_x)^{*} = \varepsilon_xL_{x^{\dagger}} = \Lambda^{\alpha}_{x^{\dagger}}$ since $\varepsilon_{x^{\dagger}} = \varepsilon_x$; for a general $x$ both sides are the sum of their homogeneous parts. The right-handed computation is the same with $R_x^{*} = R_{x^{\dagger}}$.

**Proposition (composition laws).** For all $x, z$,

$$
\Lambda^{\alpha}_{xz} = \Lambda^{\alpha}_x\Lambda^{\alpha}_z , \qquad \mathrm{P}^{\alpha}_{xz} = \mathrm{P}^{\alpha}_z\mathrm{P}^{\alpha}_x ,
$$

the signed left action composing in the written order and the signed right action anti-composing, exactly like the unsigned families.

**Proof.** $\alpha(xz) = \alpha(x)\alpha(z)$ with associativity for the left family; $\alpha(xz) = \alpha(x)\alpha(z)$ read from the right for the right family.

**Proposition (the adjoint of a composite).** For every $x, z$ and every bounded operator $T$,

$$
\bigl(\Lambda^{\alpha}_x\,T\,\Lambda^{\alpha}_z\bigr)^{*} = \Lambda^{\alpha}_{z^{\dagger}}\,T^{*}\,\Lambda^{\alpha}_{x^{\dagger}} , \qquad \bigl(\mathrm{P}^{\alpha}_x\,T\,\mathrm{P}^{\alpha}_z\bigr)^{*} = \mathrm{P}^{\alpha}_{z^{\dagger}}\,T^{*}\,\mathrm{P}^{\alpha}_{x^{\dagger}} ,
$$

so adjunction reverses the order of a composite of signed actions and carries each factor to the factor of the involution.

**Proof.** The ordinary rule $(ST)^{*} = T^{*}S^{*}$ applied twice, with the theorem.

## The Sign Rule

**Proposition (adjunction preserves the sign).** For homogeneous $x$,

$$
\bigl(\Lambda^{\alpha}_x\bigr)^{*} = \varepsilon_x\,L_{x^{\dagger}} = \varepsilon_x\,\bigl(L_x\bigr)^{*} , \qquad \bigl(\mathrm{P}^{\alpha}_x\bigr)^{*} = \varepsilon_x\,\bigl(R_x\bigr)^{*} ,
$$

so the adjoint of a signed action is the sign times the adjoint of the ordinary action, with the *same* sign $\varepsilon_x$; equivalently the sign is taken out of and put into the adjoint operation without change.

**Proof.** The theorem and $\Lambda^{\alpha}_x = \varepsilon_xL_x$ with $L_x^{*} = L_{x^{\dagger}}$.

**Theorem (the graded commutator under adjunction).** For graded operators $S,T$ the adjoint reverses the graded commutator with the Koszul sign, $[S,T\}^{*} = -(-1)^{|S||T|}[S^{*},T^{*}\}$; in particular, for homogeneous $x,z$,

$$
\bigl[\Lambda^{\alpha}_x,\ \mathrm{P}^{\alpha}_z\bigr\}^{*} = -(-1)^{|x||z|}\,\bigl[\Lambda^{\alpha}_{x^{\dagger}},\ \mathrm{P}^{\alpha}_{z^{\dagger}}\bigr\} ,
$$

so the graded commutator of the two signed actions is adjoint to the graded commutator of the two signed actions of the involution.

**Proof.** The general rule is *Adjoints of the Graded Operators of a Hermitian Algebra*; substituting the theorem for the two adjoints gives the display.

**Corollary (the sign rule is compatible with adjunction).** If two signed actions graded-commute then their adjoints graded-commute; the vanishing of a graded commutator of the signed families is therefore stable under adjunction, and the Koszul sign is unaffected by the parity sign of either family.

**Proof.** The theorem with $\Lambda^{\alpha}_x$ and $\mathrm{P}^{\alpha}_z$ in place of $S,T$; the signs $\varepsilon_x, \varepsilon_z$ are real scalars and do not enter the bracket's sign, which is $(-1)^{|x||z|}$.

**Remark (why the sign is invisible here).** On the one-sided signed action the sign is a scalar on each homogeneous part, and every structural property — kernel, image, adjointness class, graded commutation — is therefore shared with the ordinary action. The sign becomes visible only when the left and the right factors are paired, that is in the two-sided operators of *Two-Sided Operators on a Hermitian Algebra with Signed Hermitian Adjoint* and in their adjoints of *The Signed Adjoint of the Sandwich on a Hermitian Algebra*.

## The Modular Operator and the Sign Rule

**Theorem (the conjugation by the Tomita operator).** On the dense subspace $A\xi$,

$$
S\,\Lambda^{\alpha}_x\,S = \mathrm{P}^{\alpha}_{x^{\dagger}} , \qquad S\,\mathrm{P}^{\alpha}_x\,S = \Lambda^{\alpha}_{x^{\dagger}} ,
$$

so the Tomita operator exchanges the signed actions and turns each into the signed action of the involution on the other side.

**Proof.** $S\Lambda^{\alpha}_xS(y\xi) = S\Lambda^{\alpha}_x(y^{\dagger}\xi) = S(\alpha(x)y^{\dagger}\xi) = (\alpha(x)y^{\dagger})^{\dagger}\xi = y\alpha(x)^{\dagger}\xi = y\alpha(x^{\dagger})\xi = \mathrm{P}^{\alpha}_{x^{\dagger}}(y\xi)$; the second identity is the same computation with the roles of the two sides exchanged.

**Corollary (the adjoint as a conjugation of the other side).** Combining with the theorem on adjoints,

$$
\bigl(\Lambda^{\alpha}_x\bigr)^{*} = \Lambda^{\alpha}_{x^{\dagger}} = S\,\mathrm{P}^{\alpha}_x\,S ,
$$

so the adjoint of the signed left action is the conjugation of the signed right action by the Tomita operator, exactly as the adjoint is a conjugation of the other side in the unsigned theory.

**Proof.** The second identity of the theorem with $x$ in place of $x^{\dagger}$, and the involution $x^{\dagger\dagger} = x$.

**Theorem (the conjugation by the modular conjugation).** With $\jmath$ the modular conjugation of the standard form,

$$
\jmath\,\Lambda^{\alpha}_x\,\jmath = \mathrm{P}^{\alpha}_{x^{\dagger}} , \qquad \jmath\,\mathrm{P}^{\alpha}_x\,\jmath = \Lambda^{\alpha}_{x^{\dagger}} ,
$$

so the modular conjugation exchanges the signed left action with the signed right action of the involution, and the sign is neither gained nor lost in the exchange.

**Proof.** For homogeneous $x$, $\jmath\Lambda^{\alpha}_x\jmath = \varepsilon_x\jmath L_x\jmath = \varepsilon_xR_{x^{\dagger}} = \mathrm{P}^{\alpha}_{x^{\dagger}}$, using $\jmath L_x\jmath = R_{x^{\dagger}}$ of *The Adjoint of the Left and the Right Multiplication* and the definition of the signed right action; the general case follows by linearity, and the second identity is the first with $x$ replaced by $x^{\dagger}$ and applied twice.

**Theorem (the modular flow).** The modular automorphism acts by

$$
\Delta^{it}\,\Lambda^{\alpha}_x\,\Delta^{-it} = \Lambda^{\alpha}_{\sigma_t(x)} , \qquad \sigma_t(x) = \Delta^{it}x\Delta^{-it} ,
$$

and it preserves the parity, $\varepsilon_{\sigma_t(x)} = \varepsilon_x$; moreover the modular flow commutes with adjunction,

$$
\bigl(\Delta^{it}\,\Lambda^{\alpha}_x\,\Delta^{-it}\bigr)^{*} = \Delta^{it}\,\bigl(\Lambda^{\alpha}_x\bigr)^{*}\,\Delta^{-it} ,
$$

so the adjoint operation and the modular flow are interchangeable on the signed family.

**Proof.** The flow acts on the parameter by the modular automorphism of the algebra, by *The Modular Operator and Tomita-Takesaki Theory*; the parity is preserved because the modular automorphism is even, by *The Grading of a Hermitian Algebra with Signed Hermitian Adjoint*; the commutation with adjunction is the unitarity of $\Delta^{it}$ together with the ordinary rule $(UTU^{*})^{*} = UT^{*}U^{*}$ for unitary $U$.

**Remark (the two roles of the modular operator).** The modular operator enters in two distinct ways. Through the adjoint it enters not at all: the adjoint of a signed action is a signed action, because the actions are bounded and defined on the algebra. Through the conjugation it enters completely: the exchange of the two sides is implemented by $S$ and by $\jmath$, and the group $\Delta^{it}$ moves the parameter by the modular automorphism. So the adjoint operation on the signed action is algebraic, and the modular operator is what turns it into the exchange of sides, which is the same division of labour as in the unsigned theory.

## Self-Adjointness, Skew-Adjointness and Unitarity

**Theorem (the criteria).** For $x\in A$:

1. $\Lambda^{\alpha}_x$ is self-adjoint exactly when $x = x^{\dagger}$;
2. it is skew-adjoint exactly when $x^{\dagger} = -x$;
3. it is normal exactly when $xx^{\dagger} = x^{\dagger}x$;
4. it is unitary exactly when $x^{\dagger}x = xx^{\dagger} = 1$;
5. for self-adjoint $x$, it is positive exactly when $x$ lies in the positive cone.

**Proof.** By the theorem on adjoints, $(\Lambda^{\alpha}_x)^{*} = \Lambda^{\alpha}_{x^{\dagger}}$, so self-adjointness is $x = x^{\dagger}$ and skew-adjointness is $x^{\dagger} = -x$ with the left representation faithful; normality compares $(\Lambda^{\alpha}_x)^{*}\Lambda^{\alpha}_x = \Lambda^{\alpha}_{x^{\dagger}x} = \Lambda_{x^{\dagger}x}$ with $\Lambda^{\alpha}_x(\Lambda^{\alpha}_x)^{*} = \Lambda^{\alpha}_{xx^{\dagger}} = \Lambda_{xx^{\dagger}}$, the equalities to the unsigned family holding because $x^{\dagger}x$ and $xx^{\dagger}$ are even; unitarity adds the value $\mathrm{id}$; positivity is $\langle\Lambda^{\alpha}_xy,y\rangle = \langle xy,y\rangle$ for self-adjoint $x$ in the cone.

**Corollary (the criteria are unsigned).** The self-adjoint, skew-adjoint, normal, unitary and positive signed actions are exactly those of the ordinary action; the sign rescales the operator on an odd parameter, $\Lambda^{\alpha}_u = -L_u$, and changes no criterion.

**Proof.** The criteria of the theorem involve only the involution and the even products $x^{\dagger}x$, $xx^{\dagger}$; on an odd parameter $\Lambda^{\alpha}_u = -L_u$, a real rescaling, which preserves self-adjointness, skew-adjointness, normality and unitarity, and reverses positivity.

**Remark (the value at the unit).** The signed left action at the unit is $\Lambda^{\alpha}_x(1) = \alpha(x)$, equal to $x$ on the even part and to $-x$ on the odd part; this is the simplest place where the sign is visible, and it is the one-sided statement of the value $\Theta^{\alpha}_x(1) = \varepsilon_xxx^{\dagger}$ of the two-sided operator.

## Worked Cases

### A Matrix Algebra with a Grading

Let $A = M_2(\mathbb{C})$ with the form $\langle a,b\rangle = \mathrm{tr}(b^{*}a)$, the involution $a^{\dagger} = a^{*}$ and the grading $\alpha(a) = \gamma a\gamma$ with $\gamma = \mathrm{diag}(1,-1)$. For an odd $a$ the signed left action is $-L_a$, its adjoint is $\Lambda^{\alpha}_{a^{\dagger}} = -L_{a^{*}}$, and the Tomita operator is $S(b\xi) = b^{*}\xi$ with $\jmath(b\xi) = b^{*}\xi$, so that $\jmath\Lambda^{\alpha}_a\jmath = \mathrm{P}^{\alpha}_{a^{\dagger}}$ reduces to the conjugation of the left multiplication into the right multiplication by $a^{*}$.

### The Group Algebra

For $A = \mathbb{C}[G]$ with the trivially graded structure, $\Lambda^{\alpha}_g = L_g$ and the adjoint is $L_{g^{-1}} = \Lambda^{\alpha}_{g^{\dagger}}$; the signed action coincides with the ordinary one and the sign rule is empty.

### An Odd Anti-Self-Adjoint Element

Let $u$ be odd with $u^{\dagger} = -u$. Then $\Lambda^{\alpha}_u = -L_u$, its adjoint is $\Lambda^{\alpha}_{-u} = -\Lambda^{\alpha}_u$, so the signed left action is skew-adjoint, and so is the ordinary left action; the two differ by the real sign $-1$, which changes neither the adjointness class nor the norm but reverses the value at the unit.

## Summary

The **signed left and right actions** are $\Lambda^{\alpha}_x(y) = \alpha(x)y$ and $\mathrm{P}^{\alpha}_x(y) = y\alpha(x)$, equal to $\varepsilon_xL_x$ and $\varepsilon_xR_x$ on homogeneous parameters, and their **adjoints** are

$$
\bigl(\Lambda^{\alpha}_x\bigr)^{*} = \Lambda^{\alpha}_{x^{\dagger}} , \qquad \bigl(\mathrm{P}^{\alpha}_x\bigr)^{*} = \mathrm{P}^{\alpha}_{x^{\dagger}} ,
$$

the sign being preserved because the involution does not change the parity, $\varepsilon_{x^{\dagger}} = \varepsilon_x$; so the adjoint of a signed action is the same sign times the adjoint of the ordinary action, and the graded commutator satisfies the Koszul rule $[S,T\}^{*} = -(-1)^{|S||T|}[S^{*},T^{*}\}$. The **Tomita operator** conjugates each signed action into the signed action of the involution on the other side, $S\Lambda^{\alpha}_xS = \mathrm{P}^{\alpha}_{x^{\dagger}}$ and $S\mathrm{P}^{\alpha}_xS = \Lambda^{\alpha}_{x^{\dagger}}$, whence $(\Lambda^{\alpha}_x)^{*} = S\mathrm{P}^{\alpha}_xS$; the **modular conjugation** does the same, $\jmath\Lambda^{\alpha}_x\jmath = \mathrm{P}^{\alpha}_{x^{\dagger}}$; and the **modular flow** acts by $\Delta^{it}\Lambda^{\alpha}_x\Delta^{-it} = \Lambda^{\alpha}_{\sigma_t(x)}$ with the parity and the adjoint operation preserved. The **criteria** are unsigned: self-adjoint exactly when $x = x^{\dagger}$, skew-adjoint exactly when $x^{\dagger} = -x$, normal exactly when $xx^{\dagger} = x^{\dagger}x$, unitary exactly when $x^{\dagger}x = xx^{\dagger} = 1$, and positive for self-adjoint $x$ in the positive cone; the sign is visible in the value at the unit, $\Lambda^{\alpha}_x(1) = \alpha(x)$, and nowhere in the adjoint operation. The sign and the signed one-sided operators are *The Grading of a Hermitian Algebra with Signed Hermitian Adjoint* and *One-Sided Operators on a Hermitian Algebra with Signed Hermitian Adjoint*, the graded adjoint rule is *Adjoints of the Graded Operators of a Hermitian Algebra*, the Two-sided adjoint is *The Signed Adjoint of the Sandwich on a Hermitian Algebra*, and the modular objects are *The Modular Operator and Tomita-Takesaki Theory*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Lambda^{\alpha}_x(y) = \alpha(x)y$, $\mathrm{P}^{\alpha}_x(y) = y\alpha(x)$ | Signed left and right actions |
| $\Lambda^{\alpha}_x = \varepsilon_xL_x$, $\mathrm{P}^{\alpha}_x = \varepsilon_xR_x$ | Value on a homogeneous parameter |
| $(\Lambda^{\alpha}_x)^{*} = \Lambda^{\alpha}_{x^{\dagger}}$, $(\mathrm{P}^{\alpha}_x)^{*} = \mathrm{P}^{\alpha}_{x^{\dagger}}$ | The adjoints |
| $\Lambda^{\alpha}_{xz} = \Lambda^{\alpha}_x\Lambda^{\alpha}_z$, $\mathrm{P}^{\alpha}_{xz} = \mathrm{P}^{\alpha}_z\mathrm{P}^{\alpha}_x$ | Composition laws |
| $[S,T\}^{*} = -(-1)^{|S||T|}[S^{*},T^{*}\}$ | Koszul rule, sign preserved |
| $S\Lambda^{\alpha}_xS = \mathrm{P}^{\alpha}_{x^{\dagger}}$, $S\mathrm{P}^{\alpha}_xS = \Lambda^{\alpha}_{x^{\dagger}}$ | Conjugation by the Tomita operator |
| $\jmath\Lambda^{\alpha}_x\jmath = \mathrm{P}^{\alpha}_{x^{\dagger}}$ | Conjugation by the modular conjugation |
| $\Delta^{it}\Lambda^{\alpha}_x\Delta^{-it} = \Lambda^{\alpha}_{\sigma_t(x)}$ | The modular flow |

## Further Reading

- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the regular representation and its adjoint.
- Serban Stratila and László Zsidó, *Lectures on von Neumann Algebras* (Abacus Press, 1979), for the modular conjugation and the exchange of the two sides.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the modular flow on the algebra.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the grade involution and the signed multiplications.
- Pierre Deligne, Pavel Etingof, Daniel S. Freed, Lisa C. Jeffrey, David Kazhdan, John W. Morgan, David R. Morrison and Edward Witten, *Quantum Fields and Strings: A Course for Mathematicians*, vol. 1 (American Mathematical Society, 1999), for the Koszul sign rule in the graded algebra of operators.
