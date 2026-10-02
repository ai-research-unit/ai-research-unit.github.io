
# __The Signed Adjoint Sandwich on a Complex Vector Space__

## Introduction

The signed sandwich on the endomorphism algebra $E = \operatorname{End}_{\mathbb C}(V)$ is
$$
\Theta^{\alpha}_{a,b}(X) = a\,\alpha(X)\,b,
$$
with $\alpha(X) = TXT$ the grade involution of a unitary self-adjoint involution $T$ of a Hermitian space $V$, and the form of the category on $E$ is the Hermitian trace form $\langle X, Y\rangle = \operatorname{tr}(X^{\dagger}Y)$. The **adjoint** of the signed sandwich for this form is again a signed sandwich,
$$
\bigl(\Theta^{\alpha}_{a,b}\bigr)^{*} = \Theta^{\alpha}_{\alpha(a^{\dagger}),\,\alpha(b^{\dagger})},
$$
the signed sandwich of the transported adjoint elements: the adjoint exchanges $a$ and $b$ through the involution and the dagger, and the verification is the identity $\alpha(X^{\dagger}) = \alpha(X)^{\dagger}$ of the unitary self-adjoint $T$. The formula is the signed form of the ordinary adjoint law $\Phi_{a,b}^{*} = \Phi_{a^{\dagger},b^{\dagger}}$ of *The Adjoint of the Left Multiplication on a Complex Vector Space*, and it makes the **unitarity condition** explicit: the signed sandwich $\Theta^{\alpha}_{a,b}$ is an isometry of the trace form exactly when both $a$ and $b$ are unitary, because
$$
\bigl(\Theta^{\alpha}_{a,b}\bigr)^{*}\Theta^{\alpha}_{a,b} = \Theta^{\alpha}_{\alpha(a^{\dagger}a),\,\alpha(bb^{\dagger})},
$$
which is the identity exactly for $a^{\dagger}a = \mathrm{id}$ and $bb^{\dagger} = \mathrm{id}$. The adjoint of the inner signed sandwich and of the reflection's sandwich are the two corollaries of the formula.

The article has three sections: the adjoint of the signed sandwich and its proof; the unitarity condition; and the signed inner sandwich and the reflections. The signed sandwich, its laws and the grade involution are *The Signed Sandwich on a Complex Vector Space*; the unsigned adjoint law is *The Adjoint of the Left Multiplication on a Complex Vector Space*, the preceding article of this group; the endomorphism algebra and the trace form are *Algebras of Endomorphisms* and *The Left and Right Multiplication Operators on a Complex Vector Space*; the reflections are *Reflections as Signed Two-Sided Operators on a Complex Vector Space* and *The Signed Adjoint of the Reflection on a Complex Vector Space*; the Hermitian forms and the adjoint of a Hermitian operator are *Hermitian Geometry and the Unitary Group* and *The Adjoint of a Hermitian Operator*. None of that is re-derived.

Throughout, $V$ is a finite-dimensional complex vector space with a positive-definite Hermitian form $h$, $E = \operatorname{End}_{\mathbb C}(V)$, $A^{\dagger}$ is the $h$-adjoint, $T$ is a unitary self-adjoint involution, $\alpha(X) = TXT$, $\Phi_{a,b}(X) = aXb$ and $\Theta^{\alpha}_{a,b}(X) = a\alpha(X)b$ are the unsigned and signed sandwiches, and $\langle X,Y\rangle = \operatorname{tr}(X^{\dagger}Y)$ is the Hermitian trace form.

## The Adjoint of the Signed Sandwich

**Proposition (adjoint of the involution).** The grade involution is self-adjoint for the trace form, $\alpha^{*} = \alpha$, because $T$ is unitary and self-adjoint; and it preserves the adjoint, $\alpha(X^{\dagger}) = \alpha(X)^{\dagger}$.

**Proof.** $\langle\alpha(X), Y\rangle = \operatorname{tr}((TXT)^{\dagger}Y) = \operatorname{tr}(TX^{\dagger}TY) = \operatorname{tr}(X^{\dagger}TYT) = \langle X,\alpha(Y)\rangle$, using $T^{\dagger}=T$ and the trace cyclicity; the second statement is the same computation, $(TXT)^{\dagger} = TX^{\dagger}T$. This is *The Involution on a Complex Vector Space*.

**Theorem (the signed adjoint).** For all $a,b \in E$,
$$
\bigl(\Theta^{\alpha}_{a,b}\bigr)^{*} = \Theta^{\alpha}_{\alpha(a^{\dagger}),\,\alpha(b^{\dagger})},
$$
and in particular the unsigned case is $\Phi_{a,b}^{*} = \Phi_{a^{\dagger},b^{\dagger}}$; the adjoint is conjugate-linear in the pair and involutive, $(\Theta^{*})^{*} = \Theta$.

**Proof.** Write $\Theta^{\alpha}_{a,b} = \Phi_{a,b}\circ\alpha$. Then $\bigl(\Theta^{\alpha}_{a,b}\bigr)^{*} = \alpha^{*}\Phi_{a,b}^{*} = \alpha\circ\Phi_{a^{\dagger},b^{\dagger}}$, using $\alpha^{*}=\alpha$ and the unsigned adjoint law; as an operator, $\alpha(\Phi_{a^{\dagger},b^{\dagger}}(Y)) = \alpha(a^{\dagger}Yb^{\dagger}) = Ta^{\dagger}Yb^{\dagger}T = \Theta^{\alpha}_{\alpha(a^{\dagger}),\alpha(b^{\dagger})}(Y)$, since $\Theta^{\alpha}_{c,d}(Y) = c\alpha(Y)d$ with $c = \alpha(a^{\dagger}) = Ta^{\dagger}T$, $d=\alpha(b^{\dagger})=Tb^{\dagger}T$ gives $Ta^{\dagger}T\cdot TYT\cdot Tb^{\dagger}T = Ta^{\dagger}Yb^{\dagger}T$. The involutivity is $\alpha^2=\mathrm{id}$ and $(a^{\dagger})^{\dagger}=a$. The unsigned adjoint law is *The Adjoint of the Left Multiplication on a Complex Vector Space*, and the sandwich laws are *The Signed Sandwich on a Complex Vector Space*.

**Corollary (the self-adjoint signed sandwiches).** $\Theta^{\alpha}_{a,b}$ is self-adjoint, $(\Theta^{\alpha}_{a,b})^{*} = \Theta^{\alpha}_{a,b}$, exactly when
$$
a = \alpha(a^{\dagger}), \qquad b = \alpha(b^{\dagger}),
$$
that is when $aT$ and $bT$ are Hermitian; in particular the signed sandwich of a Hermitian $a$ with $b = a$ and $a = \alpha(a)$ is self-adjoint.

**Proof.** The identity $\Theta^{\alpha}_{\alpha(a^{\dagger}),\alpha(b^{\dagger})} = \Theta^{\alpha}_{a,b}$ holds when $\alpha(a^{\dagger})=a$ and $\alpha(b^{\dagger})=b$. The first equation is $Ta^{\dagger}T = a$, equivalently (right-multiplying by $T$) $aT = Ta^{\dagger} = (aT)^{\dagger}$, which is the Hermitian condition on $aT$; the second is the same condition on $bT$. This is the self-adjointness criterion of *The Adjoint of a Hermitian Operator*.

## The Unitarity Condition

**Proposition (the unitarity condition).** The signed sandwich satisfies
$$
\bigl(\Theta^{\alpha}_{a,b}\bigr)^{*}\Theta^{\alpha}_{a,b} = \Theta^{\alpha}_{\alpha(a^{\dagger}a),\,\alpha(bb^{\dagger})}, \qquad
\Theta^{\alpha}_{a,b}\bigl(\Theta^{\alpha}_{a,b}\bigr)^{*} = \Theta^{\alpha}_{\alpha(aa^{\dagger}),\,\alpha(b^{\dagger}b)},
$$
and it is a **unitary** operator on the Hermitian space $E$ exactly when $a$ and $b$ are unitary; the signed sandwiches with $a,b \in U(h)$ form the group $U(h)\times U(h)$ acting on $E$, each factor acting by a one-sided operator.

**Proof.** The products are computed with the composition law $\Theta_{c,d}\Theta_{a,b} = \Theta_{c\alpha(a),\alpha(b)d}$ of *The Signed Sandwich on a Complex Vector Space*, together with the adjoint formula: $\Theta^{\alpha}_{\alpha(a^{\dagger}),\alpha(b^{\dagger})}\Theta^{\alpha}_{a,b}$ has $c=\alpha(a^{\dagger})$, $d=\alpha(b^{\dagger})$, so $c\alpha(a) = \alpha(a^{\dagger})\alpha(a) = \alpha(a^{\dagger}a)$ and $\alpha(b)d = \alpha(b)\alpha(b^{\dagger}) = \alpha(bb^{\dagger})$. The composite is the identity exactly when $a^{\dagger}a = \mathrm{id}$ and $bb^{\dagger} = \mathrm{id}$, that is when $a$ and $b$ are unitary; the map $(a,b)\mapsto\Theta^{\alpha}_{a,b}$ is then multiplicative and injective. This is *The Adjoint of the Left Multiplication on a Complex Vector Space* and *The Unitary and Symplectic Groups*.

**Corollary (the isometries of the trace form).** The unitary group of the trace form on $E$ contains the image of $U(h)\times U(h)$ under $(a,b)\mapsto\Theta^{\alpha}_{a,b}$; the inner signed sandwich $\Theta^{\alpha}_{u,u^{-1}} = \mathrm{Ad}_u\circ\alpha$ of a unitary $u$ is the diagonal of this action and is an isometry; the signed sandwiches with $a$ or $b$ non-unitary are not isometries.

**Proof.** The unitarity of $\Theta^{\alpha}_{a,b}$ is the previous proposition; the inner signed sandwich has $a=u$ and $b=u^{-1}$ unitary when $u$ is, so it is an isometry; and if $a^{\dagger}a \neq \mathrm{id}$ or $bb^{\dagger}\neq\mathrm{id}$ the composite differs from the identity. This is *The Left and Right Multiplication Operators on a Complex Vector Space*.

## The Signed Inner Sandwich and the Reflections

**Proposition (the adjoint of the inner signed sandwich).** For invertible $a$,
$$
\bigl(\Theta^{\alpha}_{a,a^{-1}}\bigr)^{*} = \Theta^{\alpha}_{\alpha(a^{\dagger}),\,\alpha((a^{-1})^{\dagger})} = \mathrm{Ad}_{\alpha(a^{\dagger})}\circ\alpha ,
$$
and it is unitary exactly when $a$ is unitary; when $a$ is unitary the adjoint is the inverse, $\bigl(\Theta^{\alpha}_{a,a^{-1}}\bigr)^{*} = \bigl(\Theta^{\alpha}_{a,a^{-1}}\bigr)^{-1}$.

**Proof.** The first formula is the theorem with $b = a^{-1}$; the inner sandwich is $\mathrm{Ad}_{a}\circ\alpha$ with parameter $a$, and its adjoint has parameter $\alpha(a^{\dagger})$; unitarity is the criterion; and for unitary $a$ the inverse is the adjoint by the unitarity. The inner sandwiches and their squares are *The Signed Sandwich on a Complex Vector Space*.

**Proposition (the reflection as a self-adjoint signed operator).** Let $r$ be a unitary reflection of $V$, so that $r^2 = \mathrm{id}$, $r^{\dagger} = r$ and $\alpha_r(X) = rXr$. Then the signed inner sandwich of the reflection is the identity, $\Theta^{\alpha_r}_{r,r^{-1}} = \mathrm{id}$, and it is its own adjoint; more generally the signed sandwich $\Theta^{\alpha_r}_{r,r}$ is self-adjoint, since the criterion $r = \alpha_r(r^{\dagger}) = rrr = r^{3}$ holds by $r^{2}=\mathrm{id}$; and the conjugation $\mathrm{Ad}_r = \Theta^{\alpha_r}_{r,r^{-1}}\circ\alpha_r$ is a self-adjoint involution for the trace form.

**Proof.** The identity $\Theta^{\alpha_r}_{r,r^{-1}} = \mathrm{id}$ is the computation $r(rXr)r = X$ of *Reflections as Signed Two-Sided Operators on a Complex Vector Space*; the self-adjointness of $\Theta^{\alpha_r}_{r,r}$ is the criterion with $a = b = r$ Hermitian and $r = \alpha_r(r^\dagger)$; and $\mathrm{Ad}_r = L_rR_{r}$ is self-adjoint because $r^{\dagger}=r$, and an involution because $r^2 = \mathrm{id}$. This is *The Signed Adjoint of the Reflection on a Complex Vector Space*.

**Remark (the failure in the degenerate case).** The formulas presuppose the unitarity and self-adjointness of $T$, which is what makes $\alpha$ self-adjoint and adjoint-preserving. When the form is degenerate the dagger fails to be well behaved and the adjoint formula $\alpha(X^{\dagger}) = \alpha(X)^{\dagger}$ need not hold; the self-adjointness of the reflections and of the conjugations then fails, as in *The Signed Adjoint of the Reflection on a Complex Vector Space*.

## Summary

On the endomorphism algebra of a Hermitian space the adjoint of the signed sandwich is the signed sandwich of the transported adjoints, $(\Theta^{\alpha}_{a,b})^{*} = \Theta^{\alpha}_{\alpha(a^{\dagger}),\alpha(b^{\dagger})}$, proved from the self-adjointness $\alpha^{*}=\alpha$ of the grade involution and the unsigned law $\Phi_{a,b}^{*} = \Phi_{a^{\dagger},b^{\dagger}}$; the signed sandwich is self-adjoint exactly when $a = \alpha(a^{\dagger})$ and $b = \alpha(b^{\dagger})$, that is when $aT$ and $bT$ are Hermitian. The unitarity condition is $a$ and $b$ both unitary, because $(\Theta^{\alpha}_{a,b})^{*}\Theta^{\alpha}_{a,b} = \Theta^{\alpha}_{\alpha(a^{\dagger}a),\alpha(bb^{\dagger})}$; the inner signed sandwich $\Theta^{\alpha}_{a,a^{-1}} = \mathrm{Ad}_a\alpha$ has adjoint with parameter $\alpha(a^{\dagger})$ and is unitary exactly for unitary $a$, and the reflection's signed inner sandwich is the identity, with the conjugation $\mathrm{Ad}_r$ a self-adjoint involution. The signed sandwich and its laws are *The Signed Sandwich on a Complex Vector Space*; the unsigned adjoint law is *The Adjoint of the Left Multiplication on a Complex Vector Space*; the reflections are *Reflections as Signed Two-Sided Operators on a Complex Vector Space* and *The Signed Adjoint of the Reflection on a Complex Vector Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Theta^{\alpha}_{a,b}(X)=a\alpha(X)b$ | the signed sandwich |
| $(\Theta^{\alpha}_{a,b})^{*}=\Theta^{\alpha}_{\alpha(a^{\dagger}),\alpha(b^{\dagger})}$ | the signed adjoint |
| $\alpha^{*}=\alpha$, $\alpha(X^{\dagger})=\alpha(X)^{\dagger}$ | the grade involution is self-adjoint |
| $(\Theta^{\alpha}_{a,b})^{*}\Theta^{\alpha}_{a,b}=\Theta^{\alpha}_{\alpha(a^{\dagger}a),\alpha(bb^{\dagger})}$ | the unitarity condition |
| $a,b$ unitary | the isometry condition |
| $\Theta^{\alpha}_{a,a^{-1}}=\mathrm{Ad}_a\circ\alpha$ | the inner signed sandwich |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the adjoints and the unitarity of sandwiched operators.
- Paul R. Halmos, *Finite-Dimensional Vector Spaces* (Springer, 1974), for the adjoint, the trace form and the unitary operators.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2012), for the conjugate transpose, the trace form and the unitary group.
- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the sandwich operators and the algebras with involution.
