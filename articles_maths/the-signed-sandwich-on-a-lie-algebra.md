
# __The Signed Sandwich on a Lie Algebra__

## Introduction

The **sandwich** of an associative algebra is the operator $x\mapsto axb$, and the **signed sandwich** is the same operator with the grade involution inserted, $x\mapsto a\,\alpha(x)\,b$. A Lie algebra has no associative product, so the sandwich is read through its only product, the bracket: the left multiplication by $a$ is the operator $\operatorname{ad}_a$, the right multiplication by $b$ is the operator $x\mapsto[x,b]$, and the sandwich is their composite $x\mapsto[a,[x,b]]$. Inserting the grade involution gives the signed sandwich of the Lie algebra, and the pair of parameters then behaves under the involution and under composition as the associative case does, with the reflections of the group becoming visible as the signed conjugations.

This article treats the signed sandwich on a Lie algebra: the operator $x\mapsto a\,\alpha(x)\,b$ read with the bracket, the reflections it realises, and its relation to the unsigned sandwich. It is the fifth article of the `- Operator Theory` group of the category; the unsigned left and right multiplications are from *Operators on a Lie Group* and *The Adjoint Action of a Lie Algebra*, the grade involution and the grading are *Graded Lie Algebras and Lie Superalgebras* and *Graded Lie Algebras with an Involution*, the reflections are *Reflections as Signed Two-Sided Operators on a Lie Algebra*, below, and the adjoint of the operator is *The Signed Adjoint Sandwich on a Lie Algebra* of the `- * Operator Theory` group, below in the category.

The article assumes the Lie algebra and its bracket from *Lie Groups* and *The Lie Algebra and the Exponential Map*, the adjoint representation and the derivation $\operatorname{ad}_X$ from *The Lie Correspondence and the Adjoint Representation*, the universal enveloping algebra and its PBW theorem from *Universal Enveloping Algebras*, the grading and the grade involution from *Graded Lie Algebras with an Involution* and *Graded Lie Algebras and Lie Superalgebras*, and the associative sandwich and its laws from *The Signed Sandwich on an Algebra* and *The Signed Sandwich on a Graded Algebra*. The Lie algebra is used with its adjoint action throughout; the associative sandwich is cited as the model that the Lie-algebraic case imitates through the bracket, and no new structure is imported from it.

## The Conventions

### The Two Products of the Lie Algebra

**Definition.** Let $\mathrm{G}$ be a Lie algebra over a field $k$ of characteristic different from $2$, and let $\alpha$ be its **grade involution**, the involutive automorphism of the grading $\mathrm{G} = \mathrm{G}^{+}\oplus\mathrm{G}^{-}$ that is $+\mathrm{id}$ on the even part and $-\mathrm{id}$ on the odd part.

**Definition.** The **left multiplication** by $a\in\mathrm{G}$ and the **right multiplication** by $b\in\mathrm{G}$ are the endomorphisms

$$
L_a(x) = [a,x], \qquad R_b(x) = [x,b] = -\operatorname{ad}_b(x) ,
$$

so that $L_a = \operatorname{ad}_a$, $R_b = -\operatorname{ad}_b$ and $L_a - R_a = \operatorname{ad}_a$; the two families coincide up to the sign, which is the antisymmetry $[a,x] = -[x,a]$ of the bracket.

**Proposition.** The left and right multiplications are derivations of the Lie algebra,

$$
L_a[x,y] = [L_ax,y] + [x,L_ay], \qquad R_b[x,y] = [R_bx,y] + [x,R_by] ,
$$

and they are related by $[L_a, R_b] = R_{[a,b]}$ and $[L_a,L_b] = L_{[a,b]}$, $[R_a,R_b] = -R_{[a,b]}$; the sum over both families is the adjoint action of the algebra on itself.

*Proof.* The derivation property is the Jacobi identity; the commutation relations are the same identity read on the operators, and the signs record the antisymmetry of the bracket.

### The Sandwich

**Definition.** The **unsigned sandwich** by the pair $(a,b)$ is the composite

$$
\Sigma_{a,b} = L_aR_b, \qquad \Sigma_{a,b}(x) = [a,[x,b]] ,
$$

and the **signed sandwich** is

$$
\Sigma^{\alpha}_{a,b} = L_aR_b\alpha = \Sigma_{a,b}\alpha, \qquad \Sigma^{\alpha}_{a,b}(x) = [a,[\alpha(x),b]] .
$$

The pair $(a,b)$ is the **carrying pair**, and the operator depends on it and not only on the product $[a,b]$, since the left and the right multiplications do not commute.

**Remark.** The sandwich is the Lie-algebraic reading of the associative operator $x\mapsto axb$: the identity that separates them is the antisymmetry of the bracket, under which $R_b = -\operatorname{ad}_b$ and the sandwich becomes a double bracket, $\Sigma_{a,b}(x) = \operatorname{ad}_a\operatorname{ad}_b(-\mathrm{id})(x)$; the signed sandwich is the same with the insertion of $\alpha$. Every statement of the present article reduces to a statement about the adjoint action, and the reader may keep the associative picture as a guide.

## The Elementary Laws

### The Factorisations

**Proposition (the two factorisations of the signed sandwich).** The signed sandwich factors through the grade involution in two ways,

$$
\Sigma^{\alpha}_{a,b} = \Sigma_{a,b}\,\alpha = \alpha\,\Sigma_{\alpha(a),\alpha(b)} ,
$$

and the second identity uses that $\alpha$ is an automorphism of the bracket, $\alpha([u,v]) = [\alpha(u),\alpha(v)]$.

*Proof.* The first identity is the definition; the second is the computation

$$
\alpha\Sigma_{\alpha(a),\alpha(b)}(x) = \alpha[\alpha(a),[\alpha(x),\alpha(b)]] = [a,[x,b]]\alpha(x) ,
$$

which is $\Sigma_{a,b}(\alpha(x))$; hence the two operators agree on every $x$.

**Corollary.** The signed sandwich is the unsigned sandwich of the pair $(\alpha(a),\alpha(b))$ conjugated by $\alpha$, and when $\alpha$ is the identity it is the unsigned sandwich itself; the involution therefore acts on the parameter pair by the grading and not on the operator.

*Proof.* The corollary is the second factorisation read as an identity of operators, with the case $\alpha = \mathrm{id}$ immediate.

### The Composition and the Square

**Proposition.** The composite of two signed sandwiches is

$$
\Sigma^{\alpha}_{a,b}\,\Sigma^{\alpha}_{c,d} = \Sigma_{a,b}\,\alpha\,\Sigma_{c,d}\,\alpha = \Sigma_{a,b}\,\Sigma_{\alpha(c),\alpha(d)}\,\alpha^{2} ,
$$

and since $\alpha^{2} = \mathrm{id}$ it is the composite of two unsigned sandwiches; the composite of two unsigned sandwiches is generally not a sandwich, and the family of the sandwiches is closed under composition only in the associative model.

*Proof.* The computation uses the factorisation $\Sigma^{\alpha}_{c,d} = \alpha\Sigma_{\alpha(c),\alpha(d)}$ and $\alpha^2 = \mathrm{id}$, together with the fact that $\alpha$ commutes with the left and right multiplications up to the change of parameters: $\alpha L_c = L_{\alpha(c)}\alpha$, $\alpha R_d = R_{\alpha(d)}\alpha$. The last assertion is the statement that the product of two double brackets has four brackets and is not a double bracket.

**Definition.** The **square** of a signed sandwich is $\Sigma^{\alpha}_{a,b}\Sigma^{\alpha}_{a,b}$, and the sandwich is an **involution** when this square is the identity.

**Theorem (the square).** The square of the signed sandwich is

$$
\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{2} = \Sigma_{a,b}\,\Sigma_{\alpha(a),\alpha(b)} ,
$$

and it is the unsigned sandwich of the pair $(a,b)$ composed with that of the pair $(\alpha(a),\alpha(b))$; in the associative model the corresponding square is the sandwich by the product of the two carrying elements, and the Lie-algebraic computation does not in general collapse to a single sandwich.

*Proof.* The computation is the previous composition law with $(c,d) = (a,b)$; the absence of a collapse is the absence of associativity in the Lie algebra, and the reduction to a single sandwich is available only in the enveloping algebra, where the carrying elements multiply.

## The Reflections Realised

### The Signed Conjugation

**Definition.** The **signed conjugation** by $a$ is the signed two-sided operator

$$
\rho_a = \operatorname{Ad}_{\exp a}\circ\alpha , \qquad \rho_a(x) = \operatorname{Ad}_{\exp a}\bigl(\alpha(x)\bigr) ,
$$

where $\operatorname{Ad}_{\exp a} = e^{\operatorname{ad}_a}$ is the inner automorphism of the algebra determined by the group element $\exp a$; it is the Lie-algebraic form of the associative conjugation $x\mapsto a\alpha(x)a^{-1}$.

**Theorem.** The square of the signed conjugation is the inner automorphism of the element $a + \alpha(a)$,

$$
\rho_a^{2} = \operatorname{Ad}_{\exp(a+\alpha(a))} = e^{\operatorname{ad}_{a+\alpha(a)}} ,
$$

and it is an involution of the algebra exactly when $a+\alpha(a)$ is central.

*Proof.* The square is $\operatorname{Ad}_{\exp a}\alpha\operatorname{Ad}_{\exp a}\alpha = \operatorname{Ad}_{\exp a}\operatorname{Ad}_{\exp\alpha(a)} = \operatorname{Ad}_{\exp(a+\alpha(a))}$, because $\alpha$ commutes with the adjoint action up to the action on the parameter; the inner automorphism of an element is the identity exactly when the element is central in the connected group, which is the condition $[a+\alpha(a),\mathrm{G}] = 0$.

### The Relation to the Sandwich

**Theorem.** In the enveloping algebra $U(\mathrm{G})$ the signed sandwich by the pair of a unit $u$ and its inverse $u^{-1}$ is the signed conjugation,

$$
\Sigma^{\alpha}_{u,u^{-1}}(x) = u\,\alpha(x)\,u^{-1} = \rho_u(x) ,
$$

and on the Lie algebra the restriction of this operator to $\mathrm{G}$ is the signed conjugation by $\exp a$ when $u = \exp a$. Hence the pair of a unit and its inverse is the carrying pair of a reflection, and the reflections of the next article are the signed sandwiches whose carrying pair is inverse.

*Proof.* In the enveloping algebra the signed sandwich is $\Sigma^{\alpha}_{u,v}(x) = u\alpha(x)v$, and with $v = u^{-1}$ it is $u\alpha(x)u^{-1} = \rho_u$; the group element $\exp a$ acts on $\mathrm{G}$ through the adjoint representation $\operatorname{Ad}_{\exp a} = e^{\operatorname{ad}_a}$, so the restriction to the algebra is the signed conjugation. The infinitesimal form of the family at $u = e$ is the signed left multiplication, computed in the next article.

**Corollary.** The signed sandwich realises the reflections when the carrying pair is a pair of inverses in the enveloping algebra, and the signed conjugation by $\exp a$ is the case $u = \exp a$; this is why the reflections of the next article are the signed two-sided operators attached to the elements and not to arbitrary pairs.

*Proof.* The corollary restates the theorem; the identification of the reflections of the next article with the signed conjugations is made there.

## The Degenerate Cases

### The Inner Grade Involution

**Proposition.** If the grade involution is inner, $\alpha = \operatorname{Ad}_w$ for some $w$ in the connected group, then the signed sandwich is an unsigned sandwich conjugated by the inner automorphism,

$$
\Sigma^{\alpha}_{a,b} = \operatorname{Ad}_w\,\Sigma_{\operatorname{Ad}_{w^{-1}}a,\operatorname{Ad}_{w^{-1}}b} ,
$$

and it is the composite of two unsigned sandwiches; the sign therefore produces no new operator, and the reflections of the next article collapse to the inner automorphisms.

*Proof.* Substitute $\alpha = \operatorname{Ad}_w$ in the factorisation and move $\operatorname{Ad}_w$ past the two multiplications using $\operatorname{Ad}_w\operatorname{ad}_x = \operatorname{ad}_{\operatorname{Ad}_w x}\operatorname{Ad}_w$; the resulting operator is the unsigned sandwich with the parameters transformed by $\operatorname{Ad}_{w^{-1}}$, conjugated by $w$. The collapse of the reflections is immediate from $\alpha = \operatorname{Ad}_w$.

### The Abelian Lie Algebra

**Proposition.** If $\mathrm{G}$ is abelian then every sandwich is zero, $\Sigma_{a,b} = 0$, since the bracket vanishes; the signed sandwich is zero as well and the construction degenerates entirely. The sandwich measures the non-commutativity of the algebra, and on a central element either of the two products is the zero operator.

*Proof.* Immediate from the definition; the bracket of an abelian algebra is zero, and the composite of zero multiplications is zero.

### The Central Pair

**Proposition.** If $b$ is central, then $R_b = 0$ and the unsigned sandwich is zero, while the signed sandwich is $L_a\alpha$ followed by $R_b$ and is zero; if $a$ is central, $L_a = 0$ and again the signed sandwich is zero. The sandwich therefore depends on both parameters being non-central, and the carrying elements of the next article are constrained accordingly.

*Proof.* The centrality of $b$ makes $[x,b] = 0$ for every $x$, and the centrality of $a$ makes $[a,y] = 0$; the two claims follow.

## Examples

### The Orthogonal Algebra

Let $\mathrm{G} = \mathrm{so}(3)$ with the basis $E_1,E_2,E_3$ and $[E_i,E_j] = \varepsilon_{ijk}E_k$. The sandwich by the pair $(E_1,E_2)$ is $\Sigma_{E_1,E_2}(x) = [E_1,[x,E_2]]$, which on the basis is computed from the structure constants; the operator is a rank-two endomorphism, and it is the Lie-algebraic form of the corresponding matrix sandwich. The grade involution is the identity here, and the signed sandwich coincides with the unsigned one.

### The Even-Odd Algebra

Let $\mathrm{G} = \mathrm{G}^{+}\oplus\mathrm{G}^{-}$ with $\mathrm{G}^{+}$ spanned by $H$ and $\mathrm{G}^{-}$ by $E,F$ and the brackets $[H,E] = 2E$, $[H,F] = -2F$, $[E,F] = H$; the grade involution is $\alpha(H) = H$, $\alpha(E) = -E$, $\alpha(F) = -F$. Then the signed sandwich by the pair $(H,E)$ is $\Sigma^{\alpha}_{H,E}(x) = [H,[\alpha(x),E]]$, and the sign changes the operator on the odd part, which is the phenomenon of the grading.

### The Heisenberg Algebra

For the Heisenberg algebra with $[X,Y] = Z$ central and the grading with $Z$ even and $X,Y$ odd, the signed sandwich by the pair $(X,Y)$ is $\Sigma^{\alpha}_{X,Y}(x) = [X,[\alpha(x),Y]]$, which on $Z$ is nonzero and on $X,Y$ computes the central values; the example shows the signed sandwich acting on the odd part with the sign of the involution.

## Summary

On a Lie algebra the two products are the left multiplication $L_a = \operatorname{ad}_a$ and the right multiplication $R_b$ with $R_b(x) = [x,b] = -\operatorname{ad}_b$, and the unsigned sandwich is their composite $\Sigma_{a,b}(x) = [a,[x,b]]$; the **signed sandwich** is $\Sigma^{\alpha}_{a,b} = \Sigma_{a,b}\alpha$, with $\Sigma^{\alpha}_{a,b}(x) = [a,[\alpha(x),b]]$. It factors as $\Sigma_{a,b}\alpha = \alpha\Sigma_{\alpha(a),\alpha(b)}$, so the grade involution acts on the carrying pair and not on the operator, and its square is $\Sigma_{a,b}\Sigma_{\alpha(a),\alpha(b)}$, which does not collapse to a single sandwich because the algebra is not associative. The **signed conjugation** $\rho_a = \operatorname{Ad}_{\exp a}\alpha$ is the Lie-algebraic form of the conjugation $x\mapsto a\alpha(x)a^{-1}$; its square is the inner automorphism of $a+\alpha(a)$ and it is an involution exactly when that element is central, so the signed sandwich realises the reflections when the carrying pair is a pair of inverses. The construction degenerates when the grade involution is inner, when the algebra is abelian, and when either carrying element is central, in which cases the sandwich vanishes or collapses to an inner automorphism.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha$ | the grade involution, $\alpha^2 = \mathrm{id}$ |
| $L_a = \operatorname{ad}_a$ | the left multiplication, $x\mapsto[a,x]$ |
| $R_b$, $R_b(x) = [x,b]$ | the right multiplication, $R_b = -\operatorname{ad}_b$ |
| $L_a - R_a = \operatorname{ad}_a$ | the relation of the two products |
| $\Sigma_{a,b} = L_aR_b$ | the unsigned sandwich, $x\mapsto[a,[x,b]]$ |
| $\Sigma^{\alpha}_{a,b} = \Sigma_{a,b}\alpha$ | the signed sandwich, $x\mapsto[a,[\alpha(x),b]]$ |
| $\Sigma^{\alpha}_{a,b} = \alpha\Sigma_{\alpha(a),\alpha(b)}$ | the factorisation through the involution |
| $(\Sigma^{\alpha}_{a,b})^2 = \Sigma_{a,b}\Sigma_{\alpha(a),\alpha(b)}$ | the square |
| $\rho_a = \operatorname{Ad}_{\exp a}\alpha$ | the signed conjugation |
| $\rho_a^2 = \operatorname{Ad}_{\exp(a+\alpha(a))}$ | the square, an involution iff $a+\alpha(a)$ is central |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the adjoint action, the derivations and the structure of a Lie algebra.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras*, Chapters 1--3 (Springer, 1989), for the universal enveloping algebra, the adjoint action and the inner automorphisms.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, second edition, 2002), for the adjoint representation, the exponential and the inner automorphisms.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the grade involution, the graded structures and the signed operators.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the adjoint action, the derivations and the enveloping algebra.
