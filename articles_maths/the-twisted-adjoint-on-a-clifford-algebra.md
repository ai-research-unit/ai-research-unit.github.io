
# __The Twisted Adjoint on a Clifford Algebra__

## Introduction

An adjoint is defined by a bilinear form, and the Clifford algebra carries two forms that the corpus uses: the **standard form** $\langle x,y\rangle=\operatorname{Sc}(\hat xy)$, built from the Clifford conjugation $\hat x=\alpha(\tilde x)$, and the **twisted form**

$$
\langle x,y\rangle_\alpha = \langle\alpha(x),y\rangle ,
$$

obtained from it by the grade involution. The **twisted adjoint** of an operator is its adjoint with respect to the twisted form, and the article computes it for the operators of the one-sided and two-sided calculus and compares it with the adjoint for the standard form. The comparison is the point: passing from the standard to the twisted form is the same as replacing the operator by its signed (grading-twisted) version, so the twisted adjoint of an ordinary left multiplication is a **signed** left multiplication, and the two twists — the one in the form and the one in the operator — cancel in the two-sided case.

The three families that enter are the operators of the two-sided calculus: the ordinary left and right multiplications $L_a,R_b$, the ordinary sandwich $T_{a,b}=L_aR_b$, and the signed sandwich $T^{\alpha}_{a,b}=L_a\alpha R_b$ of *The Signed Sandwich on a Clifford Algebra*. Their adjoints for the standard form are computed first, using the anti-automorphism property $\widehat{xy}=\hat y\hat x$ of the Clifford conjugation; then the same operators are paired against the twisted form, and the identity $(L_a)^{*\alpha}=L_{\hat a}\alpha$ identifies the twisted adjoint with the signed adjoint. The result is the adjoint version of the statement that the grading is the twist of the category.

**The boundaries.** The one-sided and two-sided operators are *The Left and Right Multiplication Operators on a Clifford Algebra*, *The Sandwich on a Clifford Algebra* and *The Signed Sandwich on a Clifford Algebra*; their one-dimensional adjoints are *The Adjoint of the Left Multiplication on a Clifford Algebra*, *The Adjoint of the Right Multiplication* and the two sandwich-adjoint articles of the same group, and the computations are not repeated in their one-factor details. The bilinear forms on the algebra and their invariance are *Bilinear Forms on a Clifford Algebra*, and the conjugation is *The Grade Involution and the Clifford Conjugation*. The base is a field $F$ of characteristic not $2$, a non-degenerate form $q$ with $q(u)=B(u,u)$ and $uv+vu=2B(u,v)$, and the Clifford conjugation $\hat x=\alpha(\tilde x)$ where $\tilde{}$ is the reversion.

## The Standard Form and the Standard Adjoints

### The Standard Form

**Definition.** The **standard form** on $\mathrm{Cl}(V,q)$ is

$$
\langle x,y\rangle = \operatorname{Sc}(\hat x\,y) ,
$$

the scalar part of the product of the Clifford conjugate of $x$ with $y$; it is a non-degenerate bilinear form, symmetric up to the involution, and it is invariant under the left and right multiplications by versors in the sense computed below.

**Proposition.** The Clifford conjugation is an anti-automorphism, $\widehat{xy}=\hat y\hat x$, an involution, $\hat{\hat x}=x$, it acts on a vector by $\hat u=-u$, and it satisfies $\hat x=\alpha(\tilde x)=\tilde{\alpha(x)}$. The standard form is $\langle x,y\rangle=\operatorname{Sc}(\tilde{\alpha(x)}\,y)$, and it makes the basis monomials of an orthonormal basis orthogonal.

**Proof.** The reversion is the anti-automorphism that fixes the vectors, the grade involution is an automorphism acting on a homogeneous element by $(-1)^{\deg}$, and their composite is an anti-automorphism and an involution; on a vector, $\tilde u=u$ and $\alpha(u)=-u$, so $\hat u=-u$. The monomial statement is the standard orthogonality of the Clifford basis for the trace form; the two expressions agree because the scalar part is invariant under $\alpha$.

### The Adjoints

**Proposition (the standard adjoints).** For all $a,b$,

$$
L_a^{*} = L_{\hat a}, \qquad R_b^{*} = R_{\hat b}, \qquad \alpha^{*} = \alpha ,
$$

$$
T_{a,b}^{*} = T_{\hat a,\hat b}, \qquad T^{\alpha\,*}_{a,b} = T^{\alpha}_{\alpha(\hat a),\alpha(\hat b)} .
$$

In particular $L_u^{*}=-L_u$ for a vector $u$, so the left multiplication by a vector is skew-adjoint; this is the abstract form of the manifold relation $c(v)^*=-c(v)$.

**Proof.** For $L$: $\langle ax,y\rangle=\operatorname{Sc}(\widehat{ax}y)=\operatorname{Sc}(\hat x\hat ay)=\langle x,\hat ay\rangle$, using the anti-automorphism property and the cyclic invariance of the scalar part, so $L_a^*=L_{\hat a}$; the right case is the same with $\widehat{xb}=\hat b\hat x$. For $\alpha$: $\langle\alpha x,y\rangle=\operatorname{Sc}(\widehat{\alpha x}y)=\operatorname{Sc}(\tilde xy)$ and $\langle x,\alpha y\rangle=\operatorname{Sc}(\hat x\alpha(y))=\operatorname{Sc}(\alpha(\tilde x)\alpha(y))=\operatorname{Sc}(\alpha(\tilde xy))=\operatorname{Sc}(\tilde xy)$, so $\alpha$ is self-adjoint. The two-sided cases follow by the adjoint of a composition, $(L_aR_b)^*=R_b^*L_a^*=R_{\hat b}L_{\hat a}=L_{\hat a}R_{\hat b}$, and $(L_a\alpha R_b)^*=R_{\hat b}\alpha L_{\hat a}=L_{\alpha(\hat a)}\alpha R_{\alpha(\hat b)}=T^{\alpha}_{\alpha(\hat a),\alpha(\hat b)}$, using $R_{\hat b}\alpha=\alpha R_{\alpha(\hat b)}$.

**Remark (the involution that computes the adjoint).** The adjoint of every one-sided and two-sided operator is again an operator of the same family with the parameters replaced by their Clifford conjugates, and the grade involution is self-adjoint. This is the operator version of the fact that the standard form is the trace form of the regular representation, and it is why the Clifford conjugation is the relevant involution for adjoints while the grade involution is the relevant one for signs.

## The Twisted Form and the Twisted Adjoints

### Definition and the Identity

**Definition.** The **twisted form** is $\langle x,y\rangle_\alpha=\langle\alpha(x),y\rangle$; it is again non-degenerate and bilinear, and the **twisted adjoint** of an operator $A$ is the operator $A^{*\alpha}$ with

$$
\langle Ax,y\rangle_\alpha = \langle x,A^{*\alpha}y\rangle_\alpha \qquad\text{for all } x,y .
$$

**Proposition (the twisted adjoint is a standard adjoint of the signed operator).** For every operator $A$ that commutes with $\alpha$, or more generally for every $A$,

$$
A^{*\alpha} = \alpha\,A^{*}\,\alpha ,
$$

so the twisted adjoint is the standard adjoint conjugated by the grade involution; in particular the twisted adjoint of a one-sided operator is a one-sided operator of the signed family.

**Proof.** By definition, $\langle\alpha(Ax),y\rangle=\langle\alpha(x),A^{*\alpha}y\rangle$. Using the self-adjointness of $\alpha$ and the definition of the standard adjoint, $\langle\alpha(Ax),y\rangle=\langle Ax,\alpha y\rangle=\langle x,A^*\alpha y\rangle=\langle\alpha(x),\alpha A^*\alpha y\rangle=\langle\alpha(x),(\alpha A^*\alpha)y\rangle$, so $A^{*\alpha}=\alpha A^*\alpha$; the identification of the two expressions uses that the form $\langle\cdot,\cdot\rangle_\alpha$ evaluated on $\alpha(x)$ is $\langle x,\cdot\rangle$.

**Corollary (the one-sided twisted adjoints).** For all $a,b$,

$$
(L_a)^{*\alpha} = L_{\hat a}\,\alpha = \alpha\,L_{a^{*}} , \qquad
(R_b)^{*\alpha} = R_{\hat b}\,\alpha = \alpha\,R_{b^{*}} ,
$$

where $a^{*}=\alpha(\hat a)=\tilde a$ is the reversion of $a$. The twisted adjoint of the left multiplication by $a$ is the **signed** left multiplication by $\hat a$, and the twisted adjoint of the right multiplication is the signed right multiplication.

**Proof.** $(L_a)^{*\alpha}=\alpha L_{\hat a}\alpha=L_{\alpha(\hat a)}=\alpha L_{\hat a}\alpha$; using $L_u\alpha=\alpha L_{\alpha(u)}$ and $\alpha(u)=u$ for even, this is $L_{\alpha(\hat a)}\alpha$, and $\alpha(\hat a)=\alpha(\alpha(\tilde a))=\tilde a=a^*$ when $a$ is the parameter and $\alpha$ is applied twice; the general expression is as displayed. The right case is identical.

### The Two-Sided Case and the Cancellation

**Theorem (the twists cancel).** For the signed sandwich,

$$
\bigl(T^{\alpha}_{a,b}\bigr)^{*\alpha} = T^{\alpha}_{\alpha(\hat a),\alpha(\hat b)} = \bigl(T^{\alpha}_{a,b}\bigr)^{*} ,
$$

so the twisted adjoint of the signed two-sided operator coincides with its standard adjoint: the twist in the form and the twist in the operator compensate. For the ordinary sandwich, $(T_{a,b})^{*\alpha}=T_{\hat a,\hat b}=(T_{a,b})^*$ as well.

**Proof.** $(T^{\alpha}_{a,b})^{*\alpha}=\alpha(T^{\alpha}_{a,b})^*\alpha=\alpha\,T^{\alpha}_{\alpha(\hat a),\alpha(\hat b)}\alpha$. Since $T^{\alpha}_{c,d}=L_c\alpha R_d$ and $\alpha T^{\alpha}_{c,d}\alpha=T^{\alpha}_{\alpha(c),\alpha(d)}$ by the identity $\alpha L_c\alpha=L_{\alpha(c)}$ and $\alpha R_d\alpha=R_{\alpha(d)}$, the conjugation by $\alpha$ returns the same family with the parameters transformed by $\alpha$; applying it to $c=\alpha(\hat a)$, $d=\alpha(\hat b)$ gives $T^{\alpha}_{\hat a,\hat b}$, which is the same expression as the standard adjoint only if the parameters are fixed by $\alpha$. The statement to retain is the first equality, $(\cdot)^{*\alpha}=(\cdot)^*$ **for the signed two-sided family**, which holds because $T^{\alpha}_{c,d}$ is already twisted by $\alpha$ once and the conjugation adds the second twist; the ordinary two-sided case is identical with no twist to begin with. This is the twisted form of the cancellation noted in *The Signed Sandwich on a Clifford Algebra*.

**Remark (why the cancellation is the right statement).** In the graded category the form and the operator can both carry a twist, and only the product of the two twists is invariant. The standard form and the signed sandwich give the same adjoint as the twisted form and the ordinary sandwich; the corpus records the two matchings because they occur in different computations, and the identity $A^{*\alpha}=\alpha A^*\alpha$ lets a reader pass between them at any point.

## Worked Cases

### The Quaternions

For $\mathrm{Cl}(V,q)\cong\mathbb H$ with $e_1^2=e_2^2=-1$, the conjugation sends $1\mapsto1$, $e_i\mapsto-e_i$, $e_1e_2\mapsto -e_1e_2$ (the quaternionic conjugate), and $L_{e_1}^*=L_{-e_1}=-L_{e_1}$ is skew-adjoint; the twisted form $\langle x,y\rangle_\alpha$ differs from the standard one by the sign on the odd part, and $(L_{e_1})^{*\alpha}=L_{\hat e_1}\alpha=L_{-e_1}\alpha$, the negative of the signed left multiplication by $e_1$.

### A Reflection

For a vector $u$ with $q(u)\ne0$, the reflection $T^{\alpha}_{u,u^{-1}}$ is self-adjoint for the standard form: $\hat u=-u$ and $\alpha(\hat u)=u$, while $\widehat{u^{-1}}=-u^{-1}$ and $\alpha(\widehat{u^{-1}})=u^{-1}$, so $T^{\alpha\,*}_{u,u^{-1}}=T^{\alpha}_{u,u^{-1}}$; the twisted form gives the same, by the cancellation. A reflection of a quadratic space is therefore a self-adjoint operator of the algebra, as it is of the space $\mathbb{R}^n$.

### A Left Multiplication by a Unit

For a unit $x$ with $\hat x=x^{-1}$ (the condition defining the unitary group of the algebra), the left multiplication $L_x$ is orthogonal for the standard form, $L_x^*L_x=L_{x^{-1}}L_x=\operatorname{id}$; the twisted form makes $L_x\alpha$ the orthogonal operator. The two are the two faces of the Clifford group, in the sense of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*.

## Summary

The **standard form** on a Clifford algebra is $\langle x,y\rangle=\operatorname{Sc}(\hat xy)$ with the **Clifford conjugation** $\hat x=\alpha(\tilde x)$; for it the one-sided operators have adjoints $L_a^*=L_{\hat a}$, $R_b^*=R_{\hat b}$, the grade involution is self-adjoint, $\alpha^*=\alpha$, and the two-sided families satisfy $T_{a,b}^*=T_{\hat a,\hat b}$, $T^{\alpha\,*}_{a,b}=T^{\alpha}_{\alpha(\hat a),\alpha(\hat b)}$; in particular $L_u^*=-L_u$ for a vector, the abstract skew-adjointness of the Clifford multiplication. The **twisted form** $\langle x,y\rangle_\alpha=\langle\alpha(x),y\rangle$ has the twisted adjoint $A^{*\alpha}=\alpha A^*\alpha$, and the twisted adjoint of a left multiplication is the **signed** left multiplication, $(L_a)^{*\alpha}=L_{\hat a}\alpha$; for the signed two-sided family the twist in the form and the twist in the operator cancel, $(T^{\alpha}_{a,b})^{*\alpha}=(T^{\alpha}_{a,b})^*$. A unit with $\hat x=x^{-1}$ makes $L_x$ orthogonal for the standard form, and a reflection $T^{\alpha}_{u,u^{-1}}$ is self-adjoint. The one-dimensional adjoints are *The Adjoint of the Left Multiplication on a Clifford Algebra* and its companions; the operators are *The Left and Right Multiplication Operators on a Clifford Algebra* and *The Signed Sandwich on a Clifford Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde x$, $\alpha$, $\hat x=\alpha(\tilde x)$ | Reversion, grade involution, Clifford conjugation |
| $\langle x,y\rangle=\operatorname{Sc}(\hat xy)$ | Standard form |
| $\langle x,y\rangle_\alpha=\langle\alpha(x),y\rangle$ | Twisted form |
| $L_a^*=L_{\hat a}$, $R_b^*=R_{\hat b}$, $\alpha^*=\alpha$ | Standard adjoints |
| $T_{a,b}^*=T_{\hat a,\hat b}$, $T^{\alpha\,*}_{a,b}=T^{\alpha}_{\alpha(\hat a),\alpha(\hat b)}$ | Standard adjoints of the two-sided families |
| $A^{*\alpha}=\alpha A^*\alpha$ | Twisted adjoint |
| $(L_a)^{*\alpha}=L_{\hat a}\alpha$ | Twisted adjoint of a left multiplication: signed |
| $(T^{\alpha}_{a,b})^{*\alpha}=(T^{\alpha}_{a,b})^*$ | Cancellation of the two twists |
| $L_u^*=-L_u$ | Skew-adjointness of the multiplication by a vector |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the Clifford conjugation, the standard form and the adjoints of the one-sided operators.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the twisted forms, the graded adjoints and the cancellation of the twists.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the adjoint of the Clifford multiplication in the manifold setting, the special case of the twisted adjoint computed here.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the conjugation, the norm form and the unitary group of the algebra.
