
# __The Signed Sandwich on a Group__

## Introduction

A two-sided operator on a group dresses an element between two factors, $x\mapsto axb$, and the sandwich is the operator so formed. When the group carries an involutive automorphism, the element in the middle can be twisted by it before it is dressed, and the operator $x\mapsto a\,\alpha(x)\,b$ — the **signed sandwich** — is the result. This article fixes the signed sandwich, relates it to the unsigned one, derives the laws by which the two families compose, and identifies the place where the reflections of the group arise.

The article assumes the elementary theory of groups and the automorphism group from *Groups*, the definition and the elementary structure of an involution of a group, the inversion, the associated involutive automorphism $\alpha=\sigma\iota$ and the fact that the involutive automorphisms are exactly the automorphisms of order two from *Involutive Groups*, and the left and right translations with their commutation and composition laws from *Left and Right Multiplication in a Group*. The one-sided signed operator is *The Signed Left Multiplication on a Group*; the reflections read as signed operators, the correspondence with the elements acting by an involution and the degenerate cases are *Reflections as Signed Two-Sided Operators on a Group*; the adjoint of the signed sandwich is *The Signed Adjoint Sandwich on a Group*. No distance, no norm and no form is used.

## The Grade Involution

**Definition.** A **grade involution** of $G$ is an automorphism $\alpha : G\to G$ with $\alpha^2=\mathrm{id}$, that is an involutive automorphism. The pair $(G,\alpha)$ is a **graded group**.

The name is a forward reference to the grading of an algebra, where the involution of the same name negates the odd part; on a group there is no grading yet, and the automorphism alone is meant. The grade involution is the automorphism member of the theory of *Involutive Groups*: an involution $\sigma$ of $G$ is an anti-automorphism of order two, the product $\sigma\iota$ with the inversion is an involutive automorphism, the passage $\sigma\mapsto\sigma\iota$ is a bijection from the involutions onto the involutive automorphisms, and every involutive automorphism arises this way. The involution and its associated automorphism are two structures and need not be the same map; throughout this article $\alpha$ is the involutive automorphism.

**Proposition (the examples).** The identity is a grade involution. If $z\in Z(G)$ has order two then $c_z(x)=zxz^{-1}=z^2x=x$ is the identity, so a central element of order two contributes no grade involution other than, at most, the identity; the conjugation by an element $a$ is an involutive automorphism exactly when $a^2\in Z(G)$, and it is then $\alpha=c_a$. The inversion is an involutive automorphism exactly when $G$ is abelian of exponent dividing two.

**Proof.** The identity map has order two and is an automorphism. $c_a$ is an automorphism with $(c_a)^2=c_{a^2}$, and this is the identity exactly when $a^2$ is central. For the inversion, an anti-automorphism is an automorphism exactly when the group is abelian, and then $\iota^2=\mathrm{id}$; on such a group $\iota$ is the identity exactly when the exponent divides two. These are the examples of *Involutive Groups*.

**Proposition (the grade involution acts on the translations).** For all $a,b\in G$,

$$
\alpha L_a \alpha = L_{\alpha(a)}, \qquad \alpha R_b \alpha = R_{\alpha(b)} .
$$

**Proof.** $(\alpha L_a\alpha)(x)=\alpha(a\alpha(x))=\alpha(a)x=L_{\alpha(a)}(x)$, and symmetrically $(\alpha R_b\alpha)(x)=\alpha(\alpha(x)b)=x\alpha(b)=R_{\alpha(b)}(x)$.

So the grade involution, read as an operator on $G$, conjugates the left regular subgroup onto itself and the right regular subgroup onto itself. It is an automorphism of the operator layer.

## The Unsigned Sandwich

**Definition.** For $a,b\in G$ the **sandwich** by $(a,b)$ is

$$
\Sigma_{a,b} : G\longrightarrow G, \qquad \Sigma_{a,b}(x) = a\,x\,b .
$$

**Proposition (factorisation and composition).** $\Sigma_{a,b}=L_a\circ R_b=R_b\circ L_a$, and

$$
\Sigma_{a,b}\circ\Sigma_{c,d} = \Sigma_{ac,\,db} .
$$

**Proof.** The factorisation is the definition of the translations; the composition is

$$
\Sigma_{a,b}\bigl(\Sigma_{c,d}(x)\bigr) = a\,(c\,x\,d)\,b = (ac)\,x\,(db) = \Sigma_{ac,\,db}(x).
$$

The sandwich operators therefore form a subgroup of $\operatorname{Sym}(G)$ under composition, with identity $\Sigma_{e,e}$ and inverse $\Sigma_{a,b}^{-1}=\Sigma_{a^{-1},b^{-1}}$. The assignment $(a,b)\mapsto\Sigma_{a,b}$ is a homomorphism $G\times G\to\operatorname{Sym}(G)$ with kernel the anti-diagonal copy of the centre, $\{(z,z^{-1}):z\in Z(G)\}$, so the subgroup is isomorphic to $(G\times G)/Z(G)$; this is the content of *Left and Right Multiplication in a Group*.

## The Signed Sandwich

**Definition.** Let $(G,\alpha)$ be a graded group. The **signed sandwich** by $(a,b)$ is

$$
\Sigma^{\alpha}_{a,b} : G\longrightarrow G, \qquad \Sigma^{\alpha}_{a,b}(x) = a\,\alpha(x)\,b .
$$

**Proposition (factorisation).** $\Sigma^{\alpha}_{a,b} = \Sigma_{a,b}\circ\alpha$, and more generally $L_a\circ\alpha\circ R_b = \Sigma^{\alpha}_{a,\alpha(b)}$. Every signed sandwich is a sandwich composed with the grade involution; in particular it is a bijection of $G$, with inverse $(\Sigma^{\alpha}_{a,b})^{-1}=\Sigma^{\alpha}_{a^{-1},b^{-1}}$.

**Proof.** $(\Sigma_{a,b}\circ\alpha)(x)=\Sigma_{a,b}(\alpha(x))=a\,\alpha(x)\,b$, which is the definition; the general identity is $L_a(\alpha(R_b(x)))=a\alpha(xb)=a\alpha(x)\alpha(b)=\Sigma^{\alpha}_{a,\alpha(b)}(x)$. The inverse is the signed sandwich by $(a^{-1},b^{-1})$ because $\Sigma^{\alpha}_{a^{-1},b^{-1}}(\Sigma^{\alpha}_{a,b}(x))=a^{-1}\alpha(a\alpha(x)b)b^{-1}=a^{-1}a\,x\,bb^{-1}=x$, using $\alpha^2=\mathrm{id}$.

**Proposition (the composition laws).** For all $a,b,c,d\in G$,

$$
\Sigma^{\alpha}_{a,b}\circ\Sigma^{\alpha}_{c,d} = \Sigma_{a\alpha(c),\,\alpha(d)b}, \qquad
\Sigma_{a,b}\circ\Sigma^{\alpha}_{c,d} = \Sigma^{\alpha}_{ac,\,db}, \qquad
\Sigma^{\alpha}_{a,b}\circ\Sigma_{c,d} = \Sigma^{\alpha}_{a\alpha(c),\,\alpha(d)b} .
$$

**Proof.** The first is

$$
\Sigma^{\alpha}_{a,b}\bigl(\Sigma^{\alpha}_{c,d}(x)\bigr) = a\,\alpha\bigl(c\,\alpha(x)\,d\bigr)\,b = a\alpha(c)\,x\,\alpha(d)\,b ,
$$

which is the unsigned sandwich by $(a\alpha(c),\alpha(d)b)$; the other two are the same computation with the appropriate factor changed to the unsigned one. A product of two signed sandwiches is unsigned, a product of an unsigned and a signed sandwich is signed, and a product of two unsigned sandwiches is unsigned.

**Proposition (the signed family is a coset).** Let $\mathfrak{S}=\{\Sigma_{a,b}:a,b\in G\}$ be the subgroup of the unsigned sandwiches. Then the signed sandwiches are the coset

$$
\mathfrak{S}^{\alpha} = \{\Sigma^{\alpha}_{a,b} : a,b\in G\} = \mathfrak{S}\,\alpha ,
$$

and the subgroup of $\operatorname{Sym}(G)$ generated by $\mathfrak{S}$ and $\alpha$ is $\mathfrak{S}\sqcup\mathfrak{S}\alpha$, of order $2|\mathfrak{S}|$ when $\alpha\notin\mathfrak{S}$ and equal to $\mathfrak{S}$ otherwise. Moreover

$$
\alpha\in\mathfrak{S} \iff \alpha \text{ is an inner automorphism} .
$$

**Proof.** By the factorisation, $\Sigma^{\alpha}_{a,b}=\Sigma_{a,b}\alpha$, so $\mathfrak{S}^\alpha=\mathfrak{S}\alpha$, and $\mathfrak{S}\alpha$ is a coset because it is the set of products of an element of the subgroup $\mathfrak{S}$ with the fixed element $\alpha$. The union generates the group because $\alpha^2=\mathrm{id}$. For the last statement, $\alpha=\Sigma_{a,b}$ means $\alpha(x)=axb$ for all $x$; at $x=e$ this gives $ab=e$, so $b=a^{-1}$, and then $\alpha(x)=axa^{-1}=c_a(x)$ for all $x$; conversely an inner automorphism $\alpha=c_a$ equals $\Sigma_{a,a^{-1}}$.

**Corollary (the degenerate case).** If $\alpha$ is inner, then the signed sandwiches are exactly the unsigned ones, and the signed operator adds no operator that the unsigned one does not already have; the signed sandwich is a genuinely new family exactly when the grade involution is not inner.

**Proof.** The last proposition gives $\mathfrak{S}^\alpha=\mathfrak{S}$ when $\alpha\in\mathfrak{S}$ and, since $|\mathfrak{S}\alpha|=|\mathfrak{S}|$, the set of signed sandwiches equals the set of unsigned sandwiches. If $\alpha$ is not inner then $\alpha\notin\mathfrak{S}$, so the signed family is a proper coset.

The corollary is the boundary of the construction: on an abelian group every automorphism is the identity or the inversion, both inner, and the signed sandwich collapses to the unsigned one; on a group with an outer involutive automorphism the two families are distinct.

## The Reflections it Realises

The signed sandwich specialises to the operator that is the group analogue of the reflection, the signed conjugation.

**Definition.** For $a\in G$ the **signed conjugation** by $a$ is the signed sandwich with $b=a^{-1}$,

$$
\Sigma^{\alpha}_{a,a^{-1}} : G\longrightarrow G, \qquad \Sigma^{\alpha}_{a,a^{-1}}(x) = a\,\alpha(x)\,a^{-1} .
$$

**Proposition (its square).** The square of the signed conjugation is the inner conjugation by the element $a\alpha(a)$:

$$
\bigl(\Sigma^{\alpha}_{a,a^{-1}}\bigr)^2 = c_{a\alpha(a)} = \Sigma_{a\alpha(a),\,(a\alpha(a))^{-1}} .
$$

Hence the signed conjugation is an involution of the set $G$ exactly when $a\alpha(a)\in Z(G)$, that is, exactly when the element $a\alpha(a)$ is central.

**Proof.** The composition law with $c=a$, $d=a^{-1}$ and the same for $(a,b)$ gives $\Sigma_{a\alpha(a),\,\alpha(a^{-1})a^{-1}}$, and $\alpha(a^{-1})a^{-1}=\alpha(a)^{-1}a^{-1}=(a\alpha(a))^{-1}$, which is the unsigned sandwich $\Sigma_{u,u^{-1}}$ for $u=a\alpha(a)$, that is $c_u$. An inner conjugation is the identity exactly on the central elements.

The operator $\Sigma^{\alpha}_{a,a^{-1}}$ is the element of the signed family that carries the reflection; the full treatment, the correspondence with the elements acting by an involution and the degenerate cases are *Reflections as Signed Two-Sided Operators on a Group*, and the self-adjointness of these operators under the natural pairing is *The Signed Adjoint of the Reflection on a Group*.

**Remark.** With $\alpha=\mathrm{id}$, the signed conjugation is the ordinary inner conjugation $c_a$, and its square is $c_{a^2}$; the criterion $a^2\in Z(G)$ for it to be an involution is then the classical statement that an inner automorphism is an involution exactly when the conjugating element squares to a central element.

## Summary

A **grade involution** of $G$ is an involutive automorphism $\alpha$, the automorphism member of the theory of *Involutive Groups*; it satisfies $\alpha^2=\mathrm{id}$ and conjugates the left and right translations according to $\alpha L_a\alpha=L_{\alpha(a)}$ and $\alpha R_b\alpha=R_{\alpha(b)}$.

The **sandwich** $\Sigma_{a,b}(x)=axb$ factors as $L_aR_b=R_bL_a$, composes by $\Sigma_{a,b}\Sigma_{c,d}=\Sigma_{ac,db}$, and forms a subgroup isomorphic to $(G\times G)/Z(G)$. The **signed sandwich** $\Sigma^{\alpha}_{a,b}(x)=a\alpha(x)b$ factors as $\Sigma_{a,b}\alpha$, is a bijection with inverse $\Sigma^{\alpha}_{a^{-1},b^{-1}}$, and composes by $\Sigma^{\alpha}_{a,b}\Sigma^{\alpha}_{c,d}=\Sigma_{a\alpha(c),\alpha(d)b}$, $\Sigma_{a,b}\Sigma^{\alpha}_{c,d}=\Sigma^{\alpha}_{ac,db}$ and $\Sigma^{\alpha}_{a,b}\Sigma_{c,d}=\Sigma^{\alpha}_{a\alpha(c),\alpha(d)b}$. The signed sandwiches are the coset $\mathfrak{S}\alpha$ of the subgroup $\mathfrak{S}$ of unsigned sandwiches, they differ from the unsigned ones exactly when the grade involution is not an inner automorphism, and the two families together generate $\mathfrak{S}\sqcup\mathfrak{S}\alpha$. The **signed conjugation** $\Sigma^{\alpha}_{a,a^{-1}}$ has square the inner conjugation by $a\alpha(a)$, so it is an involution exactly when $a\alpha(a)$ is central; this is the operator that carries the reflections.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha$ | the grade involution, an involutive automorphism of $G$ |
| $\alpha L_a\alpha=L_{\alpha(a)}$ | conjugation of a left translation by the grade involution |
| $\Sigma_{a,b}(x)=axb$ | the sandwich by $(a,b)$ |
| $\Sigma_{a,b}\Sigma_{c,d}=\Sigma_{ac,db}$ | composition of sandwiches |
| $\mathfrak{S}=\{\Sigma_{a,b}\}$ | the subgroup of unsigned sandwiches, $\cong(G\times G)/Z(G)$ |
| $\Sigma^{\alpha}_{a,b}(x)=a\alpha(x)b$ | the signed sandwich by $(a,b)$ |
| $\Sigma^{\alpha}_{a,b}=\Sigma_{a,b}\alpha$ | factorisation of the signed sandwich |
| $\Sigma^{\alpha}_{a,b}\Sigma^{\alpha}_{c,d}=\Sigma_{a\alpha(c),\alpha(d)b}$ | product of two signed sandwiches |
| $\mathfrak{S}^{\alpha}=\mathfrak{S}\alpha$ | the signed sandwiches as a coset |
| $\alpha\in\mathfrak{S}\iff\alpha$ is inner | degeneracy of the signed family |
| $\Sigma^{\alpha}_{a,a^{-1}}(x)=a\alpha(x)a^{-1}$ | the signed conjugation |
| $(\Sigma^{\alpha}_{a,a^{-1}})^2=c_{a\alpha(a)}$ | its square, an inner conjugation |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, second edition, 2001), for the sandwich operators and the signed inner conjugation that the graded sandwich generalises.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the signed conjugation and the reflections it generates.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutive automorphisms of a group and the associated structures.
- Derek J. S. Robinson, *A Course in the Theory of Groups* (Springer, second edition, 1996), for the automorphism group, the inner automorphisms and the normaliser of a subgroup.
