
# __The Signed Left Multiplication on a Lie Algebra__

## Introduction

The **signed left multiplication** is the one-sided operator $x\mapsto a\,\alpha(x)$, read on a Lie algebra through the bracket: $\ell^{\alpha}_a = \operatorname{ad}_a\circ\alpha$, so that $\ell^{\alpha}_a(x) = [a,\alpha(x)]$. It is the infinitesimal generator of the signed conjugation — the derivative at the origin of the family $\rho_{ta} = e^{t\operatorname{ad}_a}\alpha$ — and it is the unsigned left multiplication with the sign $-1$ imposed on the odd part. The article defines the operator, relates it to the unsigned left multiplication and to the signed sandwich, computes its kernel and its fixed set, and records the cases in which it degenerates.

This article treats the signed left multiplication on a Lie algebra, its relation to the unsigned left multiplication and the elements it fixes. It is the seventh article of the `- Operator Theory` group of the category; the unsigned left and right multiplications are from *Operators on a Lie Group*, the signed sandwich is *The Signed Sandwich on a Lie Algebra* and the reflections are *Reflections as Signed Two-Sided Operators on a Lie Algebra*, both above, and the adjoint of the operator is *The Signed Adjoint of the Left Multiplication on a Lie Algebra* of the `- * Operator Theory` group, below in the category.

The article assumes the Lie algebra and the adjoint representation from *The Lie Correspondence and the Adjoint Representation*, the exponential and its differential from *The Lie Algebra and the Exponential Map*, the grade involution and the grading from *Graded Lie Algebras and Lie Superalgebras*, the centraliser and the centre from *Lie Algebras*, and the signed sandwich and the signed conjugation from the two preceding articles of this group. The associative one-sided operator $x\mapsto a\alpha(x)$ of *The Signed Left Multiplication on an Algebra* is cited as the model; the module case is *The Graded Action on a Module over a Lie Algebra*, below.

## The Definition

### The One-Sided Operator

**Definition.** Let $\mathrm{G}$ be a Lie algebra with the grade involution $\alpha$. The **signed left multiplication** by $a\in\mathrm{G}$ is the endomorphism

$$
\ell^{\alpha}_a = L_a\circ\alpha = \operatorname{ad}_a\circ\alpha , \qquad \ell^{\alpha}_a(x) = [a,\alpha(x)] ,
$$

and the **signed right multiplication** is $r^{\alpha}_b = R_b\circ\alpha$ with $r^{\alpha}_b(x) = [\alpha(x),b]$.

**Proposition.** The signed left multiplication is the derivative at the origin of the family of the signed conjugations,

$$
\ell^{\alpha}_a = \frac{d}{dt}\Big|_{t=0}\rho_{ta} = \frac{d}{dt}\Big|_{t=0}e^{t\operatorname{ad}_a}\alpha ,
$$

and it is a derivation of the algebra,

$$
\ell^{\alpha}_a[x,y] = [\ell^{\alpha}_ax,y] + [x,\ell^{\alpha}_ay] .
$$

*Proof.* Differentiate the family at $t = 0$, which gives $\operatorname{ad}_a\alpha$ because the derivative of $e^{t\operatorname{ad}_a}$ is $\operatorname{ad}_a$; the derivation property is the Jacobi identity together with the multiplicativity of $\alpha$.

### The Relation to the Unsigned Case

**Proposition (the sign on the odd part).** The signed left multiplication is the unsigned left multiplication with the sign $-1$ on the odd part,

$$
\ell^{\alpha}_a(x) = \begin{cases} [a,x] = L_a(x), & x\in\mathrm{G}^{+},\\ -[a,x], & x\in\mathrm{G}^{-}, \end{cases}
$$

so that $\ell^{\alpha}_a = L_a(\mathrm{id} - 2\pi^{-})$ with $\pi^{-}$ the projection onto the odd part, and $\ell^{\alpha}_a = L_a$ exactly when the algebra is entirely even.

*Proof.* The grade involution is $+\mathrm{id}$ on the even part and $-\mathrm{id}$ on the odd part, so the composite with $L_a$ changes the sign of the second.

**Proposition (the factorisation through $\alpha$).** The signed left multiplication factors as

$$
\ell^{\alpha}_a = \alpha\circ L_{\alpha(a)} = \alpha\circ \ell^{\alpha}_{\alpha(a)} ,
$$

and the ordinary left multiplication is recovered by $\alpha\circ\ell^{\alpha}_a = L_{\alpha(a)}$; hence the map $a\mapsto\ell^{\alpha}_a$ is $\alpha$-semilinear in the parameter.

*Proof.* Use the naturality $\alpha L_a\alpha^{-1} = L_{\alpha(a)}$, that is $\alpha L_a = L_{\alpha(a)}\alpha$; multiplying by $\alpha^{-1} = \alpha$ and substituting gives the two forms.

## The Kernel and the Fixed Set

### The Kernel

**Theorem (the annihilated elements).** The kernel of the signed left multiplication is the centraliser of $\alpha(a)$,

$$
\ker\ell^{\alpha}_a = \{x : [a,\alpha(x)] = 0\} = \mathfrak{c}(\alpha(a)) ,
$$

and the operator is injective exactly when $\alpha(a)$ is not central in any summand.

*Proof.* The equation $[a,\alpha(x)] = 0$ becomes, after applying $\alpha$, $[\alpha(a),x] = 0$; conversely $x\in\mathfrak{c}(\alpha(a))$ gives $[a,\alpha(x)] = \alpha([\alpha(a),x]) = 0$. The injectivity statement is the vanishing of the kernel.

**Corollary.** If $\alpha = \mathrm{id}$ the kernel is the ordinary centraliser $\mathfrak{c}(a)$; the signed kernel is the centraliser of the image of the parameter, so the sign moves the parameter under the involution.

*Proof.* Substitute $\alpha = \mathrm{id}$ or use the previous computation.

### The Fixed Set

**Theorem (the fixed elements).** The fixed set of the signed left multiplication as a linear map is

$$
\operatorname{Fix}(\ell^{\alpha}_a) = \{x : [a,\alpha(x)] = x\} ,
$$

and it is nonempty exactly when the operator has a fixed point; it is the solution set of the linear equation $\operatorname{ad}_a\alpha(x) = x$, an affine subspace that is a coset of the kernel, and it is a single point exactly when $\operatorname{ad}_a\alpha$ has no eigenvalue $1$.

*Proof.* The fixed equation is the definition; the solution set of a linear equation is empty or an affine subspace with direction the kernel; the uniqueness of the solution is the invertibility of $\mathrm{id} - \operatorname{ad}_a\alpha$, that is the absence of the eigenvalue $1$.

**Corollary.** For the unsigned case $\alpha = \mathrm{id}$ the fixed equation is $[a,x] = x$, which has the solution $x = 0$ and no other for a nilpotent $a$; in general the existence of a nonzero fixed point is the resonance of the operator with the identity.

*Proof.* The equation $[a,x] = x$ is $\operatorname{ad}_a x = x$, whose solution space is the kernel of $\operatorname{ad}_a - \mathrm{id}$; the nilpotent case gives $\operatorname{ad}_a - \mathrm{id}$ invertible.

## The Relation to the Sandwich

**Theorem.** The signed sandwich is the signed left multiplication followed by a signed right multiplication,

$$
\Sigma^{\alpha}_{a,b} = \ell^{\alpha}_a\,R_{\alpha(b)} = r^{\alpha}_{b}\,L_{\alpha(a)} ,
$$

and it is the composite of the signed left multiplication with a right multiplication of the $\alpha$-transformed parameter; the unsigned sandwich is the special case $\alpha = \mathrm{id}$.

*Proof.* From $\Sigma^{\alpha}_{a,b} = L_aR_b\alpha$ and the commutation $\alpha R_b = R_{\alpha(b)}\alpha$ one gets $L_aR_b\alpha = L_a\alpha R_{\alpha(b)} = \ell^{\alpha}_aR_{\alpha(b)}$; the second form is analogous.

**Corollary.** The signed sandwich is the composite of two one-sided signed operators, and the signed conjugation is the exponential of the signed left multiplication,

$$
\rho_a = e^{\operatorname{ad}_a}\alpha = \exp(\ell^{\alpha}_a) ,
$$

where the exponential is that of the endomorphism algebra and the identity makes sense because the family $t\mapsto e^{t\operatorname{ad}_a}\alpha$ is the one-parameter family with derivative $\ell^{\alpha}_a$ at the origin, in the sense of the left quotient.

*Proof.* The first statement is the factorisation of the theorem; the second is the integration of the derivative computed above, the family $e^{t\operatorname{ad}_a}\alpha$ having the prescribed derivative at $t = 0$ in the semidirect product of the inner automorphisms with the involution.

## The Degenerate Cases

### The Identity Involution

**Proposition.** If $\alpha = \mathrm{id}$ then $\ell^{\alpha}_a = L_a = \operatorname{ad}_a$ is the ordinary left multiplication, its kernel is the centraliser $\mathfrak{c}(a)$, and its fixed set is the set of the resonances of $\operatorname{ad}_a$ with the identity; the signed theory coincides with the unsigned one.

*Proof.* Substitute $\alpha = \mathrm{id}$ everywhere.

### The Abelian Case

**Proposition.** If $\mathrm{G}$ is abelian then $\ell^{\alpha}_a = 0$ for every $a$; the operator vanishes and both the kernel and the fixed set degenerate — the kernel is the whole algebra and the fixed set is empty for $a\neq0$ and the whole algebra for $a = 0$.

*Proof.* The bracket is zero in an abelian algebra.

### The Inner Involution

**Proposition.** If the grade involution is inner, $\alpha = e^{\operatorname{ad}_w}$, then

$$
\ell^{\alpha}_a = \operatorname{ad}_a e^{\operatorname{ad}_w} = e^{\operatorname{ad}_w}\operatorname{ad}_{e^{-\operatorname{ad}_w}a} ,
$$

and the signed left multiplication is the unsigned one with the parameter transformed; the one-sided sign therefore produces no new operator, as in the two-sided case.

*Proof.* Substitute $\alpha = e^{\operatorname{ad}_w}$ and move the exponential past the derivation with the naturality of the adjoint action.

### The Central Parameter

**Proposition.** If $a$ is central then $\ell^{\alpha}_a = 0$, and the kernel is the whole algebra while the fixed set is empty for the nonzero parameter; the signed left multiplication vanishes on the centre, so the operator measures the non-centrality of the parameter.

*Proof.* A central $a$ has $\operatorname{ad}_a = 0$.

## Examples

### The Rank-One Algebra

Let $\mathrm{G} = \mathrm{sl}_2(\mathbb{R})$ with $\alpha$ the negative transpose, the Cartan involution, and let $a = E + F$ be an element of the odd part. Then $\ell^{\alpha}_a = \operatorname{ad}_a\alpha$ agrees with $\operatorname{ad}_a$ on the even part and is its negative on the odd part; the kernel is the centraliser of $\alpha(a) = -a$, which is one-dimensional, and the fixed equation $\operatorname{ad}_a\alpha(x) = x$ has no solution because $\operatorname{ad}_a$ is nilpotent on the even part.

### A Graded Matrix Algebra

Let $\mathrm{G} = \mathrm{gl}(n)$ with the grading of the blocks by a decomposition $\mathbb{C}^n = V^{+}\oplus V^{-}$, the grade involution changing the sign of the off-diagonal blocks. Then $\ell^{\alpha}_a$ is the operator $x\mapsto[a,\alpha(x)]$; its matrix is the commutator with the blocks, with the sign on the off-diagonal part, and the kernel is the centraliser of the block-transformed parameter.

### The Heisenberg Algebra

Let $\mathrm{G}$ be the Heisenberg algebra with $[X,Y] = Z$ central and the grading with $Z$ even and $X,Y$ odd. For $a = X$ the operator $\ell^{\alpha}_X(x) = [X,\alpha(x)]$ sends $Y$ to $[X,-Y] = -Z$ and $Z$ to $[X,Z] = 0$; the kernel contains $Z$ and $X$, and the operator is injective on the odd part generated by $Y$.

## Summary

The **signed left multiplication** on a Lie algebra is $\ell^{\alpha}_a = \operatorname{ad}_a\circ\alpha$, the operator $x\mapsto[a,\alpha(x)]$; it is the derivative at the origin of the family of the signed conjugations $e^{t\operatorname{ad}_a}\alpha$, it is a derivation, and it is the ordinary left multiplication with the sign $-1$ on the odd part and $+1$ on the even part. It factors through the grade involution as $\ell^{\alpha}_a = \alpha L_{\alpha(a)}$, so the ordinary left multiplication is $\alpha\ell^{\alpha}_a = L_{\alpha(a)}$; its kernel is the centraliser $\mathfrak{c}(\alpha(a))$ and its fixed set is the solution set of $\operatorname{ad}_a\alpha(x) = x$, a coset of the kernel. The signed sandwich is the composite of the signed left multiplication with a signed right multiplication, $\Sigma^{\alpha}_{a,b} = \ell^{\alpha}_aR_{\alpha(b)}$, and the signed conjugation is the exponential of the signed left multiplication, $\rho_a = \exp(\ell^{\alpha}_a)$ in the semidirect product of the inner automorphisms with the involution, which is the sense in which the reflections are integrated from the one-sided operator. The construction degenerates when the involution is the identity — the unsigned case — when the algebra is abelian or the parameter is central, and when the involution is inner, in which case the sign produces no new operator.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha$ | the grade involution |
| $\ell^{\alpha}_a = \operatorname{ad}_a\alpha$ | the signed left multiplication, $x\mapsto[a,\alpha(x)]$ |
| $r^{\alpha}_b = R_b\alpha$ | the signed right multiplication, $x\mapsto[\alpha(x),b]$ |
| $\ell^{\alpha}_a = L_a(\mathrm{id}-2\pi^{-})$ | the sign on the odd part |
| $\ell^{\alpha}_a = \alpha L_{\alpha(a)}$ | the factorisation through the involution |
| $\ker\ell^{\alpha}_a = \mathfrak{c}(\alpha(a))$ | the annihilated elements |
| $\operatorname{Fix}(\ell^{\alpha}_a) = \{x : \operatorname{ad}_a\alpha(x) = x\}$ | the fixed elements |
| $\Sigma^{\alpha}_{a,b} = \ell^{\alpha}_aR_{\alpha(b)}$ | the signed sandwich as a composite |
| $\rho_a = \exp(\ell^{\alpha}_a)$ | the signed conjugation as the exponential |
| $L_a = \operatorname{ad}_a$ | the unsigned left multiplication |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the adjoint action, the derivations and the centralisers.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras*, Chapters 1--3 (Springer, 1989), for the adjoint action, the inner automorphisms and the enveloping algebra.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, second edition, 2002), for the adjoint representation, the exponential and the graded structures.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the one-sided signed operators and the graded involutions.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the adjoint action and the one-parameter families of automorphisms.
