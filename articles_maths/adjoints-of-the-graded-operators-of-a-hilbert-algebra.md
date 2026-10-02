# __Adjoints of the Graded Operators of a Hilbert Algebra__

## Introduction

A Hilbert algebra with a parity grading carries three adjoint-related structures that are easy to confuse: the **involution** $x\mapsto x^{\dagger}$ on the elements, the **Hilbert adjoint** $T\mapsto T^{*}$ on the operators, and the **grade involution** $\alpha$ on both. This article separates them by computing the adjoint of a *graded* operator, that is of an operator whose domain and range are homogeneous for the grading, and by computing the adjoint of a product of two such operators. The adjoint of a graded operator of parity $|T|$ is graded of the same parity, so the adjoint operation preserves the parity bookkeeping; and the graded commutator of two graded operators obeys the Koszul sign rule, which is what distinguishes the plain adjoint from the super-adjoint of the regular representation.

The sign rule has a concrete consequence for the regular representation, and it is the reason this article belongs to the signed group. With the **super-adjoint**

$$
T^{\star} = (-1)^{|T|}T^{*}
$$

one has $(TS)^{\star} = S^{\star}T^{\star}$, and applied to the multiplication operators it gives

$$
L_x^{\star} = \Lambda^{\alpha}_{x^{\dagger}} , \qquad R_x^{\star} = \mathrm{P}^{\alpha}_{x^{\dagger}} , \qquad \Theta_x^{\star} = \Theta^{\alpha}_{x^{\dagger}} ,
$$

so the **super-adjoint of the ordinary family is the signed family**. The signed structure is therefore not a second structure grafted onto the ordinary one: it is the adjoint operation of the graded algebra, that is, the ordinary adjoint corrected by the parity sign. The grading of the Hilbert algebra is the same statement in the multiplicative form $\Theta^{\alpha}_x = \varepsilon_x\Theta_x$.

This article fixes graded operators and the parity of their adjoints, the super-adjoint and its sign rule for products and graded commutators, the super-adjoints of the regular representation, and the compatibility of the graded adjoint with the modular structure.

The grading, the grade involution and the signed multiplications are *The Grading of a Hilbert Algebra with Signed Hermitian Adjoint* and *The Graded Multiplication Operators*; the adjoints of the multiplications are *The Adjoint of the Left and the Right Multiplication*; the signed one-sided and two-sided families are *One-Sided Operators on a Hilbert Algebra with Signed Hermitian Adjoint* and *Two-Sided Operators on a Hilbert Algebra with Signed Hermitian Adjoint*; the modular objects are *The Modular Operator and Tomita-Takesaki Theory*. Those are cited. The algebra is $A$ with involution $\dagger$, form $\langle\cdot,\cdot\rangle$ and grade involution $\alpha$, which commutes with the involution, $\alpha(x^{\dagger}) = \alpha(x)^{\dagger}$; a homogeneous element has parity $|x|$ and sign $\varepsilon_x = (-1)^{|x|}$.

## Graded Operators and the Parity of the Adjoint

**Definition.** A linear operator $T$ on $A$ is **graded**, or homogeneous, of parity $|T|$ when it maps the even part to the part of parity $|T|$ and the odd part to the part of parity $1+|T|$; then $T$ is **even** for $|T| = 0$ and **odd** for $|T| = 1$. The **form** is **even** when the two parity sectors are orthogonal, $\langle x,y\rangle = 0$ for $x$ even and $y$ odd.

**Theorem (the adjoint of a graded operator is graded of the same parity).** Let the form be even and let $T$ be a graded operator of parity $|T|$ with adjoint $T^{*}$. Then $T^{*}$ is graded of parity $|T|$.

**Proof.** For homogeneous $x$ of parity $i$ and $y$ of parity $j$ the identity $\langle Tx,y\rangle = \langle x,T^{*}y\rangle$ can be nonzero only if the two sides pair elements of the same parity: on the left $|Tx| = i+|T|$ must equal $j$, and on the right $|T^{*}y|$ must equal $i$, that is $j+|T^{*}| = i$. Hence $|T^{*}| = |T|$ mod $2$, which for $\mathbb{Z}/2$-valued parity is $|T^{*}| = |T|$.

**Corollary (the adjoint preserves the super-structure).** The adjoint operation maps even operators to even operators and odd operators to odd operators; it therefore acts on the graded algebra of operators as a map of degree zero.

**Proof.** The theorem applied to each parity class.

**Remark (why the even-ness of the form is needed).** Without it the adjoint of an odd operator would mix the two parity sectors into each other's duals and the parity of $T^{*}$ would not be defined; the even-ness of the form is the same hypothesis that makes the two sectors orthogonal on the module and in the pairing, and it is assumed throughout.

## The Super-Adjoint and the Sign Rule

**Definition.** The **super-adjoint** of a graded operator of parity $|T|$ is

$$
T^{\star} = (-1)^{|T|}\,T^{*} .
$$

It is again graded of parity $|T|$, and $T^{\star\star} = T$.

**Proof.** The sign is a real scalar, so the parity is that of $T^{*}$, namely $|T|$; for the involution, $|T^{\star}| = |T|$ and $T^{\star\star} = (-1)^{|T|}\bigl((-1)^{|T|}T^{*}\bigr)^{*} = (-1)^{2|T|}T^{**} = T$.

**Theorem (the super-adjoint is multiplicative).** For graded operators $S, T$,

$$
(TS)^{*} = T^{*}S^{*} , \qquad (TS)^{\star} = S^{\star}T^{\star} ,
$$

so the sign absorbed in the definition of the super-adjoint leaves the multiplicativity free of any extra sign.

**Proof.** The ordinary rule is the definition of the adjoint applied twice. For the super-adjoint, $(TS)^{\star} = (-1)^{|T|+|S|}(TS)^{*} = (-1)^{|T|+|S|}S^{*}T^{*}$ and $S^{\star}T^{\star} = (-1)^{|S|}S^{*}(-1)^{|T|}T^{*} = (-1)^{|S|+|T|}S^{*}T^{*}$; the two agree.

**Corollary (why the sign sits in the operator).** The sign of the super-adjoint is placed on the operator, so that the super-adjoint is plainly multiplicative, $(TS)^{\star} = S^{\star}T^{\star}$. The alternative convention of the super-symmetric literature puts the Koszul sign in the product rule, $(TS)^{\circ} = (-1)^{|S||T|}S^{\circ}T^{\circ}$ with an unsigned adjoint; that convention is consistent only for a pairing carrying the same sign, and with the even form used here it fails already on two odd operators, for which $S^{*}T^{*}\neq -S^{*}T^{*}$. Only the first convention is used, because it is the one under which the signed family of the corpus is an adjoint of the ordinary one.

**Proposition (the graded commutator under the ordinary adjoint).** For graded $S,T$,

$$
[S,T\}^{*} = -\,(-1)^{|S||T|}\,[S^{*},T^{*}\} ,
$$

so the adjoint reverses the graded commutator and picks up the Koszul sign in doing so.

**Proof.** $[S,T\}^{*} = (ST)^{*}-(-1)^{|S||T|}(TS)^{*} = T^{*}S^{*}-(-1)^{|S||T|}S^{*}T^{*}$, while $[S^{*},T^{*}\} = S^{*}T^{*}-(-1)^{|S||T|}T^{*}S^{*}$ with $|S^{*}| = |S|$ and $|T^{*}| = |T|$; multiplying the second by $-(-1)^{|S||T|}$ and using $(-1)^{2|S||T|} = 1$ gives the first.

**Proposition (the super-adjoint of the graded commutator).** For graded $S,T$,

$$
[S,T\}^{\star} = -\,(-1)^{|S||T|}\,[S^{\star},T^{\star}\} .
$$

**Proof.** By the previous proposition $[S,T\}^{*} = -(-1)^{|S||T|}[S^{*},T^{*}\}$, and $[S^{\star},T^{\star}\} = (-1)^{|S|+|T|}[S^{*},T^{*}\}$ because $S^{\star} = (-1)^{|S|}S^{*}$ is a scalar multiple of $S^{*}$; multiplying the first identity by $(-1)^{|S|+|T|}$ and substituting the second gives the display.

**Definition.** A graded operator is **self-adjoint** when $T^{*} = T$ and **super-self-adjoint** when $T^{\star} = T$, that is when $T^{*} = (-1)^{|T|}T$.

**Proposition (the two self-adjointness conditions).** An even operator is self-adjoint exactly when it is super-self-adjoint; an odd operator is self-adjoint exactly when it is anti-super-self-adjoint, $T^{\star} = -T$. So on the odd part the two adjoint operations differ by the global sign.

**Proof.** For $|T| = 0$ the two statements coincide; for $|T| = 1$, $T^{\star} = -T^{*}$ and the two conditions are opposite.

## The Super-Adjoint of the Regular Representation

**Theorem (the super-adjoint of the multiplications).** For every $x$,

$$
L_x^{\star} = \Lambda^{\alpha}_{x^{\dagger}} , \qquad R_x^{\star} = \mathrm{P}^{\alpha}_{x^{\dagger}} , \qquad \Theta_x^{\star} = \Theta^{\alpha}_{x^{\dagger}} ,
$$

where $\Lambda^{\alpha}$ and $\mathrm{P}^{\alpha}$ are the signed left and right multiplications and $\Theta^{\alpha}$ the signed Hermitian sandwich.

**Proof.** The left multiplication has parity $|x|$ and adjoint $L_x^{*} = L_{x^{\dagger}}$, so $L_x^{\star} = (-1)^{|x|}L_{x^{\dagger}} = \varepsilon_xL_{x^{\dagger}} = \Lambda^{\alpha}_{x^{\dagger}}$, using $\varepsilon_{x^{\dagger}} = \varepsilon_x$ and the definition $\Lambda^{\alpha}_z = \varepsilon_zL_z$; the right-handed identity is the same computation with $R_{x^{\dagger}}$ and $\mathrm{P}^{\alpha}_z = \varepsilon_zR_z$; for the sandwich, $\Theta_x$ has parity $|x|$ and adjoint $\Theta_{x^{\dagger}}$, so $\Theta_x^{\star} = \varepsilon_x\Theta_{x^{\dagger}} = \Theta^{\alpha}_{x^{\dagger}}$.

**Corollary (the signed family is the graded adjoint of the ordinary one).** The signed left multiplication, the signed right multiplication and the signed Hermitian sandwich are the super-adjoints of the ordinary left multiplication, right multiplication and sandwich; so the signed structure of the corpus is exactly the adjoint operation of the graded algebra.

**Proof.** The theorem, read with $x^{\dagger}$ in place of $x$ and the involution involutive: $\Lambda^{\alpha}_x = (L_{x^{\dagger}})^{\star}$, $\mathrm{P}^{\alpha}_x = (R_{x^{\dagger}})^{\star}$, $\Theta^{\alpha}_x = (\Theta_{x^{\dagger}})^{\star}$.

**Corollary (the ordinary adjoint of the signed family).** Applying the ordinary adjoint to the theorem gives $(\Lambda^{\alpha}_x)^{*} = \Lambda^{\alpha}_{x^{\dagger}}$ and $(\mathrm{P}^{\alpha}_x)^{*} = \mathrm{P}^{\alpha}_{x^{\dagger}}$ and $(\Theta^{\alpha}_x)^{*} = \Theta^{\alpha}_{x^{\dagger}}$, in agreement with *One-Sided Operators on a Hilbert Algebra with Signed Hermitian Adjoint* and *The Signed Adjoint of the Sandwich on a Hilbert Algebra*; so the signed family is stable under both adjoint operations.

**Proof.** $(\Lambda^{\alpha}_x)^{*} = \varepsilon_xL_x^{*} = \varepsilon_xL_{x^{\dagger}} = \Lambda^{\alpha}_{x^{\dagger}}$; the other identities are the same computation with the right multiplication and with the sandwich.

**Remark (one adjoint, three names).** The involution on the elements, the adjoint on the operators and the grade involution on the graded algebra are bound together by the theorem: the adjoint corrected by the parity sign of an operator is the same operation as the adjoint corrected by the parity sign of the element, and the signed family is where the two corrections are the same correction. This is the operator form of the statement of *The Grading of a Hilbert Algebra with Signed Hermitian Adjoint* that the signed member is not a second structure.

## Compatibility with the Grading and the Modular Structure

**Proposition (the modular objects are even).** The modular conjugation $\jmath$ and the modular group $\Delta^{it}$ preserve the parity grading, so they are even operators, and the modular flow preserves the sign of an element, $\varepsilon_{\sigma_t(x)} = \varepsilon_x$.

**Proof.** The form is even, hence the standard form is graded, and the modular objects are determined by the form and the involution, both of which are compatible with the grading; the conjugation and the flow therefore map each parity sector into itself, which is the even-ness.

**Theorem (the modular adjoint is the graded adjoint).** Write $T^{\sharp} = \jmath T^{*}\jmath$ for the modular adjoint on the completion. Then

$$
(T^{\sharp})^{\star} = (T^{\star})^{\sharp} , \qquad \Delta^{it}\,T^{\star}\,\Delta^{-it} = \bigl(\Delta^{it}T\Delta^{-it}\bigr)^{\star} ,
$$

so the super-adjoint commutes with the modular adjoint and with the modular flow; in other words the sign rule of adjunction is modular-invariant.

**Proof.** $\jmath$ and $\Delta^{it}$ are even, so they commute with the scalar $(-1)^{|T|}$; for the second identity the parity of $\Delta^{it}T\Delta^{-it}$ is that of $T$, since $\Delta^{it}$ is even, and the adjoint of the conjugate is the conjugate of the adjoint.

**Corollary (the signed family is invariant under the modular objects).** For every $x$,

$$
\jmath\,\Lambda^{\alpha}_x\,\jmath = \mathrm{P}^{\alpha}_{x^{\dagger}} , \qquad \Delta^{it}\,\Lambda^{\alpha}_x\,\Delta^{-it} = \Lambda^{\alpha}_{\sigma_t(x)} ,
$$

so the signed action is exchanged with the signed right action by the modular conjugation and carried into itself by the modular flow.

**Proof.** Apply the modular statements for the ordinary left multiplication, $L_x^{\star} = \Lambda^{\alpha}_{x^{\dagger}}$ and the parity-invariance of the modular objects.

**Remark (what the grading adds and what it does not).** The grading adds the sign in the adjoint of a product and the identification of the signed family with the super-adjoint of the ordinary one; it adds nothing to the *operator* content, since the adjoint of an operator, the involution and the form are unchanged. This is the same observation as before, now from the side of the adjoint instead of the side of the multiplication: the sign is bookkeeping, and the bookkeeping is exact.

## Worked Cases

### A Vector in a Three-Dimensional Algebra

In $\mathrm{Cl}_{0,3}$ with the trivial coefficient involution, let $x = e_1$. Then $|x| = 1$, $x^{\dagger} = -x$, the ordinary adjoint is $L_{e_1}^{*} = L_{-e_1} = -L_{e_1}$, and the super-adjoint is $L_{e_1}^{\star} = -L_{e_1}^{*} = L_{e_1}$. So the odd left multiplication is skew-adjoint in the ordinary sense and super-self-adjoint in the graded sense, and the two adjoints differ by the sign of the odd part.

### An Even Element

For $x = e_1e_2$ one has $|x| = 0$, so $L_x^{\star} = L_x^{*} = L_{x^{\dagger}}$: on the even part the two adjoints agree, the signed multiplication is the ordinary one, and the sign rule is invisible.

### Matrices

For $A = M_n(\mathbb{C})$ with the grading $\alpha(a) = \gamma a\gamma$ of $\mathbb{C}^{n}$, take an odd self-adjoint matrix $m$, $\alpha(m) = -m = m^{\dagger}$, for instance $\sigma_x$ with $\gamma = \mathrm{diag}(1,-1)$ in $M_2(\mathbb{C})$. The operator $T = L_m$, $T(a) = ma$, is odd, its ordinary adjoint is $T^{*} = L_{m^{\dagger}} = L_m = T$, so it is self-adjoint, and its super-adjoint is $T^{\star} = -\,T^{*} = -T$; thus an odd operator that is self-adjoint is anti-super-self-adjoint, which is the parity-$1$ case of the rule $T^{\star} = -T$ for $T^{*} = T$.

## Summary

On a graded Hilbert algebra with an even form, the **adjoint of a graded operator** is graded of the same parity, so the adjoint operation is of degree zero; and for a product the rules are

$$
(TS)^{*} = T^{*}S^{*} , \qquad (TS)^{\star} = S^{\star}T^{\star} , \qquad T^{\star} = (-1)^{|T|}T^{*} ,
$$

with the **super-adjoint** $T^{\star}$ satisfying $T^{\star\star} = T$; the adjoint reverses the graded commutator with the Koszul sign, $[S,T\}^{*} = -(-1)^{|S||T|}[S^{*},T^{*}\}$, and the super-adjoint reverses it with the same Koszul sign, $[S,T\}^{\star} = -(-1)^{|S||T|}[S^{\star},T^{\star}\}$. On the regular representation the super-adjoint is the signed family of the corpus,

$$
L_x^{\star} = \Lambda^{\alpha}_{x^{\dagger}} , \qquad R_x^{\star} = \mathrm{P}^{\alpha}_{x^{\dagger}} , \qquad \Theta_x^{\star} = \Theta^{\alpha}_{x^{\dagger}} ,
$$

so the **signed left multiplication, signed right multiplication and signed Hermitian sandwich are exactly the super-adjoints of the ordinary ones**: the signed structure is the adjoint operation of the graded algebra, not a second structure. **Self-adjointness** and **super-self-adjointness** coincide on the even part and differ by the global sign on the odd part. The **modular objects** are even, the modular adjoint $T^{\sharp} = \jmath T^{*}\jmath$ commutes with the super-adjoint, the modular flow carries the super-adjoint into itself, and the signed action satisfies $\jmath\Lambda^{\alpha}_x\jmath = \mathrm{P}^{\alpha}_{x^{\dagger}}$ and $\Delta^{it}\Lambda^{\alpha}_x\Delta^{-it} = \Lambda^{\alpha}_{\sigma_t(x)}$. The grading is *The Grading of a Hilbert Algebra with Signed Hermitian Adjoint*, the signed multiplications are *The Graded Multiplication Operators* and *One-Sided Operators on a Hilbert Algebra with Signed Hermitian Adjoint*, and the modular objects are *The Modular Operator and Tomita-Takesaki Theory*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $|T|$, $\varepsilon_x = (-1)^{|x|}$ | Parity of an operator, sign of a homogeneous element |
| $\langle x,y\rangle = 0$, $x$ even, $y$ odd | Even-ness of the form, orthogonality of the sectors |
| $T^{*}$, $T^{\star} = (-1)^{|T|}T^{*}$ | Hilbert adjoint, super-adjoint |
| $(TS)^{\star} = S^{\star}T^{\star}$ | Multiplicativity of the super-adjoint |
| $[S,T\}^{*} = -(-1)^{|S||T|}[S^{*},T^{*}\}$ | Graded commutator under the adjoint |
| $[S,T\}^{\star} = -(-1)^{|S||T|}[S^{\star},T^{\star}\}$ | Graded commutator under the super-adjoint |
| $T^{\star} = T$ | Super-self-adjointness |
| $L_x^{\star} = \Lambda^{\alpha}_{x^{\dagger}}$, $R_x^{\star} = \mathrm{P}^{\alpha}_{x^{\dagger}}$, $\Theta_x^{\star} = \Theta^{\alpha}_{x^{\dagger}}$ | Super-adjoint of the regular representation |
| $\jmath$, $\Delta^{it}$ even; $(T^{\sharp})^{\star} = (T^{\star})^{\sharp}$ | Modular compatibility |

## Further Reading

- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the grading and the adjoint on a graded algebra.
- Pierre Deligne, Pavel Etingof, Daniel S. Freed, Lisa C. Jeffrey, David Kazhdan, John W. Morgan, David R. Morrison and Edward Witten, *Quantum Fields and Strings: A Course for Mathematicians*, vol. 1 (American Mathematical Society, 1999), for the Koszul sign rule and the super-adjoint.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the adjoint of a densely defined operator and the adjoint of a product.
- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the adjoints of the regular representation.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the modular objects of a graded Hilbert algebra.
