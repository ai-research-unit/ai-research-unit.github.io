
# __The Adjoint of the Sandwich with the Signed Product__

## Introduction

The signed sandwich $T^{\alpha}_{a,b}=L_a\alpha R_b$ applies the grade involution to the argument, $x\mapsto a\alpha(x)b$, and its adjoint for the standard form is the signed sandwich by the conjugated parameters,

$$
\bigl(T^{\alpha}_{a,b}\bigr)^{*} = R_{\hat b}\,\alpha\,L_{\hat a} = T^{\alpha}_{\alpha(\hat a),\alpha(\hat b)} = \alpha\,T_{\hat a,\alpha(\hat b)} ,
$$

where the last equality exhibits the adjoint as the grade involution applied to an ordinary sandwich. The two twists — the one in the operator and the one introduced by the adjoint — compose to the identity on the parameters, so the signed family is closed under the adjoint; the reflections, which are the signed sandwiches by $(u,u^{-1})$, are therefore self-adjoint, and this is the operator form of the fact that a reflection of a quadratic space is a self-adjoint operator.

**The boundaries.** The signed sandwich and its composition are *The Signed Sandwich on a Clifford Algebra* and *Two-Sided Operators with the Signed Product*; the ordinary adjoint is *The Adjoint of the Sandwich*; the form, the conjugation and the twisted form are *The Twisted Adjoint on a Clifford Algebra*; the reflections are *Reflections as Signed Two-Sided Operators on a Clifford Algebra*. The base is a field $F$ of characteristic not $2$ with a non-degenerate $q$, $q(u)=B(u,u)$, $uv+vu=2B(u,v)$, and the standard form $\langle x,y\rangle=\operatorname{Sc}(\hat xy)$.

## The Adjoint

**Theorem.** For all $a,b$,

$$
\bigl(T^{\alpha}_{a,b}\bigr)^{*} = R_{\hat b}\,\alpha\,L_{\hat a} = L_{\alpha(\hat a)}\,\alpha\,R_{\alpha(\hat b)} = T^{\alpha}_{\alpha(\hat a),\alpha(\hat b)} ,
$$

and $\bigl(T^{\alpha}_{a,b}\bigr)^{**}=T^{\alpha}_{a,b}$. Equivalently, the adjoint of the signed sandwich is the grade involution of the ordinary sandwich with parameters $(\hat a,\alpha(\hat b))$.

**Proof.** The adjoint of a composition is the reverse composition of the adjoints; the one-factor adjoints are $L_a^*=L_{\hat a}$, $R_b^*=R_{\hat b}$, $\alpha^*=\alpha$, so $\bigl(T^{\alpha}_{a,b}\bigr)^{*}=R_b^*\alpha^*L_a^*=R_{\hat b}\alpha L_{\hat a}$. Using $R_{\hat b}\alpha=\alpha R_{\alpha(\hat b)}$ and $L_{\alpha(\hat a)}\alpha=\alpha L_{\hat a}$, the expression becomes $L_{\alpha(\hat a)}\alpha R_{\alpha(\hat b)}=T^{\alpha}_{\alpha(\hat a),\alpha(\hat b)}$, and also $\alpha R_{\alpha(\hat b)}L_{\hat a}=\alpha L_{\hat a}R_{\alpha(\hat b)}=\alpha T_{\hat a,\alpha(\hat b)}$. Applying the adjoint twice returns the conjugation twice and $\alpha$ twice, hence the operator itself.

**Proposition (self-adjointness).** $T^{\alpha}_{a,b}$ is self-adjoint if and only if $(\alpha(\hat a),\alpha(\hat b))=(ac,c^{-1}b)$ for a central unit $c$; in particular every reflection $T^{\alpha}_{u,u^{-1}}$, $q(u)\ne0$, is self-adjoint.

**Proof.** Combine the adjoint formula with the equality criterion for two two-sided operators, which is the central-unit indeterminacy of *The Sandwich on a Clifford Algebra*. For the reflection, $\hat u=-u$ so $\alpha(\hat u)=u$, and $\widehat{u^{-1}}=(\hat u)^{-1}=-u^{-1}$ so $\alpha(\widehat{u^{-1}})=u^{-1}$; the conjugated pair is $(u,u^{-1})$, and the operator is fixed.

**Proposition (twisted form).** For the twisted form $\langle x,y\rangle_\alpha=\langle\alpha(x),y\rangle$ the adjoint of the signed sandwich is the **same** operator,

$$
\bigl(T^{\alpha}_{a,b}\bigr)^{*\alpha}=\bigl(T^{\alpha}_{a,b}\bigr)^{*} ,
$$

because the twist of the form and the twist of the operator cancel, as *The Twisted Adjoint on a Clifford Algebra* records; in particular self-adjointness of a signed sandwich is the same condition for the two forms.

**Proof.** The general identity $A^{*\alpha}=\alpha A^*\alpha$ gives $\bigl(T^{\alpha}_{a,b}\bigr)^{*\alpha}=\alpha\,T^{\alpha}_{\alpha(\hat a),\alpha(\hat b)}\,\alpha=T^{\alpha}_{\hat a,\hat b}$, which is displayed in the twisted-adjoint article; the equality with the standard adjoint is the cancellation statement recorded there, and it holds because $T^{\alpha}_{c,d}$ already contains one factor $\alpha$.

## The One-Sided Factors

**Proposition.** For the signed left multiplication $\mathrm{L}^{\alpha}_a=L_a\alpha$ and the signed right multiplication $R_a\alpha$,

$$
(L_a\alpha)^{*} = \alpha L_{\hat a} = L_{\alpha(\hat a)}\,\alpha , \qquad
(R_b\alpha)^{*} = \alpha R_{\hat b} = R_{\alpha(\hat b)}\,\alpha .
$$

Each adjoint is again a signed one-sided operator, with the parameter sent to its image under $\alpha\circ\hat{\ }$; the signed one-sided families are therefore closed under the adjoint.

**Proof.** $(L_a\alpha)^*=\alpha^*L_a^*=\alpha L_{\hat a}$, and $\alpha L_{\hat a}=L_{\alpha(\hat a)}\alpha$; the right case is identical. The closure statement is the form of the result.

**Remark.** The closure of the signed families under the adjoint is the operator reason the signed calculus is stable: the adjoint of a signed operator is signed, the adjoint of an ordinary operator is ordinary, and the two are exchanged by multiplying with $\alpha$. This mirrors the coset structure $T\alpha$ of the invertible signed two-sided operators, which is a torsor under the ordinary group.

## Worked Cases

### A Reflection

For $u$ with $q(u)\ne0$ the reflection is $T^{\alpha}_{u,u^{-1}}$; it is self-adjoint for the standard form and for the twisted form, and the adjoint of its ordinary companion $T_{u,u^{-1}}=-\rho_u$ is $T_{-u,-u^{-1}}=-\rho_u$ as well, since the conjugation sends $u$ to $-u$ and $u^{-1}$ to $-u^{-1}$. The reflection is therefore self-adjoint and its ordinary companion is the negative of a self-adjoint operator, hence skew-adjoint automatically.

### A Signed Left Multiplication

For the signed left multiplication by a vector $u$, $(L_u\alpha)^*=\alpha L_{-u}=L_u\alpha$: the signed left multiplication by a vector is **self-adjoint**, in contrast with the ordinary $L_u^*=-L_u$. The grade involution converts the skew-adjoint multiplication into a self-adjoint one, which is the operator form of the reflection being self-adjoint.

### An Even Parameter

For $a=x$ even, $\alpha(x)=x$ and $\alpha(\hat x)=\hat x$, so the adjoint of $T^{\alpha}_{x,b}$ is $T^{\alpha}_{\hat x,\alpha(\hat b)}$; when $b$ is a scalar the signed sandwich coincides with the ordinary one and the adjoint reduces to the ordinary formula.

## Summary

The adjoint of the **signed sandwich** is the signed sandwich by the doubly twisted parameters, $\bigl(T^{\alpha}_{a,b}\bigr)^{*}=R_{\hat b}\alpha L_{\hat a}=T^{\alpha}_{\alpha(\hat a),\alpha(\hat b)}=\alpha T_{\hat a,\alpha(\hat b)}$, and the adjoint is an involution of the signed family. The signed sandwich is **self-adjoint** exactly when $(\alpha(\hat a),\alpha(\hat b))=(ac,c^{-1}b)$ with $c$ central; in particular every **reflection** $T^{\alpha}_{u,u^{-1}}$ is self-adjoint. For the **twisted form** the adjoint of the signed sandwich is the same operator, because the twist of the form cancels against the twist of the operator. The signed one-sided factors have adjoints $(L_a\alpha)^*=\alpha L_{\hat a}=L_{\alpha(\hat a)}\alpha$ and similarly on the right, so the signed one-sided families are closed under the adjoint; the signed left multiplication by a vector is self-adjoint while the ordinary one is skew-adjoint. The operator is *The Signed Sandwich on a Clifford Algebra*, the ordinary adjoint is *The Adjoint of the Sandwich*, and the form is *The Twisted Adjoint on a Clifford Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T^{\alpha}_{a,b}=L_a\alpha R_b$ | Signed sandwich, $x\mapsto a\alpha(x)b$ |
| $\bigl(T^{\alpha}_{a,b}\bigr)^{*}=T^{\alpha}_{\alpha(\hat a),\alpha(\hat b)}$ | Adjoint for the standard form |
| $\bigl(T^{\alpha}_{a,b}\bigr)^{*}=\alpha T_{\hat a,\alpha(\hat b)}$ | Equivalent form through an ordinary sandwich |
| $(\alpha(\hat a),\alpha(\hat b))=(ac,c^{-1}b)$, $c$ central | Self-adjointness condition |
| $T^{\alpha}_{u,u^{-1}}$ self-adjoint | Self-adjointness of every reflection |
| $\bigl(T^{\alpha}_{a,b}\bigr)^{*\alpha}=\bigl(T^{\alpha}_{a,b}\bigr)^{*}$ | Cancellation of the twists for the twisted form |
| $(L_a\alpha)^*=\alpha L_{\hat a}$ | Adjoint of a signed one-sided factor |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the
  signed two-sided operators and their adjoints in the low-dimensional algebras.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced
  Mathematics 50 (Cambridge University Press, 1995), for the signed products, the twisted forms and the
  adjoints.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for
  the reflection operators and their self-adjointness.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2
  (Springer, 1997), for the conjugation, the reflections and the two-sided operators.
