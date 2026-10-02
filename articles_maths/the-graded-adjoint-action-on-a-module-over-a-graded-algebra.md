
# __The Graded Adjoint Action on a Module over a Graded Algebra__

## Introduction

A graded algebra acts on a graded module by operators that shift the degree; the **adjoint action** is the action carried by the **dual module**, the transpose of the given action with the Koszul sign inserted, and it is the module-level counterpart of the operator adjoint of the preceding entries. For a homogeneous element $x$ of degree $|x|$ and a functional $f$ of degree $|f|$ the adjoint action is

$$
(\rho^{\vee}(x)f)(m)=-(-1)^{|x||f|}\,f(x\cdot m),
$$

the sign $(-1)^{|x||f|}$ being forced by the module axiom; the adjoint action is again a graded action, it preserves the grading in the shifted sense, and it is the action of the **coadjoint** module when the module is the algebra itself under the adjoint action. This article, the eighth and last of the `- * Operator Theory` group of the category, defines the graded dual, constructs the adjoint action, proves that the sign rule is exactly what makes it a graded action, relates it to the operator adjoint through an invariant form, and treats the coadjoint action as the worked case. The graded action and its sign rule are *The Graded Action on a Module over a Graded Algebra*; the module theory is *Modules over an Algebra* and *Representations of Lie Algebras*; the involution enters through *Graded Lie Algebras with an Involution*; the analytic theory of the adjoint of an operator on a Hilbert space belongs to a later Part and is named only.

The base is a field $K$ of characteristic not two, $A$ a $\mathbb{Z}/2$-graded algebra, $M=\bigoplus_i M^i$ a graded left $A$-module with action $x\cdot m=\rho(x)m$ preserving $|x\cdot m|=|x|+|m|$ modulo two, and $M^{\vee}$ the graded dual. All degrees are read modulo two. The article uses the duality pairing and the grading, and forms no length from any form.

## Graded Modules and the Graded Dual

**Definition.** A **graded module** over $A$ is a module $M$ with a decomposition $M=M^0\oplus M^1$ such that $A^i\cdot M^j\subseteq M^{i+j}$; an element of $M^i$ is **homogeneous of degree $i$**, written $|m|=i$.

**Definition.** The **graded dual** $M^{\vee}$ is the graded vector space with $(M^{\vee})^i=(M^i)^{*}$ for each $i$; its elements are the linear functionals, and a functional in $(M^i)^{*}$ has degree $i$.

**Proposition.** The **evaluation pairing** $\langle f,m\rangle=f(m)$ vanishes unless $|f|=|m|$ and is a map of degree zero; it is nondegenerate on each side for a finite-dimensional module, and the shift $M[1]$ with $(M[1])^i=M^{i+1}$ satisfies $(M[1])^{\vee}=M^{\vee}[1]$.

**Proof.** A functional in $(M^i)^{*}$ vanishes on $M^j$ for $j\neq i$ by definition, and eats only the component $M^i$; the equality $i=j$ in $\mathbb{Z}/2$ means $i+j=0$, so the pairing has degree zero; nondegeneracy is the finite-dimensional duality, and the shift statement is the reindexing of the dual. $\square$

**Remark.** The convention taken here grades $(M^{\vee})^i=(M^i)^{*}$ and pairs equal degrees; the opposite convention, $(M^{\vee})^i=(M^{-i})^{*}$, is obtained by the shift and carries the same adjoint action up to that shift.

## The Adjoint Action

**Definition.** Let $\rho$ be a graded action of $A$ on $M$. The **adjoint action** on $M^{\vee}$ is

$$
(\rho^{\vee}(x)f)(m)=-(-1)^{|x||f|}\,f(\rho(x)m)
$$

for homogeneous $x,f$ and every $m$, extended bilinearly.

**Theorem.** Let $\mathrm{G}$ be a graded Lie algebra acting on the graded module $M$. Then the adjoint action is a graded action of $\mathrm{G}$ on $M^{\vee}$: $\rho^{\vee}$ is linear, homogeneous of degree zero, and

$$
\rho^{\vee}([x,y])=\rho^{\vee}(x)\rho^{\vee}(y)-(-1)^{|x||y|}\rho^{\vee}(y)\rho^{\vee}(x)
$$

for homogeneous $x,y$; equivalently the sign $(-1)^{|x||f|}$ is exactly the sign that makes the transpose respect the graded bracket.

**Proof.** For homogeneous $x,y,f,m$, the module axiom $x\cdot(y\cdot m)-(-1)^{|x||y|}y\cdot(x\cdot m)=[x,y]\cdot m$ gives
$$
[\rho^{\vee}(x),\rho^{\vee}(y)]f(m)=(-1)^{|x||f|+|y||f|}\big((-1)^{|x||y|}f(y\cdot x\cdot m)-f(x\cdot y\cdot m)\big)
$$
and
$$
\rho^{\vee}([x,y])f(m)=-(-1)^{(|x|+|y|)|f|}f([x,y]\cdot m)
=(-1)^{|x||f|+|y||f|}\big((-1)^{|x||y|}f(y\cdot x\cdot m)-f(x\cdot y\cdot m)\big);
$$
the two agree, using $(-1)^{(|x|+|y|)|f|}=(-1)^{|x||f|+|y||f|}$ and the bilinearity of the action. $\square$

**Remark (the associative case).** The dual of a graded left module over a graded associative algebra is naturally a graded **right** module, $f\cdot a=\rho(a)^{t}f$; when the algebra carries an element star $a\mapsto a^{*}$, $({}^{*})^{2}=\mathrm{id}$, $(ab)^{*}=b^{*}a^{*}$, the same computation with $a^{*}$ in place of the Lie bracket makes the adjoint action a graded **left** action on $M^{\vee}$, the star supplying the reversal, and the sign rule is unchanged.

**Corollary (the sign rule).** The adjoint action satisfies the **sign rule** : for homogeneous $x,y$,
$$
\rho^{\vee}(x)(\rho^{\vee}(y)f)=(-1)^{|x||y|}\rho^{\vee}(y)(\rho^{\vee}(x)f)+\rho^{\vee}([x,y])f,
$$
so that the adjoint action is graded; without the sign $(-1)^{|x||f|}$ in its definition the transpose would satisfy the ungraded commutator and would not be a graded action.

## Compatibility with the Grading

**Proposition.** The adjoint action preserves the grading in the sense $\rho^{\vee}(x)(M^{\vee})^j\subseteq (M^{\vee})^{i+j}$ for $x\in A^i$; the operator $\rho^{\vee}(x)$ has degree $i$, as does $\rho(x)$; and the two are transposes for the evaluation pairing, $\langle\rho^{\vee}(x)f,m\rangle=-(-1)^{|x||f|}\langle f,\rho(x)m\rangle$.

**Proof.** The action $\rho^{\vee}(x)$ raises the degree of a functional by $|x|$ because $\rho(x)$ raises the degree of an element by $|x|$ and the dual grades are the same; the transpose relation is the definition of $\rho^{\vee}(x)$ read through the pairing. $\square$

**Corollary.** The **grade involution** of $A$ acts on the adjoint action by the sign: if $\alpha$ is the automorphism of $A$ that is $(-1)^i$ on $A^i$, then $\rho^{\vee}(\alpha(x))=(-1)^{|x|}\rho^{\vee}(x)$, so the adjoint action is compatible with the grading exactly through the sign rule.

**Proposition (the invariant pairing).** If $M$ carries a nondegenerate graded form $\beta$ invariant under the action, $\beta(x\cdot m,n)+(-1)^{|x||m|}\beta(m,x\cdot n)=0$, then $\beta$ identifies $M$ with $M^{\vee}$ by $m\mapsto\beta(m,\cdot)$, and under this identification the adjoint action corresponds to the operator adjoint $\rho(x)^{\dagger}$ up to the sign $(-1)^{|x||\cdot|}$; the invariant form makes the module **self-dual**.

**Proof.** The form gives an isomorphism $M\to M^{\vee}$ of graded vector spaces, since it is nondegenerate and homogeneous; transporting $\rho^{\vee}(x)$ gives an operator on $M$ that is $\pm\rho(x)^{\dagger}$ with the sign coming from the graded invariance relation, and the self-duality is the existence of the invariant form. $\square$

**Corollary (the involution).** If $A$ carries an involution $\theta$ whose transport under the duality is isomorphic to the original action, then the module is **$\theta$-self-dual**; the adjoint representation of a Lie algebra with an involution is the model, its self-duality being the isomorphism of *The Adjoint Representation and the Involution*.

## Worked Case: The Coadjoint Action

Let $\mathrm{G}$ be a Lie algebra with the trivial grading, $M=\mathrm{G}$ with the adjoint action $\rho=\operatorname{ad}$. The dual $M^{\vee}=\mathrm{G}^{*}$ with the adjoint action is the **coadjoint action**

$$
\langle\operatorname{ad}^{\vee}(x)f,y\rangle=-\langle f,[x,y]\rangle,
$$

the sign in the general definition becoming the single minus sign of the even case; the coadjoint action is a graded action (the grading is trivial, so the sign rule is void) and its orbits are the coadjoint orbits, named and studied in a later Part.

For a graded (super) Lie algebra the sign is visible: if $x$ is odd and $f$ is odd, then $|x||f|=1$ and $(\rho^{\vee}(x)f)(m)=+f(x\cdot m)$, whereas for $f$ even the sign is $-$; the two cases are the two values of the Koszul sign, and the graded bracket of the super algebra makes the adjoint action graded, as the theorem requires.

For $\mathrm{G}=\mathrm{sl}(2,K)$ with basis $e,h,f$ and the dual basis $e^{*},h^{*},f^{*}$ defined by $\langle e^{*},e\rangle=1=\langle h^{*},h\rangle=\langle f^{*},f\rangle$, the coadjoint action is $\operatorname{ad}^{\vee}(x)=-\operatorname{ad}_x^{t}$, and the invariant form is the Killing form, which identifies the adjoint and coadjoint modules; the self-duality of the adjoint representation is the statement that this identification is an isomorphism of modules, as in *The Adjoint Representation and the Involution*.

**Verified.** The sign rule of the adjoint action was checked on the homogeneous pairs of a two-dimensional super Lie algebra with an odd generator; the coadjoint action $\operatorname{ad}^{\vee}(x)=-\operatorname{ad}_x^{t}$ was checked on the basis of $\mathrm{sl}(2,K)$.

## Summary

The **graded dual** $M^{\vee}$ of a graded module is graded by the duals of the graded pieces, with the evaluation pairing of degree zero. The **adjoint action** $(\rho^{\vee}(x)f)(m)=-(-1)^{|x||f|}f(x\cdot m)$ is a graded action on the dual, and the **sign** $(-1)^{|x||f|}$ is exactly what makes the transpose respect the graded bracket or the graded product; it is the module-level sign rule, matching the graded action of *The Graded Action on a Module over a Graded Algebra*. The adjoint action preserves the grading in the shifted sense, and an invariant nondegenerate graded form identifies the module with its dual, turning the adjoint action into the operator adjoint $\rho(x)^{\dagger}$ up to the sign $(-1)^{|x||\cdot|}$ and making the module self-dual; an involution then makes the module $\theta$-self-dual. The **coadjoint action** $\langle\operatorname{ad}^{\vee}(x)f,y\rangle=-\langle f,[x,y]\rangle$ is the worked case, where the grading is trivial and only the single minus sign survives, and the super case exhibits the two values of the Koszul sign. The analytic theory of the adjoint of an operator on a Hilbert space belongs to a later Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | the base field, of characteristic not two |
| $A=A^0\oplus A^1$ | a graded algebra |
| $M=\bigoplus_i M^i$ | a graded left $A$-module |
| $\rho(x)m=x\cdot m$ | the graded action |
| $M^{\vee}$, $(M^{\vee})^i=(M^i)^{*}$ | the graded dual |
| $\langle f,m\rangle$ | the evaluation pairing of degree zero |
| $\rho^{\vee}(x)f=-(-1)^{|x||f|}f(\rho(x)\cdot)$ | the adjoint action |
| $\beta$ | an invariant graded form giving self-duality |

## Further Reading

- Claude Chevalley and Samuel Eilenberg, "Cohomology theory of Lie groups and Lie algebras", *Transactions of the American Mathematical Society* 63 (1948), 85–124, for the dual module and the coadjoint action.
- V. S. Varadarajan, *Lie Groups, Lie Algebras and Their Representations*, Graduate Texts in Mathematics 102 (Springer, 1984), for the coadjoint representation and self-dual modules.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras*, Chapters 1–3 (Springer, 1989), for graded modules and duality.
- Yuri I. Manin, *Gauge Field Theory and Complex Geometry* (Springer, 2nd ed. 1997), for the Koszul sign in the adjoint action on graded modules.
