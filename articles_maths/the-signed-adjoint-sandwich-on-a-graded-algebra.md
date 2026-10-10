
# __The Signed Adjoint Sandwich on a Graded Algebra__

## Introduction

An operator on an algebra becomes a **unitary** operator as soon as the algebra carries a form, and the adjoint of the operator is read from the form. For the signed sandwich $\Sigma^{\alpha}_{a,b}(x)=a\,\alpha(x)\,b$ of *The Signed Sandwich on a Graded Algebra* — the two-sided multiplication twisted by the grade involution $\alpha$ — the adjoint has a simple shape: it reverses the two elements and inserts the grade involution,

$$
(\Sigma^{\alpha}_{a,b})^{\dagger}=\Sigma^{\alpha}_{\alpha(b),\,\alpha(a)},
$$

and the signed sandwich is an **isometry** of the form exactly when $b=a^{-1}$, so that the signed reflections $\Sigma^{\alpha}_{a,a^{-1}}$ are isometries and, when a star is present, the unitary elements $u$ with $u^{*}u=uu^{*}=1$ give the isometric sandwiches $\Sigma^{\alpha}_{u,u^{*}}$. This article, the fifth of the `- * Operator Theory` group of the category, fixes the form on a graded algebra, defines the adjoint of an operator, computes the adjoints of the left and right multiplications and of the two sandwiches, and derives the **unitarity condition** $u^{*}u=uu^{*}=1$. The graded algebra, the sandwiches and the reflections are *The Signed Sandwich on a Graded Algebra* and *Reflections as Signed Two-Sided Operators on a Graded Algebra*; the element star is *Involutions of the Universal Enveloping Algebra*; the analytic theory of unitary operators on a Hilbert space belongs to a later Part and is named only.

The base is a field $K$ of characteristic not two, $A=A^0\oplus A^1$ is a finite-dimensional $\mathbb{Z}/2$-graded associative algebra with grade involution $\alpha$, and the form is written $\beta$ with adjoint written ${}^{\dagger}$; the element star is written ${}^{*}$ and the operator adjoint ${}^{\dagger}$, to keep the two apart. The article uses the form algebraically and forms no length from it.

## Forms and Adjoints

**Definition.** A bilinear form $\beta$ on $A$ is **nondegenerate** when $\beta(a,\cdot)=0$ implies $a=0$; it is **balanced** when

$$
\beta(ax,y)=\beta(x,ya),\qquad \beta(xb,y)=\beta(x,by)
$$

for all $a,b,x,y$. A balanced form is **α-compatible** when $\beta(\alpha x,\alpha y)=\beta(x,y)$.

**Proposition (the trace form).** Let $T(x,y)=\operatorname{tr}(L_xL_y)$ be the trace form of $A$, where $L_x$ is the left multiplication. Then $T$ is symmetric and balanced,

$$
T(ax,y)=T(x,ya),\qquad T(xb,y)=T(x,by),
$$

and it is nondegenerate when $A$ is semisimple; the grade involution is $T$-self-adjoint, $\alpha^{\dagger}=\alpha$, exactly when $\alpha$ is an inner automorphism, in particular for the algebra of endomorphisms of a graded vector space.

**Proof.** $T(ax,y)=\operatorname{tr}(L_aL_xL_y)=\operatorname{tr}(L_xL_yL_a)=T(x,ya)$ by the cyclicity of the trace, and $T(xb,y)=\operatorname{tr}(L_xL_bL_y)=\operatorname{tr}(L_xL_{by})=T(x,by)$; symmetry is the cyclicity. For an inner $\alpha$, $\alpha(x)=uxu^{-1}$ gives $T(\alpha x,y)=T(x,\alpha^{-1}y)=T(x,\alpha y)$ because $\alpha^2=\mathrm{id}$. $\square$

**Definition.** Let $\beta$ be a nondegenerate form. The **adjoint** of a linear operator $S$ is the operator $S^{\dagger}$ with

$$
\beta(Sx,y)=\beta(x,S^{\dagger}y)\qquad\text{for all }x,y .
$$

**Proposition.** The adjoint is unique when it exists, and the assignment $S\mapsto S^{\dagger}$ is additive and reverses products; when $\beta$ is balanced, every left or right multiplication has an adjoint.

**Proof.** Uniqueness and linearity are the nondegeneracy of $\beta$; the reversal of products is $\beta(STx,y)=\beta(Tx,S^{\dagger}y)=\beta(x,T^{\dagger}S^{\dagger}y)$; the multiplications have adjoints by the balanced conditions. $\square$

**Assumption.** From here the form $\beta$ is balanced, nondegenerate and **α-compatible**, with $\alpha^{\dagger}=\alpha$; the trace form of a semisimple graded algebra with inner grade involution is the model.

## Adjoints of the Multiplications and the Sandwiches

**Theorem.** For a balanced form the left and right multiplications satisfy

$$
(L_a)^{\dagger}=R_a,\qquad (R_b)^{\dagger}=L_b .
$$

**Proof.** $\beta(L_ax,y)=\beta(ax,y)=\beta(x,ya)=\beta(x,R_ay)$ gives the first; the second is the second balanced condition. $\square$

**Corollary.** The unsigned sandwich satisfies $(\Sigma_{a,b})^{\dagger}=\Sigma_{b,a}$, since $\Sigma_{a,b}=L_aR_b$ and $(\Sigma_{a,b})^{\dagger}=R_b^{\dagger}L_a^{\dagger}=L_bR_a=\Sigma_{b,a}$.

**Theorem.** For an α-compatible form the signed sandwich satisfies

$$
(\Sigma^{\alpha}_{a,b})^{\dagger}=\Sigma^{\alpha}_{\alpha(b),\,\alpha(a)} .
$$

**Proof.** Write $\Sigma^{\alpha}_{a,b}=L_aR_b\alpha$. Then $(\Sigma^{\alpha}_{a,b})^{\dagger}=\alpha^{\dagger}R_b^{\dagger}L_a^{\dagger}=\alpha L_bR_a$, and $\alpha L_bR_a(x)=\alpha(b\,x\,a)=\alpha(b)\alpha(x)\alpha(a)=\Sigma^{\alpha}_{\alpha(b),\alpha(a)}(x)$. $\square$

**Corollary.** The adjoint of the signed sandwich is the signed sandwich with the two elements replaced by their images under the grade involution and their order reversed; for the unsigned sandwich, which is the case $\alpha=\mathrm{id}$, this is $\Sigma_{b,a}$, as before; and the adjoint of the signed left multiplication is read from the case $b=1$, $(\ell_a)^{\dagger}=\Sigma^{\alpha}_{\alpha(1),\alpha(a)}=\Sigma^{\alpha}_{1,\alpha(a)}=R_{\alpha(a)}\alpha$, the signed right multiplication.

**Corollary (the sandwich of a reflection).** If $a\alpha(a)=1$ then $\alpha(a)=a^{-1}$ and $\alpha(a^{-1})=a$, so the signed reflection $\Sigma^{\alpha}_{a,a^{-1}}$ satisfies

$$
(\Sigma^{\alpha}_{a,a^{-1}})^{\dagger}=\Sigma^{\alpha}_{\alpha(a^{-1}),\alpha(a)}=\Sigma^{\alpha}_{a,a^{-1}} ,
$$

that is, every nondegenerate signed reflection is **self-adjoint**.

## Isometry and Unitarty

**Definition.** An operator $S$ is an **isometry** of the form, or **unitary**, when $S^{\dagger}S=SS^{\dagger}=\mathrm{id}$; the isometries form a subgroup of the units of $\operatorname{End}_K(A)$.

**Theorem.** The signed sandwich $\Sigma^{\alpha}_{a,b}$ is an isometry of a balanced α-compatible form if and only if $a$ is a unit and $b=a^{-1}$; equivalently the isometric signed sandwiches are exactly the signed reflections $\Sigma^{\alpha}_{a,a^{-1}}$.

**Proof.** By the composition law and the adjoint formula,
$$
(\Sigma^{\alpha}_{a,b})^{\dagger}\Sigma^{\alpha}_{a,b}
=\Sigma^{\alpha}_{\alpha(b),\alpha(a)}\circ\Sigma^{\alpha}_{a,b}
=\Sigma^{\alpha}_{\alpha(b)\alpha(a),\,\alpha(b)\alpha(a)}
=\Sigma^{\alpha}_{c,c},\qquad c=\alpha(ba),
$$
and $\Sigma^{\alpha}_{c,c}$ is the identity exactly when $c=1$, that is $ba=1$. Similarly $\Sigma^{\alpha}_{a,b}(\Sigma^{\alpha}_{a,b})^{\dagger}=\Sigma^{\alpha}_{ab,ba}$ is the identity exactly when $ab=1$. Both conditions hold exactly when $a$ and $b$ are inverse units. $\square$

**Corollary.** Every signed reflection $\Sigma^{\alpha}_{a,a^{-1}}$ is an isometry, and the isometries of the signed sandwich family are exactly these; in particular the grade involution $\alpha=\Sigma^{\alpha}_{1,1}$ is an isometry, and the reflection $\Sigma^{\alpha}_{u,u^{-1}}$ attached to a unitary element $u$ of the star below is an isometry.

## The Element Star and the Unitarity Condition

**Definition.** An **element star** on $A$ is an anti-involution ${}^{*}$ with $(ab)^{*}=b^{*}a^{*}$, $(a^{*})^{*}=a$, compatible with the grading in the sense $\alpha(a^{*})=\alpha(a)^{*}$. It is **compatible with the form** when $\beta(a^{*},b^{*})=\beta(b,a)$.

**Proposition.** If ${}^{*}$ is an element star compatible with the form $\beta$ and the form is α-compatible, then the **star form**

$$
\beta_{*}(x,y)=\beta(x^{*},y)
$$

is a balanced α-compatible form, nondegenerate when $\beta$ is, and with respect to it the adjoints of the multiplications are

$$
(L_a)^{\dagger}=L_{a^{*}},\qquad (R_b)^{\dagger}=R_{b^{*}},\qquad (\Sigma_{a,b})^{\dagger}=\Sigma_{a^{*},b^{*}} .
$$

**Proof.** For the left multiplication, $\beta_{*}(L_ax,y)=\beta((ax)^{*},y)=\beta(x^{*}a^{*},y)=\beta(x^{*},a^{*}y)=\beta_{*}(x,L_{a^{*}}y)$ using the balanced property; the right multiplication is the same computation; the unsigned sandwich is their composite. The form $\beta_{*}$ is balanced and α-compatible by the corresponding properties of $\beta$ and the compatibility of ${}^{*}$ with $\alpha$. $\square$

**Definition.** The **unitary elements** of the pair $(A,{}^{*})$ are those with

$$
u^{*}u=uu^{*}=1 ,
$$

and they form a subgroup $U(A,{}^{*})$ of the units; the condition is the **unitarity condition**.

**Theorem.** If $u$ is unitary then the signed sandwich $\Sigma^{\alpha}_{u,u^{*}}$ is an isometry of the star form.

**Proof.** The form $\beta_{*}$ is balanced and α-compatible by the previous proposition, so the isometry criterion of the previous section applies: $\Sigma^{\alpha}_{a,b}$ is a $\beta_{*}$-isometry exactly when $b=a^{-1}$. For $a=u$ unitary one has $u^{-1}=u^{*}$, so $b=u^{*}=u^{-1}$ and the sandwich is an isometry. $\square$

**Corollary.** The unitary elements give the isometric signed sandwiches; the condition $u^{*}u=uu^{*}=1$ is exactly what makes $\Sigma^{\alpha}_{u,u^{*}}$ unitary, and the map $u\mapsto\Sigma^{\alpha}_{u,u^{*}}$ carries the unitary group into the isometries of $\beta_{*}$, with kernel the central unitary elements by the injectivity-up-to-the-centre of the sandwich correspondence.

## Worked Case: Endomorphisms of a Graded Two-Dimensional Space

Let $V$ have basis $e_1,e_2$ with parity $e_1$ even and $e_2$ odd, $J=\operatorname{diag}(1,-1)$, and $A=\mathrm{End}_K(V)$ with the grading by parity of operators and the grade involution $\alpha(X)=JXJ^{-1}$. Let $\beta(X,Y)=\operatorname{tr}(XY)$, balanced, nondegenerate, α-compatible with $\alpha^{\dagger}=\alpha$.

For $a=J$ one has $\alpha(a)=J$, so $a\alpha(a)=J^2=1$ and $\Sigma^{\alpha}_{J,J^{-1}}=\Sigma^{\alpha}_{J,J}$ is the map $X\mapsto J\alpha(X)J=J(JXJ)J$ up to $J^{-1}=J$, which is the identity; the adjoint formula gives $(\Sigma^{\alpha}_{J,J})^{\dagger}=\Sigma^{\alpha}_{\alpha(J),\alpha(J)}=\Sigma^{\alpha}_{J,J}$, self-adjoint, and it is trivially an isometry.

For $a=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ one computes $\alpha(a)=\begin{pmatrix}1&-1\\0&1\end{pmatrix}$ and $a\alpha(a)=I$, so $a$ lies in $\mathrm{R}(A)$; $\Sigma^{\alpha}_{a,a^{-1}}$ is a signed reflection, self-adjoint by the corollary, and an isometry by the theorem. Taking the element star $X^{*}=X^{\dagger}_{\text{Herm}}$ the adjoint transpose, the unitary elements are the matrices with $X^{*}X=XX^{*}=I$, and for such a $u$ the sandwich $\Sigma^{\alpha}_{u,u^{*}}$ is isometric, the explicit verification being the multiplication of the two $2\times2$ matrices.

**Verified.** The adjoint formula $(\Sigma^{\alpha}_{a,b})^{\dagger}=\Sigma^{\alpha}_{\alpha(b),\alpha(a)}$ was checked on the four basis elements of $\mathsf{M}_2(K)$ for the trace form and the grade involution $\alpha(X)=JXJ^{-1}$; the self-adjointness of $\Sigma^{\alpha}_{a,a^{-1}}$ was checked for $a=J$ and for $a=\begin{pmatrix}1&1\\0&1\end{pmatrix}$; the isometry condition was checked to be $ba=1$.

## Summary

On a graded algebra with a balanced α-compatible form $\beta$, the left and right multiplications satisfy $(L_a)^{\dagger}=R_a$ and $(R_b)^{\dagger}=L_b$, so the unsigned sandwich has adjoint $(\Sigma_{a,b})^{\dagger}=\Sigma_{b,a}$ and the **signed sandwich** has adjoint

$$
(\Sigma^{\alpha}_{a,b})^{\dagger}=\Sigma^{\alpha}_{\alpha(b),\alpha(a)},
$$

the two elements conjugated by the grade involution and reversed. A signed sandwich is an **isometry** exactly when its two elements are inverse units, so the isometric signed sandwiches are the **signed reflections** $\Sigma^{\alpha}_{a,a^{-1}}$, and every such reflection is **self-adjoint**, because $a\alpha(a)=1$ forces $\alpha(a)=a^{-1}$. With an **element star** ${}^{*}$ compatible with the form, the star form $\beta_{*}(x,y)=\beta(x^{*},y)$ makes $L_a$ have adjoint $L_{a^{*}}$ and the signed sandwich have adjoint $\Sigma^{\alpha}_{a^{*},b^{*}}$; the **unitary elements** are those with $u^{*}u=uu^{*}=1$, and the **unitarity condition** is exactly what makes $\Sigma^{\alpha}_{u,u^{*}}$ an isometry. The endomorphisms of a graded two-dimensional space are the worked case, where $\beta$ is the trace form and the computations are explicit. The analytic theory of unitary operators belongs to a later Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | the base field, of characteristic not two |
| $A=A^0\oplus A^1$ | a finite-dimensional graded algebra |
| $\alpha$ | the grade involution |
| $\beta$ | a balanced α-compatible form |
| $T(x,y)=\operatorname{tr}(L_xL_y)$ | the trace form |
| $S^{\dagger}$ | the adjoint of $S$ with respect to $\beta$ |
| $\Sigma^{\alpha}_{a,b}(x)=a\alpha(x)b$ | the signed sandwich |
| ${}^{*}$ | the element star; $u^{*}u=uu^{*}=1$ the unitarity condition |
| $\beta_{*}(x,y)=\beta(x^{*},y)$ | the star form |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1989), for bilinear forms, adjoints and the trace form.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for signed conjugations and their adjoints.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for algebras with involution and the unitary group.
- Jacques Dixmier, *Enveloping Algebras*, Graduate Studies in Mathematics 11 (American Mathematical Society, 1996), for star structures and unitary elements.
