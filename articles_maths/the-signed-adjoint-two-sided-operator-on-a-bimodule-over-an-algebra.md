
# __The Signed Adjoint Two-Sided Operator on a Bimodule over an Algebra__

## Introduction

The signed two-sided operator $\mathcal{T}^{\alpha}_{a,b}(x)=a\,\alpha(x)\,b$ twists the two-sided action by the grade involution $\alpha$. When the bimodule carries also an involution $\sigma$ and a pairing compatible with both, the adjoint of a signed two-sided operator can be computed, and the answer is a signed two-sided operator again, with parameters transformed by the composite $\alpha\sigma$. The article proves the formula, derives the unitarity condition $u^{*}u=uu^{*}=1$ it defines, and shows that the adjoint respects the $\mathbb{Z}/2$-grading of the two-sided monoid.

The article is the fourth of the `* Operator Theory` group of this category. It assumes the signed two-sided operator, its relation to the unsigned one and its composition rules from *The Signed Two-Sided Operator on a Bimodule over an Algebra*; the unsigned adjoint from *The Adjoint of the Two-Sided Operator on a Bimodule over an Algebra*; the pairing and the adjoint of *The Adjoint of a Module Homomorphism*; and the involution of *The Involution on the Endomorphism Ring of a Module*. The self-adjointness of the reflections, and its failure in the degenerate case, is *The Signed Adjoint of the Reflection on a Bimodule over an Algebra*, and the one-sided case is *The Signed Adjoint of the Left Multiplication on a Module over an Algebra*. The article stays inside Part I: no distance, norm, form with a norm, positivity, topology or limit. Throughout, $R$ is a commutative ring with $1 \neq 0$ in which $2$ is invertible, $(A,\sigma)$ is an involutive $R$-algebra, $\alpha$ is a grade involution of $A$ commuting with $\sigma$, ${}_A M_A$ is a graded $(A,A)$-bimodule with grade involution $\alpha$ commuting with the actions in the graded sense, and the pairing is $\sigma$-sesquilinear, balanced and $\alpha$-invariant.

## The Graded Pairing

### The compatibility of the pairing with the grading

**Definition.** The pairing $\langle\cdot,\cdot\rangle$ on the graded bimodule $(M,\alpha)$ is **$\alpha$-invariant** when

$$
\langle\alpha(x),\alpha(y)\rangle=\langle x,y\rangle \qquad (x,y \in M).
$$

Equivalently, because $\alpha^{2}=\mathrm{id}$,

$$
\langle\alpha(x),y\rangle=\langle x,\alpha(y)\rangle \qquad (x,y \in M).
$$

The pairing is balanced for the involution $\sigma$ when it satisfies the two identities of *The Adjoint of the Two-Sided Operator on a Bimodule over an Algebra*, $\langle ax,y\rangle=\langle x,\sigma(a)y\rangle$ and $\langle xb,y\rangle=\langle x,y\sigma(b)\rangle$.

The two compatibility conditions are the two halves of "the pairing sees both structures": $\sigma$ governs the algebra and $\alpha$ the grading, and the identities say that moving an element across the pairing applies the appropriate structure on the other side.

### The grade involution is self-adjoint and unitary

**Proposition.** For an $\alpha$-invariant pairing the grade involution $\alpha$ is self-adjoint and unitary with respect to the adjoint ${}^{*}$:

$$
\alpha^{*}=\alpha, \qquad \alpha^{*}\alpha=\alpha\alpha^{*}=\mathrm{id} .
$$

*Proof.* The invariance identities give $\langle\alpha(x),y\rangle=\langle x,\alpha(y)\rangle$, which is the defining identity of the adjoint $\alpha^{*}=\alpha$. Then $\alpha^{*}\alpha=\alpha^{2}=\mathrm{id}$ and likewise.

So the grading and the involution of the module are not independent: an $\alpha$-invariant pairing makes the grade involution an isometry, and the adjoint of the grade involution is the grade involution.

## The Adjoint of the Signed Two-Sided Operator

### The main computation

**Theorem.** Let $\beta=\alpha\sigma$ be the composite of the grade involution and the involution of the algebra, an involution of $A$ because $\alpha$ and $\sigma$ commute. Then for all $a,b \in A$,

$$
\boxed{\;\bigl(\mathcal{T}^{\alpha}_{a,b}\bigr)^{*}=\mathcal{T}^{\alpha}_{\beta(a),\,\beta(b)}\;} .
$$

*Proof.* Since $\mathcal{T}^{\alpha}_{a,b}=\mathcal{T}_{a,b}\circ\alpha$ and the adjoint is anti-multiplicative, $(\mathcal{T}^{\alpha}_{a,b})^{*}=\alpha^{*}(\mathcal{T}_{a,b})^{*}$. By the proposition above $\alpha^{*}=\alpha$, and by *The Adjoint of the Two-Sided Operator on a Bimodule over an Algebra* $(\mathcal{T}_{a,b})^{*}=\mathcal{T}_{\sigma(a),\sigma(b)}$. Hence $(\mathcal{T}^{\alpha}_{a,b})^{*}=\alpha\,\mathcal{T}_{\sigma(a),\sigma(b)}$. Finally, the conjugation identity $\mathcal{T}^{\alpha}_{c,d}=\alpha \mathcal{T}_{\alpha^{-1}(c),\alpha^{-1}(d)}$ of *The Signed Two-Sided Operator on a Bimodule over an Algebra* gives $\alpha \mathcal{T}_{\sigma(a),\sigma(b)}=\mathcal{T}^{\alpha}_{\alpha^{-1}\sigma(a),\,\alpha^{-1}\sigma(b)}$, and $\alpha^{-1}\sigma=(\alpha^{-1}\sigma)=\alpha\sigma$ because $\alpha^{-1}=\alpha$ commutes with $\sigma$.

The parameters are transformed by $\beta=\alpha\sigma$, the product of the two involutions, not by $\sigma$ alone: the twist in the middle of the two-sided operator and the twist of the algebra both act, and they compose.

### Parity and the adjoint

**Corollary (the adjoint respects the grading).** The adjoint of a signed two-sided operator is signed and the adjoint of an unsigned two-sided operator is unsigned:

$$
\bigl(\mathcal{T}^{\alpha}_{a,b}\bigr)^{*}=\mathcal{T}^{\alpha}_{\beta(a),\beta(b)}, \qquad \bigl(\mathcal{T}_{a,b}\bigr)^{*}=\mathcal{T}_{\sigma(a),\sigma(b)} .
$$

Consequently the adjoint ${}^{*}$ preserves the $\mathbb{Z}/2$-grading of the monoid $\{\mathcal{T}_{a,b}\}\cup\{\mathcal{T}^{\alpha}_{a,b}\}$: a two-sided operator of parity zero is sent to a two-sided operator of parity zero, and a two-sided operator of parity one to a two-sided operator of parity one.

*Proof.* The first display is the theorem; the second is its $\alpha=\mathrm{id}$ case; the parity statement follows because the adjoint of an unsigned two-sided operator is unsigned and the adjoint of a signed two-sided operator is signed, and it is additive.

### Specialisations

**Proposition.** In the two extreme cases the formula reduces to the known ones:

**(i)** for $\alpha=\mathrm{id}$, $(\mathcal{T}_{a,b})^{*}=\mathcal{T}_{\sigma(a),\sigma(b)}$, the unsigned adjoint;

**(ii)** for $\sigma=\mathrm{id}$, $(\mathcal{T}^{\alpha}_{a,b})^{*}=\mathcal{T}^{\alpha}_{\alpha(a),\alpha(b)}$, the grading alone.

*Proof.* Immediate from $\beta=\alpha\sigma$.

## The Unitarity Condition

### Unitary signed two-sided operators

**Definition.** A signed two-sided operator is **unitary** when

$$
(\mathcal{T}^{\alpha}_{a,b})^{*}\mathcal{T}^{\alpha}_{a,b}=\mathcal{T}^{\alpha}_{a,b}(\mathcal{T}^{\alpha}_{a,b})^{*}=\mathrm{id},
$$

in the sense of the unitary elements of *The Involution on the Endomorphism Ring of a Module*.

**Theorem.** Suppose the two-sided map is injective. Then $\mathcal{T}^{\alpha}_{a,b}$ is unitary if and only if $a$ and $b$ are unitary elements of $A$:

$$
(\mathcal{T}^{\alpha}_{a,b})^{*}\mathcal{T}^{\alpha}_{a,b}=\mathcal{T}^{\alpha}_{a,b}(\mathcal{T}^{\alpha}_{a,b})^{*}=\mathrm{id} \iff \sigma(a)a=a\sigma(a)=1,\quad \sigma(b)b=b\sigma(b)=1 .
$$

*Proof.* By the theorem and the composition rules of the signed two-sided operators,

$$
\boxed{\;(\mathcal{T}^{\alpha}_{a,b})^{*}\mathcal{T}^{\alpha}_{a,b}=\mathcal{T}^{\alpha}_{\beta(a),\beta(b)}\mathcal{T}^{\alpha}_{a,b}=\mathcal{T}_{\beta(a)\alpha(a),\,\alpha(b)\beta(b)}, \qquad \mathcal{T}^{\alpha}_{a,b}(\mathcal{T}^{\alpha}_{a,b})^{*}=\mathcal{T}^{\alpha}_{a,b}\mathcal{T}^{\alpha}_{\beta(a),\beta(b)}=\mathcal{T}_{a\alpha(\beta(a)),\,\alpha(\beta(b))b}\;}.
$$

With $\beta=\alpha\sigma$ and $\alpha^{2}=\mathrm{id}$, the parameters are $\beta(a)\alpha(a)=\alpha(\sigma(a)a)$, $\alpha(b)\beta(b)=\alpha(b\sigma(b))$ in the first product, and $a\alpha(\beta(a))=a\sigma(a)$, $\alpha(\beta(b))b=\sigma(b)b$ in the second. Both products equal $\mathrm{id}=\mathcal{T}_{1,1}$ exactly when $\sigma(a)a=a\sigma(a)=1$ and $\sigma(b)b=b\sigma(b)=1$, by injectivity of the two-sided map.

The parameter criterion is independent of the grading: the grade involution enters the adjoint formula but cancels from the unitarity condition, so the unitary signed two-sided operators are those with unitary parameters, exactly as in the unsigned case.

### The unitary signed two-sided operators form a group

**Proposition.** The unitary signed two-sided operators with a fixed right parameter, or with both parameters fixed as unitary elements, form a group under composition; more precisely, if $a,a'$ and $b,b'$ are unitary in $A$ then $\mathcal{T}^{\alpha}_{a,b}\mathcal{T}^{\alpha}_{a',b'}$ is the unsigned two-sided operator $\mathcal{T}_{a\alpha(a'),\,\alpha(b')b}$ and it is unitary.

*Proof.* The composition rule $\mathcal{T}^{\alpha}_{a,b}\mathcal{T}^{\alpha}_{a',b'}=\mathcal{T}_{a\alpha(a'),\alpha(b')b}$ is that of *The Signed Two-Sided Operator on a Bimodule over an Algebra*; the product of unitary parameters $\alpha(a')$ and $b'$ is unitary, and $\alpha$ preserves unitarity because it is an involution of the algebra, so the parameters $a\alpha(a')$ and $\alpha(b')b$ are unitary and the product is unitary by the previous theorem.

Hence the unitary signed two-sided operators generate a group of isometries of the pairing, and its elements are the products of a unitary parameter on the left, the grade involution, and a unitary parameter on the right.

### Reflections

**Corollary.** For a unit $u$ the reflection $r_u=\mathcal{T}^{\alpha}_{u,u^{-1}}$ has a reflection as its adjoint,

$$
\boxed{\;(r_u)^{*}=\mathcal{T}^{\alpha}_{\beta(u),\,\beta(u)^{-1}}=r_{\beta(u)}\;},
$$

and $r_u$ is unitary exactly when $u$ is a unitary element of $A$.

*Proof.* The adjoint formula with $\mathcal{T}^{\alpha}_{u,u^{-1}}$ and the relation $\beta(u^{-1})=\beta(u)^{-1}$ give the first display; the unitarity criterion with $(a,b)=(u,u^{-1})$ gives the second.

The self-adjointness of the reflection — the case $r_{\beta(u)}=r_u$ — and its failure are the subject of *The Signed Adjoint of the Reflection on a Bimodule over an Algebra*.

## Compatibility with the Involution

### The two involutions of the algebra

**Proposition.** The adjoint of a signed two-sided operator is a signed two-sided operator whose parameters carry the composite involution $\beta=\alpha\sigma$; the involution $\sigma$ and the grade involution $\alpha$ therefore enter asymmetrically: $\sigma$ acts on the parameters of the unsigned adjoint, and $\alpha$ acts through the conjugation identity of the signed two-sided operator, so only the product $\alpha\sigma$ is visible in the answer.

*Proof.* The theorem gives $\beta=\alpha\sigma$; the roles of the two factors are as described in its proof.

**Corollary.** The adjoint operation and the grade involution commute on the two-sided operators,

$$
(\mathcal{T}^{\alpha}_{a,b})^{*}=\alpha\,(\mathcal{T}_{\alpha\sigma(a),\alpha\sigma(b)})\quad\text{and}\quad \alpha\,\mathcal{T}_{a,b}=\mathcal{T}^{\alpha}_{\alpha(a),\alpha(b)},
$$

so applying the adjoint and then the grade involution is the same as applying the grade involution and then the adjoint of the corresponding unsigned two-sided operator.

*Proof.* Both displays are the identities already established, combined.

## Degenerate Cases

### A pairing that is not $\alpha$-invariant

**Proposition.** If the pairing is not $\alpha$-invariant then $\alpha$ need not be self-adjoint and the adjoint of the grade involution, $\alpha^{*}$, is an operator different from $\alpha$; the formula for the adjoint of a signed two-sided operator acquires the extra factor $\alpha^{*}$ and reads $(\mathcal{T}^{\alpha}_{a,b})^{*}=\alpha^{*}\mathcal{T}_{\sigma(a),\sigma(b)}$, which is a signed two-sided operator only when $\alpha^{*}$ maps signed two-sided operators to signed two-sided operators.

*Proof.* The proof of the theorem used only $\alpha^{*}=\alpha$ from invariance; without it the factor $\alpha^{*}$ remains.

### The composite is not an involution

**Proposition.** If $\alpha$ and $\sigma$ do not commute then $\beta=\alpha\sigma$ is not an involution and $\beta^{k}$ cycles; the adjoint of a signed two-sided operator is still a signed two-sided operator with parameters $\beta(a),\beta(b)$, but the map on parameters is no longer an involution, and applying the adjoint twice returns $\mathcal{T}^{\alpha}_{\beta^{2}(a),\beta^{2}(b)}$, which differs from $\mathcal{T}^{\alpha}_{a,b}$ unless $\beta^{2}=\mathrm{id}$.

*Proof.* $(\mathcal{T}^{\alpha}_{a,b})^{**}=\mathcal{T}^{\alpha}_{\beta^{2}(a),\beta^{2}(b)}$ from the theorem; $\beta^{2}=\mathrm{id}$ exactly when $\alpha$ and $\sigma$ commute.

### A non-injective two-sided map

**Proposition.** If the two-sided map is not injective then the unitarity criterion is a criterion on the operator, and the parameters of a unitary signed two-sided operator are determined only up to the kernel of the two-sided map.

*Proof.* The adjoint depends only on the operator and $\mathcal{T}^{\alpha}_{a,b}$ depends only on the image of $(a,b)$ modulo the kernel.

## Examples

**(a) The trivial grading.** For $\alpha=\mathrm{id}$ the signed two-sided operator is the unsigned two-sided operator and the theorem reduces to $(\mathcal{T}_{a,b})^{*}=\mathcal{T}_{\sigma(a),\sigma(b)}$.

**(b) The trivial involution.** For $\sigma=\mathrm{id}$ the adjoint of a signed two-sided operator is $\mathcal{T}^{\alpha}_{\alpha(a),\alpha(b)}$, so the adjoint acts on the parameters by the grade involution alone.

**(c) The group algebra of a finite group.** For $A=R[G]$ with $\sigma(g)=g^{-1}$, $M=A$ the regular bimodule, and $\alpha$ the grading by $G/G^{2}$, the adjoint of $\mathcal{T}^{\alpha}_{g,h}(x)=g\alpha(x)h$ is $\mathcal{T}^{\alpha}_{\alpha\sigma(g),\alpha\sigma(h)}=\mathcal{T}^{\alpha}_{\alpha(g)^{-1},\alpha(h)^{-1}}$ for group elements; the unitarity condition is $g,h$ of order dividing the exponent forced by $\sigma$ and the grading, and it fails for elements of order not two when the grading is trivial.

**(d) The Clifford algebra.** For $A$ a Clifford algebra with its canonical involution $\sigma$ and grade involution $\alpha$, the adjoint of the signed two-sided operator gives the standard formula for conjugation by a versor composed with the reflection of the two-sided operator, and the unitarity condition is the versor condition $\sigma(v)v=1$.

## Summary

On a graded bimodule with a balanced $\sigma$-sesquilinear pairing that is $\alpha$-invariant, the grade involution is self-adjoint and unitary, $\alpha^{*}=\alpha$, and the adjoint of the signed two-sided operator is $\bigl(\mathcal{T}^{\alpha}_{a,b}\bigr)^{*}=\mathcal{T}^{\alpha}_{\beta(a),\beta(b)}$ with $\beta=\alpha\sigma$ the composite of the grade involution and the algebra involution. The adjoint preserves the $\mathbb{Z}/2$-grading: unsigned two-sided operators go to unsigned two-sided operators and signed to signed. The unitarity condition $u^{*}u=uu^{*}=\mathrm{id}$ for a signed two-sided operator holds exactly when its two parameters are unitary elements of $A$, independently of the grading, and the unitary signed two-sided operators compose to unsigned two-sided operators with unitary parameters, generating a group of isometries. The reflection $r_u=\mathcal{T}^{\alpha}_{u,u^{-1}}$ has adjoint $r_{\beta(u)}$ and is unitary exactly when $u$ is unitary in $A$; its self-adjointness is treated separately. When the pairing is not $\alpha$-invariant the formula acquires the factor $\alpha^{*}$, and when $\alpha$ and $\sigma$ do not commute the parameter map is no longer an involution.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $(A,\sigma)$ | base ring, involutive $R$-algebra |
| $\alpha$ | grade involution of $A$, commuting with $\sigma$ |
| ${}_A M_A$ | graded $(A,A)$-bimodule with grade involution $\alpha$ |
| $\langle\cdot,\cdot\rangle$ | balanced σ-sesquilinear, α-invariant pairing |
| $\alpha^{*}=\alpha$ | the grade involution is self-adjoint and unitary |
| $\mathcal{T}_{a,b}$, $\mathcal{T}^{\alpha}_{a,b}$ | unsigned and signed two-sided operators |
| $\beta=\alpha\sigma$ | the composite involution |
| $(\mathcal{T}^{\alpha}_{a,b})^{*}=\mathcal{T}^{\alpha}_{\beta(a),\beta(b)}$ | the adjoint of the signed two-sided operator |
| $\sigma(a)a=a\sigma(a)=1$ | unitarity of the parameter |
| $r_u=\mathcal{T}^{\alpha}_{u,u^{-1}}$ | the reflection, $(r_u)^{*}=r_{\beta(u)}$ |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for involutions, graded algebras and sesquilinear forms.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the interaction of the involution and the grading.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, second edition, 2001), for involutions and the unitarity conditions they define.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for involutions of graded algebras and their two-sided operators.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the grade involution, the conjugation involution and the versor unitarity condition.
