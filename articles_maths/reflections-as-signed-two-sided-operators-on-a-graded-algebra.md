
# __Reflections as Signed Two-Sided Operators on a Graded Algebra__

## Introduction

A **reflection** of a graded algebra $A$ is a two-sided operator of order two, and the signed sandwiches $\Sigma^{\alpha}_{a,b}(x)=a\alpha(x)b$ of *The Signed Sandwich on a Graded Algebra* supply the natural family of such operators: the signed sandwich $\Sigma^{\alpha}_{a,a^{-1}}$ is an involution exactly when $a\,\alpha(a)=1$, and this is the algebraic form of a reflection. This article reads the reflections of the graded algebra as signed two-sided operators, establishes the **correspondence** between the reflections and the elements $a$ with $a\alpha(a)=1$, measures how far the correspondence is from injective, and separates the nondegenerate cases, in which the correspondence holds, from the **degenerate cases**, in which a signed sandwich fails to be a reflection at all. The graded algebra and the grade involution are *Superalgebras and Graded Structures*; the sandwiches and their composition law are *The Signed Sandwich on a Graded Algebra*, cited throughout; the adjoint of a reflection is deferred to the `- * Operator Theory` group, and the geometric reflections of a quadratic space, which are the model, belong to the symmetric algebras.

The base is a commutative ring $R$ with $1$, $A=A^0\oplus A^1$ is a $\mathbb{Z}/2$-graded associative algebra with grade involution $\alpha$, and the operators are written $\Sigma^{\alpha}_{a,b}$ and $\Sigma_{a,b}$. The article reasons with the ring structure and the grading only.

## Reflections and Their Two Kinds

**Definition.** An operator $S:A\to A$ is a **reflection** when $S\circ S=\mathrm{id}_A$. A reflection is **signed** when it is a signed sandwich, and **unsigned** when it is an unsigned sandwich.

**Proposition.** The grade involution $\alpha=\Sigma^{\alpha}_{1,1}$ is a signed reflection; the inner conjugation $\Sigma_{a,a^{-1}}(x)=axa^{-1}$, defined for a unit $a$, is an automorphism, and it is a reflection exactly when $a^{2}$ is central and $a^{-1}$ acts as $a$ in the conjugation, that is when $\Sigma_{a^{-1},a}=\Sigma_{a,a^{-1}}$.

**Proof.** $\alpha^2=\mathrm{id}$ by definition. The inner conjugation is an automorphism because it is conjugation by a unit; it is an involution exactly when conjugating by $a$ and by $a^{-1}$ agree, which is the displayed condition. $\square$

**Corollary.** The signed reflections and the unsigned reflections are two different families: the first carry the twist of the argument, the second do not, and they meet in the elements fixed by $\alpha$, that is in the even part when the even elements are the only ones used.

## The Correspondence

**Theorem.** Let $\mathrm{R}(A)$ be the set of units $a$ with $a\,\alpha(a)=1$ and let $\mathrm{Ref}^{\alpha}(A)$ be the set of signed sandwiches that are reflections. The map

$$
\Phi:\mathrm{R}(A)\longrightarrow\mathrm{Ref}^{\alpha}(A),\qquad \Phi(a)=\Sigma^{\alpha}_{a,\,a^{-1}},
$$

is well defined, and its image consists of reflections whose square is the identity:

$$
\Sigma^{\alpha}_{a,a^{-1}}\circ\Sigma^{\alpha}_{a,a^{-1}}=\mathrm{id} .
$$

**Proof.** The reflection property is the theorem of *The Signed Sandwich on a Graded Algebra*; the computation is $\Sigma^{\alpha}_{a,a^{-1}}\circ\Sigma^{\alpha}_{a,a^{-1}}=\Sigma^{\alpha}_{a\alpha(a),\,\alpha(a^{-1})a^{-1}}=\Sigma^{\alpha}_{1,1}$. $\square$

**Theorem (injectivity up to the centre).** Two elements $a,c\in\mathrm{R}(A)$ give the same reflection if and only if $c^{-1}a$ lies in the centre of $A$; consequently the correspondence is injective on $\mathrm{R}(A)/\mathrm{Z}(A)^{\times}$.

**Proof.** $\Sigma^{\alpha}_{a,a^{-1}}=\Sigma^{\alpha}_{c,c^{-1}}$ means $a\alpha(x)a^{-1}=c\alpha(x)c^{-1}$ for every $x$, equivalently $(c^{-1}a)\alpha(x)=\alpha(x)(c^{-1}a)$ for every $x$; since $\alpha$ is a bijection the condition is that $c^{-1}a$ commutes with every element, which is centrality. $\square$

**Corollary.** The correspondence is a bijection onto its image when the centre is trivial; the signed reflection $\Sigma^{\alpha}_{a,a^{-1}}$ depends only on the class of $a$ modulo central units, exactly as the inner conjugation depends only on $a$ modulo central units.

**Proposition (composition).** The composite of two signed reflections is a signed sandwich of the same shape,

$$
\Sigma^{\alpha}_{a,a^{-1}}\circ\Sigma^{\alpha}_{b,b^{-1}}=\Sigma^{\alpha}_{c,\,c^{-1}},\qquad c=a\,\alpha(b),
$$

so the signed reflections generate the group of the operators $\Sigma^{\alpha}_{a,a^{-1}}$; the composite need not be an involution, and it is one exactly when $c\alpha(c)=1$.

**Proof.** The composition law of *The Signed Sandwich on a Graded Algebra* gives $\Sigma^{\alpha}_{a\alpha(b),\,\alpha(b^{-1})a^{-1}}$, and $\alpha(b^{-1})a^{-1}=(a\alpha(b))^{-1}$ because $b\in\mathrm{R}(A)$; the composite is an involution exactly when $\Sigma^{\alpha}_{c,c^{-1}}$ is one, which by the reflection theorem of the previous section is the condition $c\alpha(c)=1$. $\square$

## The Degenerate Cases

**Definition.** The correspondence is **nondegenerate** at $a$ when $a$ is a unit with $a\alpha(a)=1$; it is **degenerate** when $a\alpha(a)$ is a non-unit, and **totally degenerate** when $a\alpha(a)=0$.

**Theorem.** The map $\Phi$ fails to be a correspondence in the degenerate cases: if $a\alpha(a)\neq1$ then $\Sigma^{\alpha}_{a,a^{-1}}$ is not a reflection, and if $a\alpha(a)=0$ then

$$
\Sigma^{\alpha}_{a,a^{-1}}\circ\Sigma^{\alpha}_{a,a^{-1}}=0 ,
$$

so the operator is nilpotent of order two and not invertible.

**Proof.** The square is $\Sigma^{\alpha}_{a\alpha(a),\,\alpha(a^{-1})a^{-1}}$ by the composition law; if the product is not the unit the square is not the identity; if $a\alpha(a)=0$ the square is the zero operator. $\square$

**Corollary.** In the exterior algebra $\Lambda^\bullet V$ an odd element $v$ satisfies $\alpha(v)=-v$, so $v\alpha(v)=-v\wedge v=0$: the signed sandwich $\Sigma^{\alpha}_{v,v^{-1}}$ is defined only if $v$ is a unit, which never happens for a nonzero odd element because $v^2=0$; this is the totally degenerate case, and it is why the reflections of the geometric theory need a Clifford algebra, where an odd element can be a unit. The Clifford algebra and its orthogonal group are the model of the symmetric algebras, and nothing of them is used here.

**Remark.** The failure is not a defect of the correspondence but a genuine change of type: as long as the base ring has zero divisors or the graded algebra has nilpotent odd elements, the signed sandwiches of order two exhaust a strictly smaller set of reflections than the invertible ones, and the degenerate sandwiches form a nilpotent family. This is the algebraic statement that a geometric reflection needs a non-isotropic vector.

## Worked Case: The Even Part and the Odd Part

Let $A=A^0\oplus A^1$ be a graded algebra in which some odd element $u$ is a unit with $u\alpha(u)=1$; then $u^2=1$? Not necessarily: $u\alpha(u)=1$ reads $u\cdot(-u)=-u^2=1$ when $u$ is odd, so $u^{2}=-1$ in characteristic not two. Thus an odd signed reflection is an element whose square is $-1$, and the reflection it defines is $\Sigma^{\alpha}_{u,u^{-1}}(x)=u\alpha(x)u^{-1}$, which is the negative of the unsigned conjugation $uxu^{-1}$ on the odd part and equal to it on the even part. For the exterior algebra of a two-dimensional space there is no such odd unit, and every odd signed sandwich is totally degenerate; for a graded algebra in which the odd part is generated by elements of square $-1$, the odd signed reflections exist and are in bijection with the odd units modulo the centre.

**Verified.** The composition law, the reflection property, the injectivity-up-to-the-centre statement and the total degeneracy $\Sigma^{\alpha}_{v,v}=0$ for an odd vector were checked on the exterior algebra of a two-dimensional space and on a graded algebra with an odd unit of square $-1$, by explicit multiplication of basis elements.

## Summary

A **reflection** of a graded algebra is an order-two two-sided operator. The **signed reflections** are the signed sandwiches $\Sigma^{\alpha}_{a,a^{-1}}(x)=a\alpha(x)a^{-1}$, and they are reflections exactly when $a\,\alpha(a)=1$; the grade involution itself is $\Sigma^{\alpha}_{1,1}$, and the unsigned inner conjugation is the other kind of reflection. The map $\Phi(a)=\Sigma^{\alpha}_{a,a^{-1}}$ from the units with $a\alpha(a)=1$ to the signed reflections is well defined and injective modulo central units, its image is closed under composition in the sense that the product of two signed reflections is again a signed sandwich of the same shape with $c=a\alpha(b)$, and the product is an involution only under the stated centrality condition. In the **degenerate cases** the correspondence fails: an element with $a\alpha(a)$ a non-unit gives a non-reflection, an element with $a\alpha(a)=0$ gives a square-zero operator, and in the exterior algebra every nonzero odd element is totally degenerate because $v^2=0$, so the geometric reflections require a Clifford algebra, which is the model of the symmetric algebras and is not used here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | the commutative base ring, $K$ when units are needed |
| $A=A^0\oplus A^1$ | a $\mathbb{Z}/2$-graded associative algebra |
| $\alpha$ | the grade involution |
| $\Sigma^{\alpha}_{a,b}(x)=a\alpha(x)b$ | the signed sandwich |
| $\Sigma_{a,b}(x)=axb$ | the unsigned sandwich |
| $\mathrm{R}(A)=\{a\text{ unit}:a\alpha(a)=1\}$ | the elements defining signed reflections |
| $\Phi(a)=\Sigma^{\alpha}_{a,a^{-1}}$ | the correspondence to the signed reflections |
| $\mathrm{Z}(A)$ | the centre |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1989), for graded algebras and their operators.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for reflections as signed conjugations.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the generation of orthogonal transformations by reflections.
- Larry C. Grove, *Classical Groups and Geometric Algebra*, Graduate Studies in Mathematics 39 (American Mathematical Society, 2002), for the reflection correspondence in the geometric model.
