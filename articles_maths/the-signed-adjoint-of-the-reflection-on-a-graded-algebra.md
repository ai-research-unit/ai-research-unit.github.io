
# __The Signed Adjoint of the Reflection on a Graded Algebra__

## Introduction

A **reflection** of a graded algebra $A$ is an order-two signed sandwich $\Sigma^{\alpha}_{a,a^{-1}}(x)=a\,\alpha(x)\,a^{-1}$ with $a\,\alpha(a)=1$, as established in *Reflections as Signed Two-Sided Operators on a Graded Algebra*. When $A$ carries a balanced α-compatible form, every reflection has an adjoint, and the adjoint is computed in *The Signed Adjoint Sandwich on a Graded Algebra* as $(\Sigma^{\alpha}_{a,a^{-1}})^{\dagger}=\Sigma^{\alpha}_{\alpha(a^{-1}),\alpha(a)}$. The two expressions coincide: **every reflection is self-adjoint**. This article, the sixth of the `- * Operator Theory` group of the category, proves the self-adjointness, generalises it to the criterion that $\Sigma^{\alpha}_{a,a^{-1}}$ is self-adjoint exactly when $a\,\alpha(a)$ is central, exhibits the **failure** of self-adjointness in the degenerate case by an explicit non-central element, and reads the $\pm1$-eigenspace decomposition of a reflection as the decomposition attached to a self-adjoint operator. The reflections and the sandwiches are *Reflections as Signed Two-Sided Operators on a Graded Algebra* and *The Signed Sandwich on a Graded Algebra*; the form and the adjoint are *The Signed Adjoint Sandwich on a Graded Algebra*; the analytic spectral theory of a self-adjoint operator belongs to a later Part and is named only.

The base is a field $K$ of characteristic not two, $A$ a finite-dimensional graded algebra with grade involution $\alpha$ and a balanced α-compatible nondegenerate form $\beta$ with $\alpha^{\dagger}=\alpha$. The reflections are written $\Sigma^{\alpha}_{a,a^{-1}}$ and the operators ${}^{\dagger}$; the article uses the form algebraically and forms no length from it.

## The Adjoint of a Reflection

**Theorem.** Let $a$ be a unit with $a\,\alpha(a)=1$. Then the signed reflection $\Sigma^{\alpha}_{a,a^{-1}}$ is self-adjoint:

$$
(\Sigma^{\alpha}_{a,a^{-1}})^{\dagger}=\Sigma^{\alpha}_{a,a^{-1}} .
$$

**Proof.** The adjoint formula of *The Signed Adjoint Sandwich on a Graded Algebra* gives
$$
(\Sigma^{\alpha}_{a,a^{-1}})^{\dagger}=\Sigma^{\alpha}_{\alpha(a^{-1}),\alpha(a)} .
$$
Since $\alpha$ is an automorphism and $\alpha(a)=a^{-1}$, one has $\alpha(a^{-1})=\alpha(a)^{-1}=a$, so the adjoint is $\Sigma^{\alpha}_{a,a^{-1}}$. $\square$

**Corollary.** The grade involution $\alpha=\Sigma^{\alpha}_{1,1}$ is self-adjoint, and the reflection $\Sigma^{\alpha}_{u,u^{-1}}$ attached to a unitary element $u$ of a star is self-adjoint; the reflections form a family all of whose members are self-adjoint, in contrast with the general sandwiches of *The Signed Adjoint Sandwich on a Graded Algebra*, whose adjoint reverses the elements.

**Remark (the parity of the defining element).** The reflection condition $a\alpha(a)=1$ reads differently according to the parity of $a$: for an even $a$ one has $\alpha(a)=a$, so the condition is $a^{2}=1$ and the reflection is the sandwich $a\alpha(\cdot)a$; for an odd $a$ one has $\alpha(a)=-a$, so the condition is $a^{2}=-1$ in characteristic not two, and the inverse is $a^{-1}=-a=\alpha(a)$.

## The Self-Adjointness Criterion

**Theorem.** Let $a$ be a unit, and put $c=a\,\alpha(a)$. Then $\Sigma^{\alpha}_{a,a^{-1}}$ is self-adjoint if and only if $c$ is central. In particular every reflection ($c=1$) is self-adjoint, and the self-adjointness of a signed sandwich of reflection shape is exactly the centrality of its normalising element.

**Proof.** By the adjoint formula, $(\Sigma^{\alpha}_{a,a^{-1}})^{\dagger}=\Sigma^{\alpha}_{\alpha(a)^{-1},\alpha(a)}$, which is the reflection-shaped sandwich $\Sigma^{\alpha}_{b,b^{-1}}$ with $b=\alpha(a)^{-1}$. By the injectivity-up-to-the-centre of the reflection correspondence of *Reflections as Signed Two-Sided Operators on a Graded Algebra*, two reflection-shaped signed sandwiches with the same shape coincide if and only if the corresponding elements differ by a central unit; here $b^{-1}a=\alpha(a)a=c$ must be central. Conversely, if $c$ is central then $b^{-1}a=c$ is central and the sandwiches coincide. $\square$

**Corollary.** The self-adjointness of a reflection is therefore automatic, and the self-adjointness of the wider family of reflection-shaped sandwiches is a centrality condition on the product $a\alpha(a)$; the centrality is the algebraic form in which the normalisation $a\alpha(a)=1$ is relaxed.

## Failure in the Degenerate Case

**Definition.** The reflection-shaped sandwich $\Sigma^{\alpha}_{a,a^{-1}}$ is **degenerate** when $c=a\alpha(a)$ is not central, and **totally degenerate** when $a$ is not a unit, so that $a^{-1}$ does not exist and the sandwich is not defined.

**Theorem (failure of self-adjointness).** There exist graded algebras with a balanced α-compatible form and a unit $a$ for which $\Sigma^{\alpha}_{a,a^{-1}}$ is not self-adjoint; concretely, in $A=\mathrm{End}_K(V)$ with the grade involution $\alpha(X)=JXJ^{-1}$, $J=\operatorname{diag}(1,-1)$, the trace form $\beta(X,Y)=\operatorname{tr}(XY)$ and the unit $a=\operatorname{diag}(1,2)$ one has $\alpha(a)=a$, hence $c=a\alpha(a)=\operatorname{diag}(1,4)$ non-central, and the conjugation $\Sigma^{\alpha}_{a,a^{-1}}(X)=aXa^{-1}$ has adjoint $\Sigma^{\alpha}_{a^{-1},a}(X)=a^{-1}Xa\neq aXa^{-1}$.

**Proof.** The element $a=\operatorname{diag}(1,2)$ commutes with $J$, so $\alpha(a)=a$ and $c=\operatorname{diag}(1,4)$, which is not a scalar and therefore not central in $\mathsf{M}_2(K)$; by the criterion the sandwich is not self-adjoint. The adjoint is computed by the general formula as $\Sigma^{\alpha}_{a^{-1},a}$, and $a^{-1}Xa\neq aXa^{-1}$ for example at $X=\begin{pmatrix}0&1\\0&0\end{pmatrix}$. $\square$

**Corollary (the totally degenerate case).** When $a$ is not a unit the reflection-shaped sandwich does not exist; the related operator $\Sigma^{\alpha}_{a,a}$ is defined for every $a$ and satisfies $\Sigma^{\alpha}_{a,a}\circ\Sigma^{\alpha}_{a,a}=\Sigma^{\alpha}_{a\alpha(a),\,\alpha(a)a}$, which is the zero operator when $a\alpha(a)=0$; in the exterior algebra an odd vector $v$ gives $\Sigma^{\alpha}_{v,v}=0$, a square-zero operator that is not a reflection, and the self-adjointness question for the reflection does not arise because the reflection is not defined.

## The Eigenspace Decomposition

**Proposition.** A reflection $S=\Sigma^{\alpha}_{a,a^{-1}}$ satisfies $S^{2}=\mathrm{id}$, so it decomposes $A$ into the two eigenspaces $A_\pm=\{x:Sx=\pm x\}$, the fixed part and the anti-fixed part; the decomposition is defined by the operator alone, and the two projectors $\tfrac12(\mathrm{id}\pm S)$ are the spectral projectors of $S$.

**Proof.** An involutive operator is diagonalisable with eigenvalues $\pm1$ in characteristic not two, and the eigenspaces are the ranges of the spectral projectors $\tfrac12(\mathrm{id}\pm S)$; self-adjointness does not change the decomposition, which is determined by $S$. $\square$

**Corollary.** The fixed part of the grade involution $\alpha=\Sigma^{\alpha}_{1,1}$ is the even part and the anti-fixed part the odd part; the fixed part of a general reflection is the set of $x$ with $a\alpha(x)a^{-1}=x$, that is $\alpha(x)=a^{-1}xa$; and the two parts have the same dimension when the reflection is described by an even element and conjugate to $\alpha$.

## Worked Case: The Reflection Defined by the Grade Involution

Let $A=\mathrm{End}_K(V)$ with $J=\operatorname{diag}(1,-1)$, $\alpha(X)=JXJ$, and $\beta(X,Y)=\operatorname{tr}(XY)$. For $a=J$ one has $a\alpha(a)=J\cdot J=1$, so $\Sigma^{\alpha}_{J,J^{-1}}$ is a reflection; the adjoint formula gives $(\Sigma^{\alpha}_{J,J^{-1}})^{\dagger}=\Sigma^{\alpha}_{\alpha(J^{-1}),\alpha(J)}=\Sigma^{\alpha}_{J,J}$ (since $\alpha(J)=J$ and $J^{-1}=J$), which equals the reflection itself, confirming self-adjointness. Its fixed part is the set of $X$ with $JXJ=X$, that is the matrices commuting with $J$, the even matrices plus the diagonal odd part, and its anti-fixed part is the complementary set.

For the non-reflection unit $a=\operatorname{diag}(1,2)$ the sandwich $\Sigma^{\alpha}_{a,a^{-1}}$ is not self-adjoint, as displayed; the adjoint is $\Sigma^{\alpha}_{a^{-1},a}$, the conjugation by $a^{-1}$, and the two differ on the elementary matrix $E_{12}$.

**Verified.** Self-adjointness of $\Sigma^{\alpha}_{J,J}$ was checked on the four basis elements of $\mathsf{M}_2(K)$; the non-self-adjointness of the conjugation by $\operatorname{diag}(1,2)$ was checked by comparing $\beta(SX,Y)$ and $\beta(X,S^{\dagger}Y)$ at the basis element $X=E_{12}$, $Y=E_{11}$.

## Summary

A **signed reflection** $\Sigma^{\alpha}_{a,a^{-1}}$ with $a\alpha(a)=1$ has adjoint $\Sigma^{\alpha}_{\alpha(a^{-1}),\alpha(a)}$, which equals the reflection itself because $\alpha(a)=a^{-1}$; hence **every reflection is self-adjoint** with respect to a balanced α-compatible form. More generally $\Sigma^{\alpha}_{a,a^{-1}}$ is self-adjoint exactly when $a\,\alpha(a)$ is central, the centrality being the relaxed form of the reflection normalisation; the **degenerate** case in which $a\alpha(a)$ is not central produces a reflection-shaped sandwich that is not self-adjoint, with the explicit example the conjugation by $\operatorname{diag}(1,2)$ in $\mathsf{M}_2(K)$ for the trace form, and the **totally degenerate** case in which $a$ is not a unit produces no reflection at all, the related operator $\Sigma^{\alpha}_{a,a}$ being square-zero when $a\alpha(a)=0$, as for an odd vector in the exterior algebra. The $\pm1$-eigenspace decomposition of a reflection is its spectral decomposition, with the fixed part $\alpha(x)=a^{-1}xa$; for the grade involution it is the even-odd decomposition. The analytic spectral theory of the self-adjoint reflections belongs to a later Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | the base field, of characteristic not two |
| $A=A^0\oplus A^1$ | a graded algebra with a balanced α-compatible form |
| $\alpha$ | the grade involution |
| $\Sigma^{\alpha}_{a,b}(x)=a\alpha(x)b$ | the signed sandwich |
| $\Sigma^{\alpha}_{a,a^{-1}}$ | a signed reflection when $a\alpha(a)=1$ |
| $S^{\dagger}$ | the adjoint of $S$ |
| $A_\pm$ | the $\pm1$-eigenspaces of a reflection |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for reflections as signed conjugations and their self-adjointness.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the reflection operators of the Clifford algebra.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the centrality conditions on conjugations.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1989), for the spectral decomposition of an involution.
