
# __The Signed Adjoint of the Left Multiplication on a Clifford Algebra__

## Introduction

The signed left multiplication of *The Signed Left Multiplication on a Clifford Algebra* is the operator

$$
\mathrm{L}^{\alpha}_a = L_a\circ\alpha , \qquad \mathrm{L}^{\alpha}_a(y)=a\,\alpha(y) ,
$$

the twist being on the argument; it agrees with $L_a$ on the even part of the algebra and equals $-L_a$ there where the argument is odd, and it satisfies the composition law $\mathrm{L}^{\alpha}_a\mathrm{L}^{\alpha}_c=L_{a\alpha(c)}$, whose composite is an ordinary left multiplication. The article computes the adjoint of $\mathrm{L}^{\alpha}_a$ for the standard form $\langle x,y\rangle=\operatorname{Sc}(\hat xy)$. The answer is that the adjoint **stays inside the signed family**,

$$
\bigl(\mathrm{L}^{\alpha}_a\bigr)^{*}=\mathrm{L}^{\alpha}_{\alpha(\hat a)} ,
$$

the parameter replaced by its grade-twisted Clifford conjugate; the involution of parameters is therefore $a\mapsto\alpha(\hat a)$, the self-adjoint members are those with $\alpha(\hat a)=a$, and the isometric members satisfy the same condition $\hat aa=1$ as for the ordinary left multiplication — the signed and the ordinary left multiplication are isometric simultaneously. For the **twisted form** the adjoint is $\mathrm{L}^{\alpha}_{\hat a}$, the parameter conjugated by the Clifford conjugation alone.

**The boundaries.** The signed left multiplication, its composition law and the disambiguation of the two twists are *The Signed Left Multiplication on a Clifford Algebra*; the ordinary adjoints $L_a^*=L_{\hat a}$ and the Clifford conjugation $\hat x=\alpha(\tilde x)$ are *The Adjoint of the Left Multiplication on a Clifford Algebra*; the twisted form and the identity $(A^{*\alpha})=\alpha A^*\alpha$ are the latter; the signed sandwich, of which $\mathrm{L}^{\alpha}_a$ is the left factor, is *The Signed Sandwich on a Clifford Algebra* and *The Signed Adjoint Sandwich on a Clifford Algebra*. The parameter-twisted family $\Lambda^{\alpha}_x(y)=\alpha(x)y$ of *The Graded Multiplication Operators* is a different operator and is not treated. The base is a field $F$ of characteristic not $2$, $q$ a non-degenerate quadratic form with $q(u)=B(u,u)$ and $uv+vu=2B(u,v)$.

## The Adjoint and Its Involution

**Theorem.** For the standard form the adjoint of the signed left multiplication is the signed left multiplication by the twisted conjugate,

$$
\bigl(\mathrm{L}^{\alpha}_a\bigr)^{*}=\alpha\,L_{\hat a}=\mathrm{L}^{\alpha}_{\alpha(\hat a)} .
$$

The map $a\mapsto\alpha(\hat a)$ is an anti-automorphism and an involution of the algebra, it is the composite $\alpha\circ\hat{}$ of the grade involution with the Clifford conjugation, on a vector it acts by $\alpha(\hat u)=\alpha(-u)=u$, and the adjoint correspondence is an involution of the signed family.

**Proof.** By definition $\mathrm{L}^{\alpha}_a=L_a\alpha$, so $(\mathrm{L}^{\alpha}_a)^*=\alpha^*L_a^*=\alpha L_{\hat a}$, using the adjoints $L_a^*=L_{\hat a}$ and $\alpha^*=\alpha$ of *The Adjoint of the Left Multiplication on a Clifford Algebra*. Now $\alpha L_{\hat a}(y)=\alpha(\hat ay)=\alpha(\hat a)\alpha(y)$, so $\alpha L_{\hat a}=\mathrm{L}^{\alpha}_{\alpha(\hat a)}$. The statements about $a\mapsto\alpha(\hat a)$ are those of the two anti-involutions: $\widehat{\alpha(ab)}=\widehat{\alpha(a)\alpha(b)}=\alpha(b)\alpha(a)=\alpha(\hat b)\alpha(\hat a)$, and $\alpha(\hat{\alpha(\hat a)})=\alpha(\alpha(\hat a))=\hat a$. On a vector, $\hat u=-u$ and $\alpha(-u)=u$.

**Corollary.** The adjoint of the ordinary left multiplication is ordinary, $L_a^*=L_{\hat a}$, while the adjoint of the signed left multiplication is signed; the two families are each stable under the adjoint correspondence, and the involutions of the parameters are $\hat{}$ and $\alpha(\hat{})$ respectively.

## Self-Adjoint Operators and Isometries

**Proposition (self-adjointness).** The signed left multiplication $\mathrm{L}^{\alpha}_a$ is self-adjoint exactly when $\alpha(\hat a)=a$. The elements with $\alpha(\hat a)=a$ form a subspace of the algebra, they include the scalars and the unit, and a vector $u$ satisfies the condition because $\alpha(\hat u)=u$: **the signed left multiplication by a vector is always self-adjoint**, in contrast with the skew-adjointness $L_u^*=-L_u$ of the ordinary left multiplication.

**Proof.** $\bigl(\mathrm{L}^{\alpha}_a\bigr)^{*}=\mathrm{L}^{\alpha}_{\alpha(\hat a)}$, and the signed left multiplications are faithful, so self-adjointness is $\alpha(\hat a)=a$; the fixed set of an involution is a subspace; the vector case is the computation $\alpha(\hat u)=\alpha(-u)=u$ above.

**Proposition (isometry).** The signed left multiplication is an isometry of the standard form,

$$
\bigl(\mathrm{L}^{\alpha}_a\bigr)^{*}\mathrm{L}^{\alpha}_a=\operatorname{id} ,
$$

if and only if $\hat aa=1$; the condition is the same as the orthogonality condition of the ordinary left multiplication $L_a$, so the signed and the ordinary multiplication by $a$ are isometric simultaneously, and the isometric elements form a subgroup of the units containing $\pm1$ and closed under $a\mapsto\hat a$.

**Proof.** Using the adjoint and the composition law of the signed family,

$$
\bigl(\mathrm{L}^{\alpha}_a\bigr)^{*}\mathrm{L}^{\alpha}_a
=\mathrm{L}^{\alpha}_{\alpha(\hat a)}\mathrm{L}^{\alpha}_a
=L_{\alpha(\hat a)\alpha(a)}=L_{\alpha(\hat a\,a)} ,
$$

which equals the identity exactly when $\alpha(\hat aa)=1$, that is $\hat aa=1$; the group statements are those of *The Adjoint of the Left Multiplication on a Clifford Algebra*.

**Remark (the two conditions are different).** Self-adjointness is $\alpha(\hat a)=a$ and isometry is $\hat aa=1$; neither implies the other, and they coincide only for the elements with $a^{2}=1$ and $\hat a=a$. The parity of $a$ does not decide either condition; the involution $\alpha(\hat{})$ decides self-adjointness and the conjugation $\hat{}$ decides isometry.

## The Twisted Form and the Second Adjoint

**Definition.** The **twisted form** is $\langle x,y\rangle_\alpha=\langle\alpha(x),y\rangle$, and the **twisted adjoint** $A^{*\alpha}$ is the adjoint for it; the identity $A^{*\alpha}=\alpha A^*\alpha$ holds by definition of the signed adjoint.

**Proposition.** For the twisted form the adjoint of the signed left multiplication is the signed left multiplication by the Clifford conjugate,

$$
\bigl(\mathrm{L}^{\alpha}_a\bigr)^{*\alpha}=\alpha\bigl(\mathrm{L}^{\alpha}_a\bigr)^{*}\alpha
=\alpha\bigl(\alpha L_{\hat a}\bigr)\alpha=L_{\hat a}\alpha=\mathrm{L}^{\alpha}_{\hat a} ,
$$

so for the twisted form the parameter involution is the Clifford conjugation $\hat{}$ alone, and the twisted adjoint of the signed family is the signed family with the parameter conjugated. In particular the twisted self-adjointness of $\mathrm{L}^{\alpha}_a$ is $\hat a=a$, and its twisted isometry is again $\hat aa=1$.

**Proof.** Substitute the standard adjoint and cancel the two grade involutions, $\alpha\gamma=\gamma\alpha$ for $\gamma=\alpha$; the composition $L_{\hat a}\alpha=\mathrm{L}^{\alpha}_{\hat a}$ is the definition of the signed family; the conditions are read off as before.

**Remark (the meaning of the two displays).** The standard form pairs the signed family with the twisted conjugate and the twisted form with the conjugate; the difference is exactly the twist which defines the form, and it is the operator-level form of the statement that the grading is the twist of the category. In the notation of the graded-algebra article of the category, the same computation reads $(\Sigma^{\alpha}_{a,b})^{*}=\Sigma^{\alpha}_{\alpha(\hat a),\alpha(\hat b)}$ with the right factor absent.

## Relation to the Signed Sandwich

**Proposition.** The signed sandwich factors as $\Sigma^{\alpha}_{a,b}=\mathrm{L}^{\alpha}_a\,R_b$, and the adjoint of the factor is a factor of the adjoint,

$$
\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{*}=\bigl(\mathrm{L}^{\alpha}_a\bigr)^{*}R_b^{*} = \mathrm{L}^{\alpha}_{\alpha(\hat a)}R_{\hat b} ,
$$

which is the decomposition of the signed-sandwich adjoint $\Sigma^{\alpha}_{\alpha(\hat a),\alpha(\hat b)}$ into its two factors; in particular the self-adjointness of the left factor is the special case $\alpha(\hat a)=a$ of the left parameter of a self-adjoint sandwich.

**Proof.** The sandwich is the composite of the signed left multiplication with the ordinary right multiplication, and the adjoint of a composite is the composite of the adjoints in the reverse order; the right multiplications commute with the left ones, so the product of the two adjoints is the signed sandwich with the two parameters as displayed, matching *The Signed Adjoint Sandwich on a Clifford Algebra*.

## Worked Cases

### A Vector

For a vector $u$ the twisted conjugate is $\alpha(\hat u)=u$, so $(\mathrm{L}^{\alpha}_u)^{*}=\mathrm{L}^{\alpha}_u$: the signed left multiplication by a vector is **self-adjoint**. It is an isometry exactly when $\hat uu=-u^2=-q(u)=1$, that is $q(u)=-1$; in the negative-definite normalisation every unit vector gives a self-adjoint isometry.

### The Quaternions

For $\mathrm{Cl}\cong\mathbb{H}$ with $e_1^2=e_2^2=-1$ and the quaternionic conjugation $\hat x=\bar x$, the twisted conjugate of a pure quaternion $a$ is $\alpha(\hat a)=\alpha(\bar a)=-\bar a=-a^{-1}$, so $(\mathrm{L}^{\alpha}_a)^{*}=\mathrm{L}^{\alpha}_{-a^{-1}}$; a pure unit quaternion has $a^{-1}=-a$, hence $\alpha(\hat a)=a$ and $\mathrm{L}^{\alpha}_a$ is self-adjoint.

### An Even Element

For an even element $a$ one has $\alpha(a)=a$ and $\alpha(\hat a)=\hat a$, so the standard adjoint of $\mathrm{L}^{\alpha}_a$ is $\mathrm{L}^{\alpha}_{\hat a}$ and self-adjointness is $\hat a=a$; for $a=e_1e_2$ in the negative-definite plane, $\hat a=-e_1e_2=-a$ and the signed left multiplication is not self-adjoint, while it is an isometry exactly when $\hat aa=-a^2=1$.

## Summary

For the standard form the **adjoint of the signed left multiplication** is the signed left multiplication by the twisted conjugate,

$$
\bigl(\mathrm{L}^{\alpha}_a\bigr)^{*}=\mathrm{L}^{\alpha}_{\alpha(\hat a)} , \qquad \hat a=\alpha(\tilde a) ,
$$

so the adjoint stays inside the signed family and its parameter involution is $a\mapsto\alpha(\hat a)$. The operator is **self-adjoint** exactly when $\alpha(\hat a)=a$ — a condition met by every vector — and it is an **isometry** exactly when $\hat aa=1$, the same condition as for the ordinary left multiplication $L_a$, so signedness does not change the orthogonal elements. For the **twisted form** the adjoint is $\mathrm{L}^{\alpha}_{\hat a}$, the parameter conjugated by $\hat{}$, the two twists of the form and of the operator cancelling; and the factorisation $\Sigma^{\alpha}_{a,b}=\mathrm{L}^{\alpha}_aR_b$ makes the adjoint of the signed sandwich the product of the adjoints of its factors, matching *The Signed Adjoint Sandwich on a Clifford Algebra*. The ordinary adjoint is *The Adjoint of the Left Multiplication on a Clifford Algebra*, the disambiguation of the twists is *The Signed Left Multiplication on a Clifford Algebra*, and the module-level story is *The Graded Adjoint Action on a Module over a Clifford Algebra*, the last entry of the group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{L}^{\alpha}_a=L_a\alpha$, $\mathrm{L}^{\alpha}_a(y)=a\alpha(y)$ | Signed left multiplication; argument twist |
| $\mathrm{L}^{\alpha}_a\mathrm{L}^{\alpha}_c=L_{a\alpha(c)}$ | Composition law |
| $\hat a=\alpha(\tilde a)$ | Clifford conjugation |
| $a\mapsto\alpha(\hat a)$ | Twisted conjugate; parameter involution of the adjoint |
| $\bigl(\mathrm{L}^{\alpha}_a\bigr)^{*}=\mathrm{L}^{\alpha}_{\alpha(\hat a)}$ | Standard adjoint |
| $\alpha(\hat a)=a$ | Self-adjointness; automatic for a vector |
| $\hat aa=1$ | Isometry; shared with the ordinary left multiplication |
| $\bigl(\mathrm{L}^{\alpha}_a\bigr)^{*\alpha}=\mathrm{L}^{\alpha}_{\hat a}$ | Twisted-form adjoint |
| $\Sigma^{\alpha}_{a,b}=\mathrm{L}^{\alpha}_aR_b$ | Signed sandwich; factorisation |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the signed multiplications, the conjugations and their adjoints in the low-dimensional cases.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the twisted conjugation and the groups defined by the isometry conditions.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the signed Clifford multiplication and its self-adjointness up to sign.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the graded structure of the Clifford algebra and the two conjugations.
