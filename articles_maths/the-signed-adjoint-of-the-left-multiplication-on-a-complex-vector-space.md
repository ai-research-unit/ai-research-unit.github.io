
# __The Signed Adjoint of the Left Multiplication on a Complex Vector Space__

## Introduction

The signed left multiplication is the operator
$$
\Lambda^{\alpha}_{a}(X) = a\,\alpha(X)
$$
on the endomorphism algebra $E = \operatorname{End}_{\mathbb C}(V)$ of a Hermitian space, with $\alpha(X) = TXT$ the grade involution of a unitary self-adjoint involution $T$, and with the Hermitian trace form $\langle X,Y\rangle = \operatorname{tr}(X^{\dagger}Y)$ for the adjoint. The **adjoint** of the signed left multiplication is the signed left multiplication of the transported adjoint,
$$
\bigl(\Lambda^{\alpha}_{a}\bigr)^{*} = \Lambda^{\alpha}_{\alpha(a^{\dagger})},
$$
because the grade involution is self-adjoint, $\alpha^{*} = \alpha$, and the adjoint of the plain left multiplication is $L_{a}^{*} = L_{a^{\dagger}}$: the adjoint moves the dagger into the parameter and lets the involution pass through. The formula is the one-sided case $b = \mathrm{id}$ of the signed adjoint sandwich, and its consequences are the usual ones of a one-sided multiplication: $\Lambda^{\alpha}_{a}$ is self-adjoint exactly when $a = \alpha(a^{\dagger})$, that is when $aT$ is Hermitian, and it is unitary exactly when $a$ is unitary, in which case its adjoint is its inverse. The signed left multiplications realise the left action of $U(h)$ on $E$ twisted by the involution, and they generate with the signed right multiplications the two-sided signed sandwiches.

The article has three sections: the adjoint formula and its proof; the self-adjointness, normality and unitarity of the signed left multiplication; and the relation to the signed sandwich. The signed left multiplication, its composition law and the involution are *The Signed Sandwich on a Complex Vector Space* and *The Signed Left Multiplication on a Complex Vector Space*; the unsigned adjoint law is *The Adjoint of the Left Multiplication on a Complex Vector Space*, the preceding article of this group; the signed adjoint sandwich is *The Signed Adjoint Sandwich on a Complex Vector Space*; the endomorphism algebra, the trace form and the involution are *Algebras of Endomorphisms*, *The Left and Right Multiplication Operators on a Complex Vector Space* and *The Involution on a Complex Vector Space*; the adjoint of a Hermitian operator and the unitary group are *The Adjoint of a Hermitian Operator* and *Hermitian Geometry and the Unitary Group*. None of that is re-derived.

Throughout, $V$ is a finite-dimensional complex vector space with a positive-definite Hermitian form $h$, $E = \operatorname{End}_{\mathbb C}(V)$, $A^{\dagger}$ is the $h$-adjoint, $T$ is a unitary self-adjoint involution, $\alpha(X) = TXT$, $L_a$, $R_b$ are the plain left and right multiplications, $\Lambda^{\alpha}_{a}(X) = a\alpha(X) = L_a\circ\alpha$ and $\rho^{\alpha}_{b}(X) = \alpha(X)b = R_b\circ\alpha$ are the signed one-sided multiplications, and $\langle X,Y\rangle = \operatorname{tr}(X^{\dagger}Y)$ is the trace form.

## The Adjoint of the Signed Left Multiplication

**Proposition (the adjoint formula).** For all $a \in E$,
$$
\bigl(\Lambda^{\alpha}_{a}\bigr)^{*} = \Lambda^{\alpha}_{\alpha(a^{\dagger})}, \qquad \bigl(\rho^{\alpha}_{b}\bigr)^{*} = \rho^{\alpha}_{\alpha(b^{\dagger})},
$$
and the assignment is conjugate-linear and involutive.

**Proof.** $\Lambda^{\alpha}_{a} = L_a\circ\alpha$, so $\bigl(\Lambda^{\alpha}_{a}\bigr)^{*} = \alpha^{*}L_a^{*} = \alpha\circ L_{a^{\dagger}}$, using $\alpha^{*} = \alpha$ (the self-adjointness of the grade involution) and $L_a^{*} = L_{a^{\dagger}}$; and $\alpha L_{a^{\dagger}}(Y) = \alpha(a^{\dagger}Y) = \alpha(a^{\dagger})\alpha(Y) = \Lambda^{\alpha}_{\alpha(a^{\dagger})}(Y)$, because $\alpha$ is an algebra automorphism. The right-handed case is identical on the other side. The self-adjointness of $\alpha$ and the unsigned law are *The Adjoint of the Left Multiplication on a Complex Vector Space*, and the involution is *The Involution on a Complex Vector Space*.

**Corollary (the rectangular relation).** $\Lambda^{\alpha}_{a} = \alpha\circ L_{\alpha(a)}$ and $\rho^{\alpha}_{b} = \alpha\circ R_{\alpha(b)}$, so the signed one-sided operators are the plain one-sided operators conjugated by the involution; consequently $\Lambda^{\alpha}_{a}$ is obtained from $L_{a}$ by $\alpha$, and the adjoint formula reads $\alpha L_{a}^{*}\alpha = L_{\alpha(a)}^{*}$, the compatibility of the previous article.

**Proof.** $\alpha L_{\alpha(a)}(X) = \alpha(\alpha(a)X) = a\alpha(X) = \Lambda^{\alpha}_{a}(X)$, using $\alpha^{2}=\mathrm{id}$; the adjoint reading is $\Lambda^{\alpha}_{\alpha(a^{\dagger})} = \alpha L_{\alpha(\alpha(a^{\dagger}))} = \alpha L_{a^{\dagger}}$. This is *The Signed Left Multiplication on a Complex Vector Space*.

## Self-Adjointness, Normality and Unitarity

**Proposition (the criteria).** The signed left multiplication $\Lambda^{\alpha}_{a}$ is
- self-adjoint exactly when $a = \alpha(a^{\dagger})$, equivalently when $aT$ is Hermitian;
- normal exactly when $a$ is normal;
- unitary exactly when $a$ is unitary.

**Proof.** The self-adjointness is $\Lambda^{\alpha}_{\alpha(a^{\dagger})} = \Lambda^{\alpha}_{a}$, i.e., $\alpha(a^{\dagger}) = a$, the criterion of the signed adjoint article. Normality is $\Lambda^{\alpha}_{\alpha(a^{\dagger})}\Lambda^{\alpha}_{a} = \Lambda^{\alpha}_{a}\Lambda^{\alpha}_{\alpha(a^{\dagger})}$; the composition law $\Lambda^{\alpha}_{c}\Lambda^{\alpha}_{a} = L_{c\alpha(a)}$ turns this into $L_{\alpha(a^{\dagger}a)} = L_{\alpha(aa^{\dagger})}$, that is $\alpha(a^{\dagger}a) = \alpha(aa^{\dagger})$, equivalently $a^{\dagger}a = aa^{\dagger}$ since $\alpha$ is bijective. The unitarity is the unitarity criterion of the signed sandwich with $b=\mathrm{id}$. These are *The Signed Sandwich on a Complex Vector Space* and *The Adjoint of a Hermitian Operator*.

**Corollary (the isometries and the representation).** The map $a\mapsto\Lambda^{\alpha}_{a}$ restricts on $U(h)$ to a faithful unitary representation of $U(h)$ on $E$; for unitary $a$ one has $(\Lambda^{\alpha}_{a})^{*} = (\Lambda^{\alpha}_{a})^{-1}$, so the signed left multiplications of the unitaries are isometries of the trace form.

**Proof.** The unitarity criterion gives the isometry; the map is multiplicative by $\Lambda^{\alpha}_{b}\Lambda^{\alpha}_{a} = L_{b\alpha(a)}$ and injective because $\Lambda^{\alpha}_{a}(\mathrm{id}) = a$; the adjoint is the inverse for unitary parameters. This is *Unitary Representations of a Lie Group* and *The Unitary and Symplectic Groups*.

## The Relation to the Signed Sandwich

**Proposition (the one-sided operators as degenerate sandwiches).** The signed left multiplication is the signed sandwich with the right parameter equal to the identity,
$$
\Lambda^{\alpha}_{a} = \Theta^{\alpha}_{a,\mathrm{id}}, \qquad \rho^{\alpha}_{b} = \Theta^{\alpha}_{\mathrm{id},b},
$$
and its adjoint is the signed sandwich of the transported adjoint and the identity,
$$
\bigl(\Lambda^{\alpha}_{a}\bigr)^{*} = \Theta^{\alpha}_{\alpha(a^{\dagger}),\mathrm{id}} ;
$$
the two-sided signed sandwich is the composite $\Theta^{\alpha}_{a,b} = \Lambda^{\alpha}_{a}\circ\rho^{\alpha}_{b}$.

**Proof.** $\Theta^{\alpha}_{a,\mathrm{id}}(X) = a\alpha(X)\mathrm{id} = \Lambda^{\alpha}_{a}(X)$, and the adjoint follows from the general formula $\bigl(\Theta^{\alpha}_{a,b}\bigr)^{*} = \Theta^{\alpha}_{\alpha(a^{\dagger}),\alpha(b^{\dagger})}$ with $b = \mathrm{id}$ and $\alpha(\mathrm{id}) = \mathrm{id}$; the composite is $\Lambda^{\alpha}_{a}\rho^{\alpha}_{b}(X) = a\alpha(\alpha(X)b) = aX\alpha(b)$, which is the signed sandwich read with the parameters $a,\alpha(b)$. The signed sandwich and its adjoint are *The Signed Sandwich on a Complex Vector Space* and *The Signed Adjoint Sandwich on a Complex Vector Space*.

**Remark (the one-sided versus the two-sided adjoint).** The one-sided case of the adjoint formula is the case in which the unitarity condition of the signed sandwich degenerates to the unitarity of a single parameter, since the identity is unitary; the self-adjointness of the reflections, the conjugations and the involutions of the group all reduce to the one-sided criteria when the other side is the identity, which is why the one-sided signed adjoints are the building blocks of the two-sided ones.

## Summary

For the endomorphism algebra of a Hermitian space with the trace form, the adjoint of the signed left multiplication is $\bigl(\Lambda^{\alpha}_{a}\bigr)^{*} = \Lambda^{\alpha}_{\alpha(a^{\dagger})}$, of the signed right multiplication $\bigl(\rho^{\alpha}_{b}\bigr)^{*} = \rho^{\alpha}_{\alpha(b^{\dagger})}$, proved from the self-adjointness of the grade involution and the unsigned law $L_a^{*}=L_{a^{\dagger}}$; the signed one-sided operators are the plain ones conjugated by $\alpha$, $\Lambda^{\alpha}_{a} = \alpha L_{\alpha(a)}$. The signed left multiplication is self-adjoint exactly when $a = \alpha(a^{\dagger})$ (i.e. $aT$ Hermitian), normal exactly when $a$ is normal, and unitary exactly when $a$ is unitary, in which case the adjoint is the inverse; on $U(h)$ the map $a\mapsto\Lambda^{\alpha}_{a}$ is a faithful unitary representation. The signed left multiplication is the signed sandwich $\Theta^{\alpha}_{a,\mathrm{id}}$, and the two-sided sandwich is the composite of the two one-sided ones. The signed sandwich and its laws are *The Signed Sandwich on a Complex Vector Space* and *The Signed Left Multiplication on a Complex Vector Space*; the unsigned adjoint law is *The Adjoint of the Left Multiplication on a Complex Vector Space*; the signed adjoint sandwich is *The Signed Adjoint Sandwich on a Complex Vector Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Lambda^{\alpha}_{a}(X)=a\alpha(X)$ | the signed left multiplication |
| $\rho^{\alpha}_{b}(X)=\alpha(X)b$ | the signed right multiplication |
| $(\Lambda^{\alpha}_{a})^{*}=\Lambda^{\alpha}_{\alpha(a^{\dagger})}$ | the signed adjoint |
| $\Lambda^{\alpha}_{a}=\alpha L_{\alpha(a)}$ | the rectangular relation |
| $a=\alpha(a^{\dagger})$ | self-adjointness ($aT$ Hermitian) |
| $\Lambda^{\alpha}_{a}=\Theta^{\alpha}_{a,\mathrm{id}}$ | the degenerate signed sandwich |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the adjoints and the twisted multiplications.
- Paul R. Halmos, *Finite-Dimensional Vector Spaces* (Springer, 1974), for the adjoint, the trace form and the one-sided operators.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2012), for the conjugate transpose, the trace form and the unitary groups.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (American Mathematical Society, 2001), for the unitary representations and the trace form.
