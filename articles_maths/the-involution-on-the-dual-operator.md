# __The Involution on the Dual Operator__

## Introduction

A non-degenerate pairing on a linear space transports to the dual space, and with it the involution it defines on the endomorphisms. The result is that the two dualities of the category — the duality of the dual space, given by the transpose, and the duality of the pairing, given by the adjoint — commute: the adjoint of the transpose is the transpose of the adjoint, and the involution on the endomorphisms of the dual is the one transported from the involution on the endomorphisms of the space. This article develops the pairing induced on the dual, the comparison of the two dualities, and the involution it produces on the operators of the dual.

The transposed involution of an **involution** of $V$ is *Involutions of the Dual Space*; the transpose of a general linear map and the double dual are *The Transpose of a Linear Map*; the pairing-based involution and the adjoint of a single endomorphism are *Involutions of the Endomorphism Algebra* and *The Adjoint of an Endomorphism*. This article compares the two dualities and is the compatibility statement between them. The forms and the analysis are *Hilbert Algebras*, Part II.

Throughout, $F$ is a field, $V$ is a finite-dimensional $F$-linear space, $B$ is a non-degenerate reflexive pairing on $V$ with involution $\varsigma$ and reflexive sign $\varepsilon$, and $V^{*}$ is the dual space. The adjoint of $A \in \operatorname{End}_F(V)$ is $A^{*}$, and the transpose of a linear map is written ${}^{\mathsf{T}}$.

## The Pairing Induced on the Dual

**Definition.** For $\varphi \in V^{*}$ let $x_{\varphi}$ be the unique vector with $B(x_{\varphi},y) = \varphi(y)$ for all $y$, and define

$$
B^{*}(\varphi,\psi) = B(x_{\varphi},x_{\psi}) .
$$

**Proposition.** $B^{*}$ is a non-degenerate reflexive pairing on $V^{*}$ with the same involution $\varsigma$ and the same reflexive sign $\varepsilon$ as $B$; the assignment $\varphi \mapsto x_{\varphi}$ is an isomorphism $V^{*} \to V$ carrying $B^{*}$ to $B$, and it is $\varsigma$-semilinear in the sesquilinear case.

**Proof.** Well-definedness and bilinearity are inherited; non-degeneracy follows because $\varphi \mapsto x_\varphi$ is a bijection, being the composite of the linear isomorphism $V \to V^{*}$, $x \mapsto B(x,\cdot)$, with the inverse. The reflexivity and the sign are inherited from $B$, and the semilinearity is that of the identification.

**Lemma (the transpose transported is the adjoint).** For $C \in \operatorname{End}_F(V)$ and $\varphi \in V^{*}$ the representing vector of the transpose is

$$
x_{C^{\mathsf{T}}\varphi} = C^{*}x_{\varphi} .
$$

**Proof.** For every $z$, $B(C^{*}x_{\varphi}, z) = B(x_{\varphi}, Cz) = \varphi(Cz) = (C^{\mathsf{T}}\varphi)(z)$; the representing vector is unique, giving the identity.

**Proposition (the transpose as an adjoint).** For $A \in \operatorname{End}_F(V)$ the transpose $A^{\mathsf{T}} : V^{*} \to V^{*}$ satisfies

$$
B^{*}(A^{\mathsf{T}}\varphi,\psi) = B^{*}\bigl(\varphi, (A^{*})^{\mathsf{T}}\psi\bigr) ,
$$

so the $B^{*}$-adjoint of the transpose is the transpose of the $B$-adjoint; under the identification $V^{*} \cong V$ the transpose of $A$ corresponds to the adjoint of $A$.

**Proof.** By the lemma applied to $C=A$, the left side is $B(A^{*}x_{\varphi},x_{\psi}) = B(x_{\varphi}, A x_{\psi})$; by the lemma applied to $C=A^{*}$ and $(A^{*})^{*}=A$, the right side is $B(x_{\varphi}, A x_{\psi})$. For the last statement, the lemma with $C=A$ says exactly that $A^{\mathsf{T}}$ transported to $V$ is $A^{*}$.

## The Two Dualities Commute

**Theorem.** On the endomorphisms of the dual the $B^{*}$-adjoint of the transpose is the transpose of the $B$-adjoint:

$$
\bigl(A^{\mathsf{T}}\bigr)^{*_{B^{*}}} = \bigl(A^{*_B}\bigr)^{\mathsf{T}} ,
$$

and the assignment $A \mapsto A^{*_B}$ transported to $V^{*}$ by the identification $V^{*}\cong V$ is the $B^{*}$-involution on $\operatorname{End}_F(V^{*})$.

**Proof.** The transposition is a contravariant functor, so $(A^{\mathsf{T}})^{\mathsf{T}} = A$ under the double-dual identification, and the adjoint is an involution; applying the previous proposition to the transpose and to the adjoint gives the displayed identity, and the transport statement is the definition of the involution transported by an isomorphism.

**Corollary (the involutions correspond).** If $\Phi_{B}$ is the involution on $\operatorname{End}_F(V)$ with $\Phi_B(A) = A^{*_B}$ and $\Phi_{B^{*}}$ the corresponding involution on $\operatorname{End}_F(V^{*})$, then the isomorphism $V^{*}\cong V$ conjugates $\Phi_{B^{*}}$ into $\Phi_B$; the two have the same type in the sense of the involution of a linear space, and the same fixed part under the identification.

**Proof.** Conjugation by an isomorphism preserves the order and the multiplication, hence the involutions; the fixed parts correspond because the isomorphism is bijective.

**Example.** For the standard pairing on $F^n$ the induced pairing on the dual is standard, the transpose of a matrix is its transpose, and the adjoint is the transpose; the two dualities coincide, which is the degenerate case where the two comparisons add nothing.

## The Fixed Part and the Self-Adjoint Operators

**Proposition.** A functional $\varphi$ is fixed by the transported involution exactly when its representing vector $x_{\varphi}$ is $B$-self-adjoint in the image of the corresponding operator; the fixed part of the involution on $\operatorname{End}_F(V^{*})$ therefore corresponds to the self-adjoint operators of $\operatorname{End}_F(V)$, and the unitary elements correspond to one another.

**Proof.** The transport is an isomorphism of algebras, and it carries the fixed points and the unitary elements of one involution to those of the other.

## Summary

A non-degenerate reflexive pairing $B$ on $V$ induces a pairing $B^{*}$ on the dual $V^{*}$ by $B^{*}(\varphi,\psi) = B(x_\varphi,x_\psi)$, with the same involution and reflexive sign, and the assignment $\varphi\mapsto x_\varphi$ is an isomorphism carrying $B^{*}$ to $B$. Under this identification the transpose of an endomorphism corresponds to its adjoint, $B^{*}(A^{\mathsf{T}}\varphi,\psi) = B^{*}(\varphi,A^{*}\psi)$, and consequently the two dualities commute: $(A^{\mathsf{T}})^{*_{B^{*}}} = (A^{*_B})^{\mathsf{T}}$. The $B^{*}$-involution on the endomorphisms of the dual is the transport of the $B$-involution on the endomorphisms of the space, so the two have the same type, the same fixed part and the same unitary elements under the identification; the standard pairing on $F^n$ is the case where the two dualities coincide.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $B$ | the pairing on $V$ |
| $B^{*}(\varphi,\psi)=B(x_\varphi,x_\psi)$ | the induced pairing on $V^{*}$ |
| $x_\varphi$ | the $B$-dual vector of $\varphi$, $B(x_\varphi,y)=\varphi(y)$ |
| $A^{\mathsf{T}}\varphi = \varphi A$ | the transpose on the dual |
| $A^{*}$ | the $B$-adjoint on $V$ |
| $(A^{\mathsf{T}})^{*_{B^{*}}}=(A^{*_B})^{\mathsf{T}}$ | commutation of the two dualities |
| $\Phi_B, \Phi_{B^{*}}$ | the involutions on the two endomorphism algebras |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for duality and sesquilinear pairings.
- Werner Greub, *Linear Algebra* (Springer, 4th ed. 1975), for the transpose and the adjoint.
- Serge Lang, *Linear Algebra* (Springer, 3rd ed. 1987), for dual spaces, adjoints and their compatibility.
- Steven Roman, *Advanced Linear Algebra* (Springer, 3rd ed. 2008), for bilinear pairings, the induced form on the dual and the adjoint.
