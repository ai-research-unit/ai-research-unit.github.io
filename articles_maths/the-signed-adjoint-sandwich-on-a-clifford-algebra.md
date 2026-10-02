
# __The Signed Adjoint Sandwich on a Clifford Algebra__

## Introduction

The signed sandwich of a Clifford algebra is the operator $\Sigma^{\alpha}_{a,b}(x)=a\,\alpha(x)\,b$ of *The Signed Sandwich on a Clifford Algebra*, the two-sided multiplication twisted by the grade involution; its geometric rôle is to realise the **reflections** of the quadratic space, $\Sigma^{\alpha}_{u,u^{-1}}=\rho_u$ for a vector $u$ with $q(u)\ne0$. The Clifford algebra carries the **standard form** $\langle x,y\rangle=\operatorname{Sc}(\hat xy)$ of *The Twisted Adjoint on a Clifford Algebra*, and the article computes the adjoint of the signed sandwich for it,

$$
\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{*}=\Sigma^{\alpha}_{\alpha(\hat a),\alpha(\hat b)} ,
$$

the signed sandwich with the two parameters conjugated and their order kept — the reversal is already inside the conjugation, $\widehat{ab}=\hat b\hat a$. From the adjoint and the composition law comes the **isometry criterion**, that a signed sandwich is an isometry exactly when its two parameters are inverse units, so that the isometric signed sandwiches are precisely the **reflections**; and from an element Hermitian conjugation $^{\dagger}$ comes the **unitarity condition** $u^{\dagger}u=uu^{\dagger}=1$, which makes the signed sandwiches $\Sigma^{\alpha}_{u,u^{\dagger}}$ isometric.

**The boundaries.** The signed sandwich, its composition law and its reading on the quadratic space are *The Signed Sandwich on a Clifford Algebra*, *Two-Sided Operators with the Signed Product* and *Reflections as Signed Two-Sided Operators on a Clifford Algebra*; the standard form, the Clifford conjugation $\hat x=\alpha(\tilde x)$ and the adjoints of the one-sided factors are *The Twisted Adjoint on a Clifford Algebra*; the Hermitian conjugation of the elements is *Hermitian Clifford Structures* and *Two-Sided Operators on a Clifford Algebra*. The adjoint of a reflection and of the signed left multiplication are *The Signed Adjoint of the Reflection on a Clifford Algebra* and *The Signed Adjoint of the Left Multiplication on a Clifford Algebra*, the next two entries of the group, and are not anticipated here. The base is a field $F$ of characteristic not $2$, $q$ a non-degenerate quadratic form with $q(u)=B(u,u)$ and $uv+vu=2B(u,v)$.

**A convention.** The operator adjoint of the category is written ${}^{*}$, following *The Twisted Adjoint on a Clifford Algebra*; the element Hermitian conjugation is written ${}^{\dagger}$, following *Two-Sided Operators on a Clifford Algebra* and *Hermitian Clifford Structures*. The two marks are kept apart throughout.

## The Standard Form and the Adjoints

**Definition.** The **standard form** is $\langle x,y\rangle=\operatorname{Sc}(\hat xy)$ with $\hat x=\alpha(\tilde x)$ the Clifford conjugation; it is non-degenerate and bilinear, and the **adjoint** of an operator $A$ is the operator $A^{*}$ with $\langle Ax,y\rangle=\langle x,A^{*}y\rangle$.

**Proposition (quoted).** The adjoints of the one-sided factors and of the grade involution for the standard form are

$$
L_a^{*}=L_{\hat a} , \qquad R_b^{*}=R_{\hat b} , \qquad \alpha^{*}=\alpha ,
$$

so that the ordinary sandwich satisfies $T_{a,b}^{*}=T_{\hat a,\hat b}$ and the left multiplication by a vector is skew-adjoint, $L_u^{*}=-L_u$.

**Proof.** The computation is *The Twisted Adjoint on a Clifford Algebra*: $\langle ax,y\rangle=\operatorname{Sc}(\widehat{ax}y)=\operatorname{Sc}(\hat x\hat ay)=\langle x,\hat ay\rangle$, the right case being identical, and the self-adjointness of $\alpha$ following from $\widehat{\alpha x}=\tilde x$ and the invariance of the scalar part under $\alpha$. The vector value is $\hat u=\alpha(\tilde u)=-u$.

**Theorem.** The adjoint of the signed sandwich is the signed sandwich by the conjugated parameters,

$$
\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{*}=\Sigma^{\alpha}_{\alpha(\hat a),\,\alpha(\hat b)}
=R_{\hat b}\,\alpha\,L_{\hat a} .
$$

**Proof.** The adjoint of a composite is the composite of the adjoints in the reverse order, so $\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{*}=(L_a\alpha R_b)^{*}=R_b^{*}\alpha^{*}L_a^{*}=R_{\hat b}\alpha L_{\hat a}$. Now $R_{\hat b}\alpha=\alpha R_{\alpha(\hat b)}$ and $L_{\alpha(\hat a)}\alpha=\alpha L_{\hat a}$, so the composite is $\alpha R_{\alpha(\hat b)}L_{\hat a}=L_{\alpha(\hat a)}\alpha R_{\alpha(\hat b)}$, which is the signed sandwich by $\alpha(\hat a)$ and $\alpha(\hat b)$ since the left and right multiplications commute.

**Corollary.** The adjoint is an involution of the signed family, $\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{**}=\Sigma^{\alpha}_{a,b}$, and it is the conjugate-linear correspondence of parameters $a\mapsto\alpha(\hat a)$; for a central parameter it reduces to the Clifford conjugation $\hat a=a^{-1}$ for the orthogonal elements of *The Adjoint of the Left Multiplication on a Clifford Algebra*.

## Isometry and the Reflections

**Definition.** An operator $S$ is an **isometry** of the standard form when $S^{*}S=\operatorname{id}$; the isometries form a group.

**Proposition (composition law, quoted).** The composites of the two-sided family are

$$
\Sigma^{\alpha}_{a,b}\Sigma^{\alpha}_{c,d}=\Sigma_{a\alpha(c),\,\alpha(d)b} , \qquad
\Sigma^{\alpha}_{a,b}T_{c,d}=\Sigma^{\alpha}_{a\alpha(c),\,\alpha(d)b} , \qquad
T_{a,b}\Sigma^{\alpha}_{c,d}=\Sigma^{\alpha}_{ac,\,db} ,
$$

so the composite of two signed sandwiches is an **ordinary** sandwich, the two grade involutions cancelling.

**Proof.** The computation is *Two-Sided Operators with the Signed Product*: $\Sigma^{\alpha}_{a,b}\Sigma^{\alpha}_{c,d}(x)=a\alpha(c)\,\alpha(\alpha(x))\,\alpha(d)b=a\alpha(c)\,x\,\alpha(d)b$, the middle twist being the identity.

**Theorem (the isometry criterion).** The signed sandwich $\Sigma^{\alpha}_{a,b}$ is an isometry of the standard form if and only if the products $ba$ and $ab$ are central; in the central-simple case this is equivalent to $b=a^{-1}$, and then the isometric signed sandwiches are exactly the **reflections** $\Sigma^{\alpha}_{a,a^{-1}}$.

**Proof.** By the composition law and the adjoint formula,

$$
\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{*}\Sigma^{\alpha}_{a,b}
=\Sigma^{\alpha}_{\alpha(b),\alpha(a)}\Sigma^{\alpha}_{a,b}
=\Sigma_{\alpha(b)\alpha(a),\,\alpha(b)\alpha(a)}=\Sigma_{c,c} , \qquad c=\alpha(ba) ,
$$

by the composition law, because the two twists cancel; and $\Sigma_{c,c}=\operatorname{id}$ exactly when $c$ is a central unit, by the injectivity of the two-sided correspondence up to the centre recorded in *The Sandwich on a Clifford Algebra*. Hence $ba$ central; the reverse order gives $ab$ central; in the central-simple case both are the conditions $ba=ab=1$, that is $b=a^{-1}$.

**Corollary.** The graded involution $\alpha=\Sigma^{\alpha}_{1,1}$ is an isometry; every reflection $\Sigma^{\alpha}_{u,u^{-1}}=\rho_u$ with $q(u)\ne0$ is an isometry by *The Signed Sandwich on a Clifford Algebra*; and the map $a\mapsto\Sigma^{\alpha}_{a,a^{-1}}$ is the reflection correspondence whose injectivity up to the centre is quoted.

## The Unitarity Condition

**Definition.** Let ${}^{\dagger}$ be the element Hermitian conjugation of *Hermitian Clifford Structures*, an anti-involution with $(xy)^{\dagger}=y^{\dagger}x^{\dagger}$ and $(x^{\dagger})^{\dagger}=x$, compatible with the grade involution in the sense $\alpha(x^{\dagger})=\alpha(x)^{\dagger}$. The **unitary elements** are those with

$$
u^{\dagger}u=uu^{\dagger}=1 ,
$$

and the condition is the **unitarity condition**; the unitary elements form a group $U(\mathrm{Cl},{}^{\dagger})$.

**Proposition.** If $u$ is unitary, the signed sandwich $\Sigma^{\alpha}_{u,u^{\dagger}}$ is an isometry of the standard form, and its adjoint is $\Sigma^{\alpha}_{\alpha(u),\alpha(u^{\dagger})}$; the assignment $u\mapsto\Sigma^{\alpha}_{u,u^{\dagger}}$ carries the unitary group into the isometries of the standard form, with kernel the central unitary elements.

**Proof.** Put $b=u^{\dagger}$. Since $u^{\dagger}=u^{-1}$ by the unitarity condition, the products $ba=u^{\dagger}u=1$ and $ab=uu^{\dagger}=1$ are central and actually trivial, so the isometry criterion applies. The adjoint is the formula of the theorem; the kernel statement is the injectivity up to the centre.

**Remark (the two conditions).** The unitarity condition is a condition on the **elements** and belongs to the involutive layer; the isometry criterion is a condition on the **parameters** of the sandwich, that the two be inverse to within the centre. The two meet in the statement that a unitary element gives an isometric signed sandwich, and they must not be identified: a signed sandwich may be isometric without its parameters being unitary elements for $^{\dagger}$, and a unitary element may give a signed sandwich whose adjoint is not itself.

## Worked Cases

### The Quaternions

For $\mathrm{Cl}\cong\mathbb{H}$ with $e_1^2=e_2^2=-1$, the Clifford conjugation is the quaternionic conjugation, $\hat x=\bar x$, and the signed sandwich $\Sigma^{\alpha}_{a,b}$ is the map $x\mapsto a\alpha(x)b$ with $\alpha$ the identity on the scalars and the negation on the pure part. The unitary elements for the quaternionic conjugation satisfy $u\bar u=1$, the unit sphere, and the signed sandwiches $\Sigma^{\alpha}_{u,\bar u}$ are isometric; the reflections are the $\Sigma^{\alpha}_{u,u^{-1}}$ with $u$ a vector of norm one.

### The Negative-Definite Plane

For the negative-definite plane with $e_1^2=e_2^2=-1$, a vector $u$ has $q(u)<0$ and $\hat u=-u$, so $\Sigma^{\alpha}_{u,-u^{-1}}=\rho_u$ is a reflection and an isometry; the criterion $b=a^{-1}$ is verified by the computation $\alpha(u)\alpha(u^{-1})=\alpha(1)=1$ of the proof, and the isometries so obtained generate the rotation group of the plane.

### The Split Plane

For the split plane with $e_1^2=1$, $e_2^2=-1$, a null vector $u=e_1+e_2\ne0$ has $q(u)=0$ and is not invertible, so the signed sandwich $\Sigma^{\alpha}_{u,u^{-1}}$ does not exist; the operator $\Sigma^{\alpha}_{u,u}$ is defined, and the next entry of the group, *The Signed Adjoint of the Reflection on a Clifford Algebra*, treats the failure.

## Summary

For the standard form $\langle x,y\rangle=\operatorname{Sc}(\hat xy)$ the **adjoint of the signed sandwich** is the signed sandwich by the conjugated parameters,

$$
\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{*}=\Sigma^{\alpha}_{\alpha(\hat a),\alpha(\hat b)} ,
$$

an involution of the signed family. Combined with the composition law $\Sigma^{\alpha}_{a,b}\Sigma^{\alpha}_{c,d}=\Sigma_{a\alpha(c),\alpha(d)b}$, whose composite is an ordinary sandwich, the adjoint gives the **isometry criterion**: $\Sigma^{\alpha}_{a,b}$ is an isometry exactly when $ba$ and $ab$ are central, that is $b=a^{-1}$ in the central-simple case, so the isometric signed sandwiches are precisely the **reflections** $\Sigma^{\alpha}_{a,a^{-1}}$. With an **element Hermitian conjugation** $^{\dagger}$ the **unitarity condition** $u^{\dagger}u=uu^{\dagger}=1$ makes $\Sigma^{\alpha}_{u,u^{\dagger}}$ an isometry, the two conditions living on the elements and on the parameters respectively. The adjoints of the reflection and of the signed left multiplication are the next two entries of the group; the form is *The Twisted Adjoint on a Clifford Algebra*, and the sandwich is *The Signed Sandwich on a Clifford Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle x,y\rangle=\operatorname{Sc}(\hat xy)$ | Standard form; $\hat x=\alpha(\tilde x)$ |
| $\Sigma^{\alpha}_{a,b}(x)=a\alpha(x)b$ | Signed sandwich |
| $L_a^{*}=L_{\hat a}$, $R_b^{*}=R_{\hat b}$, $\alpha^{*}=\alpha$ | Adjoints of the one-sided factors |
| $\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{*}=\Sigma^{\alpha}_{\alpha(\hat a),\alpha(\hat b)}$ | Adjoint of the signed sandwich |
| $\Sigma^{\alpha}_{a,b}\Sigma^{\alpha}_{c,d}=\Sigma_{a\alpha(c),\alpha(d)b}$ | Composition law |
| $ba$, $ab$ central (or $b=a^{-1}$) | Isometry criterion |
| $\Sigma^{\alpha}_{a,a^{-1}}$ | The reflection-shaped isometries |
| $^{\dagger}$ | Element Hermitian conjugation; $u^{\dagger}u=uu^{\dagger}=1$ the unitarity condition |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the signed conjugations, the reflections and the isometries of the standard form.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the Clifford conjugation, the standard form and the explicit low-dimensional adjoints.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for algebras with involution, the unitary group and the unitarity condition.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the reflection operators and their isometry property.
