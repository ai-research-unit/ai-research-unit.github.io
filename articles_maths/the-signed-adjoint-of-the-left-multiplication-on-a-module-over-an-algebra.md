
# __The Signed Adjoint of the Left Multiplication on a Module over an Algebra__

## Introduction

The signed left multiplication is the one-sided operator $L^{\alpha}_a(m)=a\,\alpha(m)$ that carries the parity sign of the grading. This article computes its adjoint with respect to an $\alpha$-invariant pairing; the answer is the signed left multiplication by the parameter transformed by the composite $\beta=\alpha\sigma$, $(L^{\alpha}_a)^{*}=L^{\alpha}_{\beta(a)}$. It is the one-sided specialisation of the signed adjoint sandwich and the companion of the unsigned rule $(L_a)^{*}=L_{\sigma(a)}$.

The article is the sixth of the `* Operator Theory` group of this category. It assumes the signed left multiplication and its elementary properties from *The Signed Left Multiplication on a Module over an Algebra*, the signed adjoint sandwich from *The Signed Adjoint of the Sandwich on a Bimodule over an Algebra*, and the pairing and adjoint of *The Adjoint of a Module Homomorphism*; the unsigned one-sided adjoint is *The Adjoint of a Module Homomorphism*, and the reflection case is *The Signed Adjoint of the Reflection on a Bimodule over an Algebra*. The article stays inside Part I: no distance, norm, form with a norm, positivity, topology or limit. Throughout, $R$ is a commutative ring with $1 \neq 0$ in which $2$ is invertible, $(A,\sigma)$ is an involutive $R$-algebra, $\alpha$ is a grade involution of $A$ commuting with $\sigma$, $\beta=\alpha\sigma$, $M$ is a graded left $A$-module with an $\alpha$-invariant balanced $\sigma$-sesquilinear pairing, $L_a(m)=am$ is the unsigned left multiplication, and $L^{\alpha}_a=L_a\circ\alpha$, $L^{\alpha}_a(m)=a\,\alpha(m)$.

## The Signed Left Multiplication and Its Adjoint

### The one-sided adjoint

**Theorem.** For every $a \in A$ the adjoint of the signed left multiplication is the signed left multiplication by the transformed parameter:

$$
\bigl(L^{\alpha}_a\bigr)^{*}=L^{\alpha}_{\beta(a)}, \qquad \beta=\alpha\sigma .
$$

*Proof.* The signed left multiplication is the signed sandwich with right parameter $1$, $L^{\alpha}_a=S^{\alpha}_{a,1}$. By *The Signed Adjoint of the Sandwich on a Bimodule over an Algebra*, $\bigl(S^{\alpha}_{a,1}\bigr)^{*}=S^{\alpha}_{\beta(a),\beta(1)}$, and $\beta(1)=1$ because $\beta$ is an involution of the algebra. Hence the adjoint is $S^{\alpha}_{\beta(a),1}=L^{\alpha}_{\beta(a)}$. $\square$

**Proof (direct).** Write $L^{\alpha}_a=L_a\circ\alpha$, so by anti-multiplicativity $\bigl(L^{\alpha}_a\bigr)^{*}=\alpha^{*}(L_a)^{*}$. The pairing is $\alpha$-invariant, so $\alpha^{*}=\alpha$, and *The Adjoint of a Sandwich on a Bimodule over an Algebra* gives $(L_a)^{*}=L_{\sigma(a)}$. Hence $\bigl(L^{\alpha}_a\bigr)^{*}=\alpha L_{\sigma(a)}=L^{\alpha}_{\alpha\sigma(a)}$, using the identity $\alpha L_b=L^{\alpha}_{\alpha(b)}$ of *The Signed Left Multiplication on a Module over an Algebra*. $\square$

The parameter transforms by the composite $\beta=\alpha\sigma$, exactly as for the general signed sandwich: the grading and the involution both act, and only their product is visible.

### Relation to the unsigned adjoint and to the grading

**Proposition.** The adjoint of the signed left multiplication and the adjoint of the unsigned left multiplication are related by the grade involution:

$$
\bigl(L^{\alpha}_a\bigr)^{*}=\alpha\,(L_{\sigma(a)})^{*}=\alpha\,L_{\sigma(a)}, \qquad \bigl(L_a\bigr)^{*}=L_{\sigma(a)} .
$$

*Proof.* The first is the direct computation in the proof of the theorem; the second is the unsigned rule. $\square$

**Corollary (parity).** The signed left multiplications are odd for the $\mathbb{Z}/2$-grading of the sandwich monoid, and the adjoint sends an odd operator to an odd operator: $\bigl(L^{\alpha}_a\bigr)^{*}=L^{\alpha}_{\beta(a)}$. The adjoint commutes with the grading, as it does for the two-sided operators.

*Proof.* Immediate from the theorem and the parity statement of *The Signed Adjoint of the Sandwich on a Bimodule over an Algebra*. $\square$

## Relation to the Signed Sandwich

### The one-sided operators inside the sandwich

**Proposition.** For all $a,b \in A$ the signed sandwich factors through the signed left multiplication,

$$
S^{\alpha}_{a,b}=L^{\alpha}_a\circ R_{\alpha(b)}, \qquad L^{\alpha}_a=S^{\alpha}_{a,1}, \qquad R^{\alpha}_b:=S^{\alpha}_{1,b} .
$$

*Proof.* $L^{\alpha}_a(R_{\alpha(b)}(x))=a\,\alpha(x\alpha(b))=a\,\alpha(x)\,\alpha(\alpha(b))=a\,\alpha(x)\,b=S^{\alpha}_{a,b}(x)$, and the other identities are the parameter choices. $\square$

**Corollary.** The adjoint of the signed sandwich is the composite of the adjoints of its factors in the reverse order, and the one-sided adjoints assemble it:

$$
\bigl(S^{\alpha}_{a,b}\bigr)^{*}=\bigl(R_{\alpha(b)}\bigr)^{*}\bigl(L^{\alpha}_a\bigr)^{*}=R_{\sigma(\alpha(b))}L^{\alpha}_{\beta(a)}=R_{\beta(b)}L^{\alpha}_{\beta(a)}=S^{\alpha}_{\beta(a),\beta(b)} .
$$

*Proof.* Anti-multiplicativity and the theorem, with the right-handed adjoint $R_c^{*}=R_{\sigma(c)}$ obtained from the opposite algebra as in *The Adjoint of the Sandwich on a Bimodule over an Algebra*. For the middle equality, $\sigma(\alpha(b))=\sigma\alpha(b)=\alpha\sigma(b)=\beta(b)$ because $\alpha$ and $\sigma$ commute. For the last, $R_dL^{\alpha}_c=S^{\alpha}_{c,d}$ directly, since $R_dL^{\alpha}_c(x)=c\,\alpha(x)\,d$. $\square$

The one-sided case is therefore not an analogy but a factorisation: the sandwich is a signed left multiplication composed with a right multiplication, and its adjoint is the composite of the one-sided adjoints.

## Self-Adjointness and Unitarity

### Self-adjoint and skew-adjoint signed left multiplications

**Proposition.** The kernel of the parameter map $a \mapsto L^{\alpha}_a$ is the annihilator $\operatorname{Ann}_A(M)=\{a : aM=0\}$. Consequently

$$
\bigl(L^{\alpha}_a\bigr)^{*}=L^{\alpha}_a \iff \beta(a)-a \in \operatorname{Ann}_A(M), \qquad \bigl(L^{\alpha}_a\bigr)^{*}=-L^{\alpha}_a \iff \beta(a)+a \in \operatorname{Ann}_A(M).
$$

For a faithful module these read $\beta(a)=a$ and $\beta(a)=-a$.

*Proof.* $L^{\alpha}_a=L^{\alpha}_{a'}$ is $L^{\alpha}_{a-a'}=0$, that is $(a-a')M=0$, by the kernel statement of *The Signed Left Multiplication on a Module over an Algebra*; applying this to the theorem gives the criteria. $\square$

So the self-adjoint signed left multiplications are those with $\beta$-symmetric parameter (modulo the annihilator), the analogue of the symmetric operators among the unsigned left multiplications.

### Unitary signed left multiplications

**Proposition.** A signed left multiplication is unitary exactly when its parameter is a unitary element of $A$:

$$
\bigl(L^{\alpha}_a\bigr)^{*}L^{\alpha}_a=L^{\alpha}_a\bigl(L^{\alpha}_a\bigr)^{*}=\mathrm{id} \iff \sigma(a)a=a\sigma(a)=1 .
$$

*Proof.* This is the unitarity criterion of *The Signed Adjoint of the Sandwich on a Bimodule over an Algebra* with $(a,b)=(a,1)$. $\square$

**Corollary.** The unitary signed left multiplications form a group isomorphic to the unitary group of $A$ modulo the annihilator: the map $a \mapsto L^{\alpha}_a$ restricted to the unitary elements of $A$ is multiplicative on unitary parameters and has kernel the unitary elements of $\operatorname{Ann}_A(M)$.

*Proof.* For unitary $a,b$ the composition rule gives $L^{\alpha}_aL^{\alpha}_b=L_{a\alpha(b)}$, and $a\alpha(b)$ is unitary when $a$ and $b$ are; the kernel is computed as above. $\square$

## Kernel, Image and the Paired Complement

### The complement identities

**Proposition.** For every $a$,

$$
\ker\bigl(L^{\alpha}_a\bigr)^{*}=\bigl(\operatorname{im}L^{\alpha}_a\bigr)^{\mathrm{c}}, \qquad \operatorname{im}\bigl(L^{\alpha}_a\bigr)^{*}={}^{\mathrm{c}}\bigl(\ker L^{\alpha}_a\bigr) .
$$

*Proof.* These are the general identities of *The Adjoint of a Module Homomorphism* for the operator $L^{\alpha}_a$. $\square$

### The explicit complements

**Proposition.** With $\operatorname{im}L^{\alpha}_a=aM$ and $\ker L^{\alpha}_a=\alpha(\ker L_a)$,

$$
\ker\bigl(L^{\alpha}_a\bigr)^{*}=\ker L_{\sigma(a)}, \qquad \operatorname{im}\bigl(L^{\alpha}_a\bigr)^{*}=\beta(a)M .
$$

*Proof.* The first is $(aM)^{\mathrm{c}}=\{n : \langle am,n\rangle=0\ \forall m\}=\{n : \langle m,\sigma(a)n\rangle=0\ \forall m\}=\ker L_{\sigma(a)}$ by non-degeneracy. The second is the image of $L^{\alpha}_{\beta(a)}$, namely $\beta(a)M$. $\square$

**Corollary.** The two descriptions agree: $\alpha(\ker L_{\beta(a)})=\ker L_{\sigma(a)}$, which is the identity $\alpha(\ker L_c)=\ker L_{\alpha(c)}$ for $c=\beta(a)$.

*Proof.* $\alpha(\ker L_{\beta(a)})=\{m : \beta(a)\,\alpha(m)=0\}=\{m : \alpha(\sigma(a)m)=0\}=\ker L_{\sigma(a)}$ using $\alpha(\beta(a))=\sigma(a)$. $\square$

## Examples

**(a) The trivial grading.** For $\alpha=\mathrm{id}$ the theorem reduces to $(L_a)^{*}=L_{\sigma(a)}$, the unsigned rule.

**(b) The trivial involution.** For $\sigma=\mathrm{id}$ the adjoint is $(L^{\alpha}_a)^{*}=L^{\alpha}_{\alpha(a)}$, so a signed left multiplication is self-adjoint exactly when its parameter is even.

**(c) The regular module.** For $M={}_A A$ with the regular pairing, $\operatorname{Ann}_A(M)=0$, so the criteria are the exact equalities $\beta(a)=a$ and $\beta(a)=-a$, and the unitary signed left multiplications are the unitary elements of $A$.

**(d) A module with annihilator.** For $A=k[x]/(x^{2})$ acting on $M=k[x]/(x)$ with $x\cdot m=0$, the annihilator is the maximal ideal $(x)$ and every parameter with the same image in $k$ gives the same signed left multiplication: the self-adjointness criterion degenerates to congruence modulo $(x)$, and $\ker L^{\alpha}_a$ is all of $M$ for $a \in (x)$.

**(e) The Clifford algebra.** For $A$ a Clifford algebra with canonical involution $\sigma$ and grade involution $\alpha$, the signed left multiplication $L^{\alpha}_v$ by a vector $v$ has adjoint $L^{\alpha}_{\beta(v)}$ with $\beta=\alpha\sigma$; it is self-adjoint exactly for $\beta(v)=v$, which for a vector holds exactly when the vector's parity is even, and it is unitary exactly for a unit vector $\sigma(v)v=1$.

## Summary

For a graded module with an $\alpha$-invariant balanced $\sigma$-sesquilinear pairing, the adjoint of the signed left multiplication is the signed left multiplication by the composite $\beta=\alpha\sigma$, $\bigl(L^{\alpha}_a\bigr)^{*}=L^{\alpha}_{\beta(a)}$; this is the one-sided case of the signed adjoint sandwich, obtained directly from $\alpha^{*}=\alpha$, $(L_a)^{*}=L_{\sigma(a)}$ and the identity $\alpha L_b=L^{\alpha}_{\alpha(b)}$. The adjoint preserves the grading parity. Because the signed left multiplication is the signed sandwich with right parameter $1$, the sandwich adjoint factors through the one-sided adjoints. Self-adjointness holds exactly when $\beta(a)-a$ annihilates the module, skew-adjointness when $\beta(a)+a$ does, and unitarity exactly when the parameter is unitary in $A$; for a faithful module the criteria are the equalities $\beta(a)=a$, $\beta(a)=-a$ and $\sigma(a)a=a\sigma(a)=1$. The kernel and the image of the adjoint are described by the paired complements: $\ker(L^{\alpha}_a)^{*}=\ker L_{\sigma(a)}$ and $\operatorname{im}(L^{\alpha}_a)^{*}=\beta(a)M$, in agreement with the general theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $(A,\sigma)$ | base ring, involutive $R$-algebra |
| $\alpha$, $\beta=\alpha\sigma$ | grade involution, and the composite involution |
| $M$, $\langle\cdot,\cdot\rangle$ | graded left module with α-invariant balanced σ-sesquilinear pairing |
| $L_a$ | unsigned left multiplication, $L_a(m)=am$ |
| $L^{\alpha}_a=L_a\alpha$ | signed left multiplication, $L^{\alpha}_a(m)=a\alpha(m)$ |
| $(L^{\alpha}_a)^{*}=L^{\alpha}_{\beta(a)}$ | the adjoint of the signed left multiplication |
| $\alpha L_b=L^{\alpha}_{\alpha(b)}$ | the conjugation identity used in the proof |
| $S^{\alpha}_{a,b}=L^{\alpha}_a R_{\alpha(b)}$ | the signed sandwich through the one-sided operators |
| $\operatorname{Ann}_A(M)$ | the annihilator, source of the degenerate criteria |
| $\ker(L^{\alpha}_a)^{*}=\ker L_{\sigma(a)}$ | the kernel of the adjoint |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for graded modules, involutions and sesquilinear forms.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the interaction of the involution and the grading in one-sided operators.
- T. Y. Lam, *Lectures on Modules and Rings* (Springer, 1999), for annihilators, faithful modules and the kernels of one-sided multiplications.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the grade involution and the one-sided actions of a Clifford algebra.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for one-sided multiplication operators and their adjoints over rings.
