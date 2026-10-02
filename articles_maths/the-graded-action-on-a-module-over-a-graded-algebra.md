
# __The Graded Action on a Module over a Graded Algebra__

## Introduction

A module over a graded algebra is itself graded, and the action must respect the two gradings: the product of an element of degree $i$ with an element of degree $j$ has degree $i+j$. This article treats the **graded action**: the definition of a graded module over a graded algebra, the parity of the operators the action defines, the requirement that the action be a homomorphism of graded algebras, the **sign rule** that this requirement imposes through the graded commutativity of the algebra, and the form the rule takes when the algebra is a graded Lie algebra, whose bracket enters with the Koszul sign $(-1)^{|a||b|}$. The graded algebra, the parity and the Koszul sign rule are *Superalgebras and Graded Structures*; the signed one-sided and two-sided operators are *The Signed Left Multiplication on a Graded Algebra* and *The Signed Sandwich on a Graded Algebra*; the adjoint version of the action is *The Graded Adjoint Action on a Module over a Graded Algebra* in the `- * Operator Theory` group, deferred here.

The base is a commutative ring $R$ with $1$, $A=A^0\oplus A^1$ is a $\mathbb{Z}/2$-graded associative algebra with grade involution $\alpha$, and $M=M^0\oplus M^1$ is a $\mathbb{Z}/2$-graded $R$-module. The action is written $(a,m)\mapsto a\cdot m$, the endomorphisms of the module by $\operatorname{End}_R(M)$, and the $A$-linear endomorphisms by $\operatorname{End}_A(M)$. The article reasons with the ring structure and the grading only.

## Graded Modules and the Action

**Definition.** A **graded module** over $A$ is a graded $R$-module $M=M^0\oplus M^1$ with an $R$-bilinear action $A\times M\to M$ such that

$$
A^i\cdot M^j\subseteq M^{i+j}\qquad (i,j\in\mathbb{Z}/2),
$$

and $1\cdot m=m$ for a unital algebra. The action is **graded** when it satisfies this degree condition, and $M$ is then a **graded $A$-module**.

**Proposition.** The action is a homomorphism of graded algebras

$$
\rho:A\longrightarrow\operatorname{End}_R(M),\qquad \rho(a)(m)=a\cdot m,
$$

where $\operatorname{End}_R(M)$ is graded by parity, $\operatorname{End}_R(M)^i=\{T:T(M^j)\subseteq M^{i+j}\}$; conversely every such homomorphism defines a graded action.

**Proof.** The two constructions are inverse: $\rho$ is a homomorphism by the module axioms, the degree condition $A^iM^j\subseteq M^{i+j}$ is exactly $\rho(a)(M^j)\subseteq M^{i+j}$, and unitality is $1\cdot m=m$. $\square$

**Definition.** The **annihilator** of $M$ is $\operatorname{Ann}(M)=\{a:a\cdot m=0\text{ for all }m\}$; it is a graded ideal of $A$, and $M$ is **faithful** when it is zero.

**Proposition.** The annihilator is homogeneous: it is the direct sum of its intersections with $A^0$ and $A^1$.

**Proof.** If $a\in\operatorname{Ann}(M)$ with $a=a_0+a_1$ and $a_0,a_1$ homogeneous, then for a homogeneous $m\in M^j$ the equation $a_0\cdot m+a_1\cdot m=0$ splits according to the parity, so $a_0\cdot m=a_1\cdot m=0$; as $m$ is homogeneous this for all $m$ gives $a_0,a_1\in\operatorname{Ann}(M)$. $\square$

## Compatibility with the Grading

**Proposition.** The action of a homogeneous element is a homogeneous operator of the same degree: if $a\in A^i$ then $\rho(a)\in\operatorname{End}_R(M)^i$, so $a\cdot M^j\subseteq M^{i+j}$. In particular the even elements of $A$ act by parity-preserving operators and the odd elements by parity-reversing operators; the action of the even part preserves $M^0$ and $M^1$ separately.

**Proof.** This is the degree condition restated for homogeneous $a$, and the parity of the operators is the same statement read in $\operatorname{End}_R(M)$. $\square$

**Corollary.** If $\rho(a)=0$ for a homogeneous $a$ of degree $i$, then $a\cdot M^j\subseteq M^{i+j}\cap0$, that is, the grading forces the annihilation on the components. The map $\rho$ restricts to a homomorphism $A^0\to\operatorname{End}_R(M)^0$ and sends $A^1$ into $\operatorname{End}_R(M)^1$.

**Proposition (the parity of the operator action).** The action of the grade involution of $A$ is a parity-preserving operator when it is defined; when $A$ has a unit and $\alpha$ is inner, the operator $\rho(\alpha)$ is the conjugation by the parity of the algebra, and it commutes with every $\rho(a)$ up to the sign $(-1)^{|a|}$.

**Proof.** $\rho$ is a homomorphism of algebras, so it carries $\alpha$ to an operator; the sign is the Koszul sign of the graded endomorphism algebra applied to the commutator of $\rho(\alpha)$ with $\rho(a)$. $\square$

## The Sign Rule Imposed by the Action

**Theorem (the sign rule).** Let $A$ be **graded-commutative**, $ab=(-1)^{|a||b|}ba$ for homogeneous $a,b$. Then every graded module over $A$ satisfies the sign rule

$$
a\cdot(b\cdot m)=(-1)^{|a||b|}\,b\cdot(a\cdot m)
\qquad\text{for homogeneous } a,b,m .
$$

**Proof.** By the module axioms $a\cdot(b\cdot m)=(ab)\cdot m$ and $b\cdot(a\cdot m)=(ba)\cdot m$, and the graded commutativity of $A$ equates the two products with the sign; the module axioms then transport the equality to the actions. $\square$

**Corollary.** The action of a graded-commutative algebra is automatically compatible with the sign rule, and no extra hypothesis on the module is needed; the sign is the one forced by the algebra.

**Theorem (the rule for a graded Lie algebra).** Let $\mathrm{G}$ be a graded Lie algebra with bracket of degree zero and graded antisymmetry, $[a,b]=-(-1)^{|a||b|}[b,a]$, and let $M$ be a graded $\mathrm{G}$-module; the action is compatible with the bracket exactly when

$$
a\cdot(b\cdot m)-(-1)^{|a||b|}\,b\cdot(a\cdot m)=[a,b]\cdot m
$$

for homogeneous $a,b,m$.

**Proof.** The displayed relation is the definition of a module over a graded Lie algebra; it is the graded form of the relation that the action of the commutator is the commutator of the actions, and the sign $(-1)^{|a||b|}$ is the Koszul sign of the graded commutator. $\square$

**Corollary.** The adjoint action of *The Adjoint Action of a Lie Algebra* is the case $M=\mathrm{G}$ with $a\cdot m=[a,m]$, and the sign rule above reduces there to the graded Jacobi identity; the reduction is recorded in *Superalgebras and Graded Structures*.

## The Graded Bimodule and the Signed Action

**Proposition.** If $M$ has both a left and a right $A$-action with $(am)b=a(mb)$, then $M$ is a graded $A$-bimodule; the signed left multiplication $\ell_a$ of *The Signed Left Multiplication on a Graded Algebra* gives a right-module example, $\ell_a(m)=a\alpha(m)$, and the signed sandwich is the composite of the two actions.

**Proof.** The bimodule axiom is associativity; the identification of $\ell_a$ with $a\alpha(\cdot)$ and its composition law are the content of the companion article. $\square$

**Corollary.** The signed actions are the operators of a graded module that carry the twist of the argument; the unsigned actions are the ordinary module multiplications, and the two families are related exactly as in the one-sided case.

## Worked Case: The Exterior Algebra as a Module over Itself

Let $A=M=\Lambda^\bullet V$ with the grading modulo two. The left multiplication makes $M$ a graded module over itself, with $A^i\cdot M^j\subseteq M^{i+j}$; the action is graded, the annihilator is zero, and the module is faithful. The sign rule $a\wedge(b\wedge\omega)=(-1)^{|a||b|}b\wedge(a\wedge\omega)$ is the graded commutativity of $\Lambda^\bullet V$. When $A$ is viewed as a graded Lie algebra with the commutator bracket $[a,b]=ab-(-1)^{|a||b|}ba$, the module condition reads $a(b\omega)-(-1)^{|a||b|}b(a\omega)=[a,b]\omega$, which holds because the bracket is the graded commutator and the action is by (graded) multiplication; and the even part $\Lambda^{\mathrm{even}}V$ acts by endomorphisms preserving the parity while the odd part acts by parity-reversing operators.

**Verified.** The degree condition, the sign rule and the bracket relation were checked on the eight homogeneous basis elements of the exterior algebra of a two-dimensional space, by explicit multiplication.

## Summary

A **graded module** $M=M^0\oplus M^1$ over a $\mathbb{Z}/2$-graded algebra $A$ carries an action with $A^iM^j\subseteq M^{i+j}$, equivalently a homomorphism $\rho:A\to\operatorname{End}_R(M)$ of graded algebras. The annihilator is a graded ideal, so its homogeneous parts are the elements acting as zero, and a homogeneous $a$ acts by a homogeneous operator of the same parity: the even elements preserve the parity of $M$, the odd elements reverse it. When the algebra is **graded-commutative** the module inherits the **sign rule** $a(bm)=(-1)^{|a||b|}b(am)$, with no extra hypothesis; when the algebra is a **graded Lie algebra** the compatibility of the action with the bracket is the sign rule $a(bm)-(-1)^{|a||b|}b(am)=[a,b]m$, the graded form of the relation that the action of a commutator is a commutator of actions. The adjoint and the signed one-sided operators are graded actions of this kind, the latter carrying the twist of the argument; the exterior algebra over itself is the worked case, where the sign rule is graded commutativity and the bracket is the graded commutator. The adjoint of the graded action is deferred to the `- * Operator Theory` group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | the commutative base ring |
| $A=A^0\oplus A^1$ | a $\mathbb{Z}/2$-graded associative algebra |
| $M=M^0\oplus M^1$ | a graded $A$-module |
| $A^iM^j\subseteq M^{i+j}$ | the degree compatibility of the action |
| $\rho:A\to\operatorname{End}_R(M)$ | the action as a graded algebra homomorphism |
| $\operatorname{Ann}(M)$ | the graded annihilator |
| $(-1)^{\vert a\vert\vert b\vert}$ | the Koszul sign of the action |
| $[a,b]$ | the graded commutator $ab-(-1)^{\vert a\vert\vert b\vert}ba$ |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1989), for graded modules and the graded tensor product.
- Charles A. Weibel, *An Introduction to Homological Algebra*, Cambridge Studies in Advanced Mathematics 38 (Cambridge University Press, 1994), for graded modules and the sign rule.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for graded actions and their signs.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for modules over a Lie algebra and the Jacobi identity in the module form.
