
# __Involutions and the Word Problem__

## Introduction

A group presentation may be written so that the involution it carries is visible in the generators and relations; the involution then acts on the words, and two problems arise: the ordinary word problem, whether a word represents the identity, and the involutive word problem, whether a word and its image under the involution represent the same element. This article fixes the notion of an involutive presentation, proves that the involution neither creates nor removes decidability of the ordinary word problem, proves the equivalence of the word problem of a group and that of its extension by the involution, and records the classical decidable and undecidable cases. It is the sixth and last of the involutive `*`-articles; presentations, free groups, free products and the word problem are owned by *Generators, Presentations and Free Products*, the involution and the extension by *Involutive Groups*, and the associativity of the constructions used here by the same article.

## Involutive Presentations

**Definition.** An **involutive presentation** is a set $S$ with an involution $\sigma_S:S\to S$ (a bijection with $\sigma_S^{2}=\mathrm{id}$), extended anti-multiplicatively to the free group $F(S)$ by $\sigma(w_1\cdots w_k)=\sigma_S(w_k)^{-1}\cdots \sigma_S(w_1)^{-1}$ on reduced words, and a set $R\subseteq F(S)$ of relators with $\sigma(R)=R$; the group it presents is $G=\langle S\mid R\rangle$, and $\sigma$ descends to an involution of $G$. The pair $(G,\sigma)$ is the **presented involutive group**.

**Proposition (the descended map is an involution).** With the notation above, the extension of $\sigma_S$ to $F(S)$ is an anti-automorphism of order two, it preserves the normal closure of $R$ when $\sigma(R)=R$, and it descends to an involution of $G$.

**Proof.** The formula defines a map on words that reverses the product order and whose square is the identity, so it is an anti-automorphism of $F(S)$ of order two. If $r\in R$ then $\sigma(r)\in R$ by hypothesis, so the normal closure is stable; the descended map on $G=F(S)/\langle\langle R\rangle\rangle$ is therefore well defined, and it is an involution because $\sigma_S$ is. This is the involutive presentation of *Involutive Groups*, §10, read through a presentation.

**Proposition (every involutive group is presented).** Every involutive group $(G,\sigma)$ has an involutive presentation: take $S=G$ with $\sigma_S=\sigma$ and $R$ the set of relations $g\cdot h=gh$ for all $g,h\in G$.

**Proof.** The set $S=G$ generates $G$, the map $\sigma_S=\sigma$ is an involution of the set $S$ because $\sigma$ is an involution of the group, and the relators $g\cdot h=gh$ present $G$ and are stable under $\sigma$ because $\sigma(g h)=\sigma(h)\sigma(g)$. The presentation is not finite in general, which is the point of the notion: a finite involutive presentation is a finite presentation together with an involution of its generators that preserves its relators.

## The Ordinary Word Problem

**Definition.** The **word problem** of a presentation $\langle S\mid R\rangle$ asks for an algorithm deciding, for a word $w\in F(S)$, whether $w$ represents the identity of $G$. The **involutive word problem** of an involutive presentation asks for an algorithm deciding whether $w$ and $\sigma(w)$ represent the same element.

**Proposition (the involutive problem reduces to the ordinary one).** If the ordinary word problem of $(G,\sigma)$ is decidable and the involution $\sigma$ is computable on the generators, then the involutive word problem is decidable.

**Proof.** Given $w$, compute the word $\sigma(w)$ by applying $\sigma_S$ to each generator and reversing; then $w$ and $\sigma(w)$ represent the same element exactly when the word $w\,\sigma(w)^{-1}$ represents the identity, which the ordinary word problem decides.

**Remark (the two problems are not the same).** The reduction is one-way in form: it uses the ordinary decision procedure and the computability of $\sigma$. An involutive presentation whose involution is not computable on the generators may have a decidable ordinary word problem and an undecidable involutive one, because the question whether $w=\sigma(w)$ then involves a word the algorithm cannot produce.

**Theorem (Novikov–Boone).** There exists a finitely presented group whose word problem is undecidable.

**Proposition (undecidability survives the involution).** There exists a finitely presented involutive group whose ordinary word problem is undecidable.

**Proof.** Let $N=\langle S\mid R\rangle$ be a finitely presented group with undecidable word problem, and let $G=N\times C_2$ with the involution $\sigma(n,z)=(n,-z)$, which is an automorphism of order two. The group $G$ is finitely presented, the involution is computable on the generators, and the word problem of $G$ is undecidable: a word in the generators of $N$ represents the identity of $N$ if and only if the corresponding word in $G$ represents the identity, so a decision procedure for $G$ would decide the problem for $N$, contradicting the choice of $N$.

## Decidable Cases

**Proposition (the free group with reversal).** Let $F=F(S)$ be free on $S$ with the reversal $\mathrm{rev}$, extended anti-multiplicatively by fixing the letters. The ordinary word problem of $F$ is decidable by reduction of words, and the involutive word problem for $\mathrm{rev}$ is decidable too.

**Proof.** A word in $F(S)$ is trivial exactly when it reduces to the empty word by cancelling adjacent inverse pairs, which is a terminating and confluent procedure; and $\mathrm{rev}$ is computable on the generators, so the involutive problem reduces to the ordinary one by the proposition above.

**Proposition (free products).** If $G$ and $H$ have decidable word problems, then the free product $G*H$ has a decidable word problem by reduction to normal form, and the free product inherits the involutions of the factors.

**Proof.** The normal form of an element of $G*H$ is an alternating word of non-identity elements of the factors, and the reduction of an arbitrary word to normal form is computable when the word problems of the factors are; an involution of $G$ and one of $H$ combine to an involution of $G*H$ by acting on the letters of the normal form.

**Theorem (Coxeter groups and one-relator groups).** The Coxeter group $\langle s_1,\dots,s_n\mid s_i^{2}=e,\ (s_is_j)^{m_{ij}}=e\rangle$ with the involution fixing each generator has a decidable word problem (Tits), and a one-relator group with a computable involution has a decidable word problem (Magnus). The proofs are not reproduced here; the statements are recorded as the standard decidable classes.

## The Word Problem of the Extension

Let $\alpha$ be an involutive automorphism of $G$, computable on a generating set, and let $G\rtimes\langle t\rangle$ be the semidirect product of *Involutive Groups*, §9, with $tgt^{-1}=\alpha(g)$.

**Theorem.** The word problem of $G$ is decidable if and only if the word problem of $G\rtimes\langle t\rangle$ is decidable.

**Proof.** Suppose first that the word problem of $G$ is decidable. Every word in the generators of $G$ together with $t$ is reduced to a normal form by repeatedly (i) replacing $t^{2}$ by $e$, (ii) pushing each $t$ to the right across a generator $s$ by $t s=\alpha(s)t$, and (iii) reducing the resulting word in the generators of $G$ by the decision procedure for $G$. The reductions are computable because $\alpha$ is computable on the generators, and every word reaches the unique normal form $g\,t^{i}$ with $g$ in normal form and $i\in\{0,1\}$, which represents the identity exactly when $i=0$ and $g=e$. Conversely, a word $w$ in the generators of $G$ represents the identity of $G$ exactly when it represents the identity of $G\rtimes\langle t\rangle$, since $G$ is a subgroup; so a decision procedure for the extension decides the problem for $G$.

**Corollary (the involution does not change the word problem).** For a finitely presented involutive group the ordinary word problem and the word problem of the extension by the involution are equivalent, and both are decidable or both undecidable.

**Proof.** The extension is the semidirect product by the associated involutive automorphism, so the theorem applies; the ordinary word problem of the involutive group is that of $G$, and by the theorem it agrees with that of the extension.

**Remark (which direction is trivial).** The direction from the extension to $G$ is immediate because $G$ sits inside as a subgroup; the content is the other direction, where the computability of $\alpha$ on the generators is what makes the collection of the $t$'s effective. Without that computability the normal form is not reachable by an algorithm and the equivalence may fail.

## Summary

An **involutive presentation** is a set of generators with an involution, extended anti-multiplicatively to the free group, and a set of relators stable under it; it presents a group with an involution, and every involutive group has one, finite when the group is finitely presented and the involution is given on the generators. The **ordinary word problem** asks whether a word is trivial and the **involutive word problem** asks whether a word equals its image under the involution; the second reduces to the first when the involution is computable on the generators, and then is no harder.

Undecidability is not removed by an involution: the product $N\times C_2$ of a finitely presented group $N$ with undecidable word problem and the two-element group carries the involution $\sigma(n,z)=(n,-z)$ and keeps the undecidable word problem. Decidability is preserved in the free group with reversal, in free products of groups with decidable word problems, in Coxeter groups, and in one-relator groups. Finally, for a computable involutive automorphism $\alpha$ the word problem of $G$ is decidable if and only if that of the semidirect product $G\rtimes\langle t\rangle$ is, so the extension by the involution changes nothing.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma_S$ | involution on the generating set |
| $\sigma(w_1\cdots w_k)=\sigma_S(w_k)^{-1}\cdots\sigma_S(w_1)^{-1}$ | extension to the free group |
| $w\,\sigma(w)^{-1}=e$ | the involutive word problem, reduced to the ordinary one |
| $N\times C_2$, $\sigma(n,z)=(n,-z)$ | an involutive group with undecidable word problem |
| $g\,t^{i}$ | normal form in the extension, the reduction of the theorem |
| $\langle s_i\mid s_i^{2}=e,(s_is_j)^{m_{ij}}=e\rangle$ | the Coxeter presentation, decidable word problem |

## Further Reading

- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, fourth edition, 1995), for presentations, free groups, free products and the word problem.
- Wilhelm Magnus, Abraham Karrass and Donald Solitar, *Combinatorial Group Theory* (Dover, second revised edition, 1976), for the word problem of one-relator groups and the reduction of free words.
- Roger C. Lyndon and Paul E. Schupp, *Combinatorial Group Theory* (Springer, Classics in Mathematics, 2001), for the Novikov–Boone theorem, decision problems and free constructions.
- Petr S. Novikov, *On the algorithmic unsolvability of the word problem in group theory*, Trudy Matematicheskogo Instituta imeni V. A. Steklova 44 (1955), for the unsolvability theorem.
- James E. Humphreys, *Reflection Groups and Coxeter Groups* (Cambridge University Press, 1990), for Coxeter groups and the solution of their word problem.
