
# __The Adjoint of the Left Multiplication on a Clifford Algebra__

## Introduction

The left multiplication $L_a$ acts on the Clifford algebra by $x\mapsto ax$, and its adjoint for the standard form $\langle x,y\rangle=\operatorname{Sc}(\hat xy)$ is the left multiplication by the Clifford conjugate,

$$
L_a^{*} = L_{\hat a} , \qquad \hat a = \alpha(\tilde a) ,
$$

an operator of the same family with the parameter conjugated. The adjoint therefore defines an involution on the parameters, and its consequences are geometric: the **self-adjoint** left multiplications are those with $\hat a=a$, the **orthogonal** ones are the units $a$ with $\hat aa=1$, and the multiplication by a vector is skew-adjoint, $L_u^*=-L_u$. The article collects these consequences and the corresponding statements for the twisted form of *The Twisted Adjoint on a Clifford Algebra*, on which the article depends for the form and the involution.

**The boundaries.** The operator and its calculus are *The Left and Right Multiplication Operators on a Clifford Algebra*; the form, the Clifford conjugation and the twisted form are *The Twisted Adjoint on a Clifford Algebra*; the right-hand mirror of the article is *The Adjoint of the Right Multiplication*; the two-sided operators are *The Adjoint of the Sandwich* and *The Adjoint of the Two-Sided Multiplication Operator*. The unitary and versor conditions in the geometry of the orthogonal group are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*. The base is a field $F$ of characteristic not $2$ with a non-degenerate $q$, $q(u)=B(u,u)$, $uv+vu=2B(u,v)$.

## The Adjoint and Its Involution

**Theorem.** For every $a\in\mathrm{Cl}(V,q)$ the adjoint of the left multiplication for the standard form is $L_a^*=L_{\hat a}$; the map $a\mapsto\hat a$ is an anti-automorphism and an involution of the algebra, $\widehat{a+b}=\hat a+\hat b$, $\widehat{ab}=\hat b\hat a$, $\hat{\hat a}=a$, and $\hat u=-u$ for a vector $u$.

**Proof.** $\langle ax,y\rangle=\operatorname{Sc}(\widehat{ax}y)=\operatorname{Sc}(\hat x\hat ay)=\langle x,\hat ay\rangle$, using the anti-automorphism property of the conjugation and the cyclic invariance of the scalar part; the involution and anti-automorphism statements are those of the conjugation, and the vector value is $\hat u=\alpha(\tilde u)=-u$. The computation is the one-factor case of *The Twisted Adjoint on a Clifford Algebra*.

**Proposition (self-adjointness).** $L_a$ is self-adjoint, $L_a^*=L_a$, if and only if $\hat a=a$; the elements with $\hat a=a$ form a subspace of the algebra and include the scalars, the unit, and every product of an even number of anticommuting vectors in the definite case.

**Proof.** $L_a^*=L_{\hat a}$ and the left multiplications are faithful, so $L_a^*=L_a$ is equivalent to $\hat a=a$ by *The Left and Right Multiplication Operators on a Clifford Algebra*; the fixed subspace of an involution is a subspace, and the examples are immediate from $\hat u=-u$ and multiplicativity.

**Proposition (orthogonality).** $L_a$ is orthogonal for the standard form, $L_a^*L_a=\operatorname{id}$, if and only if $\hat aa=1$; such $a$ are units. The orthogonal left multiplications form a subgroup of the group of units, containing $\pm1$ and closed under $a\mapsto\hat a$.

**Proof.** $L_a^*L_a=L_{\hat a}L_a=L_{\hat aa}$, and $L_c=\operatorname{id}$ only for $c=1$, so orthogonality is $\hat aa=1$; the condition makes $a$ invertible with $a^{-1}=\hat a$, the set is closed under inversion because $\hat{\hat a}a=1$, and closed under products because $\widehat{ab}ab=\hat b\hat aab$, which is $1$ when $\hat aa=\hat bb=1$ and $\hat b$ commutes with $a$ in the scalar case $1$.

**Remark (the norm).** The quantity $\langle ax,ax\rangle$ is the quadratic form of the algebra transported by left multiplication; the orthogonality condition $\hat aa=1$ is the statement that the conjugation is the inverse, and for a unit vector $u$ with $u^2=q(u)$ it reads $(-u)u=-q(u)=1$, which holds for the negative-definite normalisation $q(u)=-1$. The passage between the two normalisations changes which vectors are orthogonal but not the structure of the statements.

## The Twisted Adjoint

**Proposition.** For the twisted form the adjoint of $L_a$ is the **signed** left multiplication

$$
(L_a)^{*\alpha} = L_{\hat a}\,\alpha ,
$$

as *The Twisted Adjoint on a Clifford Algebra* records; the operator is one-sided signed and differs from the standard adjoint by the grade involution. Consequently a left multiplication is self-adjoint for the twisted form exactly when $L_{\hat a}\alpha=L_a$, that is when $a\alpha(x)=\alpha(x)a$ for all $x$, which holds only for the central scalars in the central-simple case.

**Proof.** The formula is the corollary of the twisted-adjoint identity $A^{*\alpha}=\alpha A^*\alpha$ and the commutation $L_u\alpha=\alpha L_{\alpha(u)}$; the self-adjointness computation reduces to $\hat a=a$ together with $\alpha$ centralising $L_a$, and in a central-simple algebra only central elements $\alpha$-commute with every left multiplication.

## Worked Cases

### The Quaternions

For $\mathrm{Cl}\cong\mathbb H$ with $e_1^2=e_2^2=-1$, the conjugation is the quaternionic conjugate, and $L_{e_1}^*=L_{-e_1}=-L_{e_1}$: the left multiplication by a pure quaternion unit is skew-adjoint. The orthogonal left multiplications are $L_a$ with $\hat aa=|a|^2=1$, the unit sphere, the group of unit quaternions.

### A Unit Vector

For any vector $u$ with $q(u)\ne0$, $L_u^*=L_{-u}=-L_u$, so the multiplication by a vector is always skew-adjoint, independent of the signature; the same computation is the manifold relation $c(v)^*=-c(v)$ of *The Adjoint of the Clifford Multiplication*.

### An Even Element

For $a=e_1e_2$ in the negative-definite plane, $\hat a=(-e_2)(-e_1)=e_2e_1=-e_1e_2=-a$, and $L_a^*=L_{-a}=-L_a$: an even element can be skew-adjoint too. The parity of $a$ does not decide self-adjointness; the involution $\hat{}$ does.

## Summary

For the standard form $\langle x,y\rangle=\operatorname{Sc}(\hat xy)$ the adjoint of the left multiplication is the left multiplication by the **Clifford conjugate**, $L_a^*=L_{\hat a}$ with $\hat a=\alpha(\tilde a)$ an anti-automorphism and an involution acting on a vector by $\hat u=-u$. Hence $L_a$ is **self-adjoint** exactly when $\hat a=a$ and **orthogonal** exactly when $\hat aa=1$, the latter defining the group of orthogonal left multiplications inside the units; the multiplication by a vector is always **skew-adjoint**, $L_u^*=-L_u$. For the twisted form the adjoint is the **signed** left multiplication $(L_a)^{*\alpha}=L_{\hat a}\alpha$, and a left multiplication is self-adjoint for the twisted form only for central scalars in the central-simple case. The operator is *The Left and Right Multiplication Operators on a Clifford Algebra*, the form is *The Twisted Adjoint on a Clifford Algebra*, the mirror article is *The Adjoint of the Right Multiplication*, and the manifold case is *The Adjoint of the Clifford Multiplication*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_a(x)=ax$ | Left multiplication |
| $\hat a=\alpha(\tilde a)$ | Clifford conjugation; anti-automorphism, involution |
| $\langle x,y\rangle=\operatorname{Sc}(\hat xy)$ | Standard form |
| $L_a^*=L_{\hat a}$ | Adjoint of the left multiplication |
| $\hat u=-u$ | Conjugation on a vector; $L_u^*=-L_u$ |
| $\hat a=a$ | Self-adjointness condition |
| $\hat aa=1$ | Orthogonality condition; group of orthogonal left multiplications |
| $(L_a)^{*\alpha}=L_{\hat a}\alpha$ | Twisted adjoint; signed left multiplication |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the
  conjugation, the standard form and the adjoints of the left multiplications.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced
  Mathematics 50 (Cambridge University Press, 1995), for the unitary group of an algebra with involution
  and the orthogonal left multiplications.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for
  the skew-adjointness of the Clifford multiplication, the manifold form of $L_u^*=-L_u$.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2
  (Springer, 1997), for the conjugation, the norm and the group of units preserving it.
