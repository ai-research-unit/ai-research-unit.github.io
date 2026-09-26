
# __Heyting Algebras and Intuitionistic Logic__

## Introduction

This is the second article of the Boolean system in Part V, and it occupies the **algebra slot** of that system for the *intuitionistic* reading of the two-element domain. The system is still the propositional one, with connectives $\wedge, \vee, \to, \neg$, but the logic is now the intuitionistic propositional calculus rather than the classical calculus, and the algebras are the **Heyting algebras** rather than the Boolean algebras. The article states the algebra, the semantics it supplies, and the precise sense in which the classical case of *Boolean Algebras and Lattices* is the special case in which double negation is the identity.

The boundary against the general theory is again deliberate. The proof theory of intuitionistic logic — natural deduction, the BHK reading, Kripke semantics, the disjunction and existence properties, the negative translation — belongs to *Logic and Proof* and to *Proof Theory and Type Theory*, and is cited rather than re-derived. The complete Heyting algebras, in which arbitrary joins distribute over meet, are the frames, and that topological enrichment is not developed here. The many-valued algebras that stand between the Boolean and the intuitionistic case and the non-distributive case are not covered here.

Throughout, a Heyting algebra is written $(H, \wedge, \vee, \to, 0, 1)$, its order is $\leq$, and its pseudocomplement is $\neg a = a \to 0$. The two-element algebra is $\mathbf{2} = \{0,1\}$, and the power set of a set $X$ is $\mathcal{P}(X)$. The Boolean algebras of *Boolean Algebras and Lattices* are the Heyting algebras in which $\neg\neg a = a$ for every $a$; this is the main theorem of the present article.

## Heyting Algebras

### Definition by Residuation

**Definition.** A **Heyting algebra** is a bounded lattice $(H, \wedge, \vee, 0, 1)$ together with a binary operation $\to$, the **Heyting implication**, subject to the **residuation** law

$$
c \leq a \to b \iff c \wedge a \leq b
$$

for all $a, b, c \in H$. The element $a \to b$ is the **relative pseudocomplement** of $a$ in $b$, and the **pseudocomplement** of $a$ is

$$
\neg a = a \to 0 .
$$

The defining law is an adjunction: the map $c \mapsto c \wedge a$ is left adjoint to the map $b \mapsto a \to b$ in the order-theoretic sense, and the general theory of such adjunctions — the **Galois connection** — is in *Order Theory and Lattices*. Because a right adjoint is unique when it exists, the implication is determined by the lattice whenever it exists.

**Theorem.** In a Heyting algebra the following hold for all $a, b, c$:

$$
a \to a = 1, \qquad a \wedge (a \to b) \leq b, \qquad b \leq a \to b, \qquad a \to 1 = 1, \qquad 1 \to a = a, \qquad 0 \to a = 1 .
$$

Moreover $a \to b = 1$ if and only if $a \leq b$, and $a \leq b$ implies $a \to b = 1$.

**Proof.** The first three are the residuation law at $c = 1$, at $c = a \to b$, and at $c = b$ respectively, using $b \wedge a = a \wedge b \leq b$. The identities $a \to 1 = 1$ and $1 \to a = a$ follow from $c \leq a \to 1 \iff c \wedge a \leq 1$, which is automatic, and from $c \leq 1 \to a \iff c \wedge 1 \leq a \iff c \leq a$. The identity $0 \to a = 1$ follows from $c \leq 0 \to a \iff c \wedge 0 \leq a$, which is automatic. Finally $a \to b = 1 \iff 1 \wedge a \leq b \iff a \leq b$ by residuation at $c = 1$. $\square$

**Theorem (monotonicity).** The implication is antitone in its first argument and monotone in its second: if $a' \leq a$ and $b \leq b'$, then $a \to b \leq a' \to b'$.

**Proof.** By residuation it suffices to show $(a \to b) \wedge a' \leq b'$. Now $(a \to b) \wedge a' \leq (a \to b) \wedge a \leq b \leq b'$, using $a' \leq a$ and the counit of the adjunction. $\square$

### The Underlying Lattice Is Distributive

**Theorem.** The underlying lattice of a Heyting algebra is distributive.

**Proof.** In any lattice $(a \wedge b) \vee (a \wedge c) \leq a \wedge (b \vee c)$, so it suffices to prove the reverse inequality. Write $D = (a \wedge b) \vee (a \wedge c)$. Since $b \wedge a \leq D$, residuation gives $b \leq a \to D$; since $c \wedge a \leq D$, it gives $c \leq a \to D$. Hence $b \vee c \leq a \to D$, and residuation again gives $a \wedge (b \vee c) \leq D$, which is the desired inequality. $\square$

The converse is not quite automatic in the infinite case but does hold in the finite case, and the precise statement is the following.

**Theorem.** A finite bounded lattice is a Heyting algebra if and only if it is distributive. In a finite distributive lattice, $a \to b$ is the join of the finitely many $c$ with $c \wedge a \leq b$.

**Proof.** The necessity is the theorem above. For the sufficiency, the set $\{c : c \wedge a \leq b\}$ is finite, nonempty (it contains $0$) and directed, since if $c_1 \wedge a \leq b$ and $c_2 \wedge a \leq b$ then $(c_1 \vee c_2) \wedge a = (c_1 \wedge a) \vee (c_2 \wedge a) \leq b$ by distributivity; let $d$ be its join. Then $d \wedge a = \bigvee \{c \wedge a : c \wedge a \leq b\} \leq b$ by distributivity again, so $d \leq a \to b$ if the operation is to satisfy residuation; conversely any $c$ with $c \wedge a \leq b$ satisfies $c \leq d$ by definition, so $d$ is the largest such $c$ and is the required relative pseudocomplement. $\square$

**Example (the three-element chain).** Let $H = \{0, u, 1\}$ with $0 < u < 1$. This finite chain is distributive, hence a Heyting algebra, with

$$
u \to 0 = 0, \qquad 0 \to u = 1, \qquad u \to u = 1, \qquad 1 \to u = u .
$$

The pseudocomplement is $\neg u = 0$ and $\neg 0 = 1$, so $\neg\neg u = \neg 0 = 1 \neq u$. The chain is therefore a Heyting algebra that is not a Boolean algebra, and it is the smallest one; it is the algebra of the three-valued Gödel logic, and the existence of such an algebra is the reason intuitionistic logic is not the logic of a single two-valued matrix.

**Example (Boolean algebras).** Every Boolean algebra is a Heyting algebra for the operation $a \to b = \neg a \vee b$; then $a \to 0 = \neg a \vee 0 = \neg a$, so the Heyting pseudocomplement is the Boolean complement. Residuation reads $c \leq \neg a \vee b \iff c \wedge a \leq b$, which is the standard Boolean equivalence of *Boolean Algebras and Lattices*. The Boolean algebras are thus the Heyting algebras in which $\neg\neg a = a$ everywhere, by the theorem below.

### Basic Identities of the Pseudocomplement

**Theorem.** In a Heyting algebra, for all $a, b$:

$$
a \wedge \neg a = 0, \qquad a \leq \neg \neg a, \qquad \neg \neg \neg a = \neg a, \qquad
\neg(a \vee b) = \neg a \wedge \neg b, \qquad \neg\neg(a \wedge b) = \neg\neg a \wedge \neg\neg b,
$$

and $\neg a = 1$ if and only if $a = 0$.

**Proof.** The first is the counit $a \wedge (a \to 0) \leq 0$. The second, $a \leq \neg\neg a$, follows from $a \wedge \neg a = 0$ by residuation. For the third, extensivity applied to $\neg a$ gives $\neg a \leq \neg\neg\neg a$, while antitonicity of $\neg$ applied to $a \leq \neg\neg a$ gives $\neg\neg\neg a \leq \neg a$; hence equality. For the De Morgan law, $c \leq \neg(a \vee b) \iff c \wedge (a \vee b) \leq 0 \iff (c \wedge a) \vee (c \wedge b) \leq 0 \iff c \wedge a \leq 0$ and $c \wedge b \leq 0 \iff c \leq \neg a \wedge \neg b$, and uniqueness of the adjoint gives the identity. For the meet identity, the inequality $\neg\neg(a \wedge b) \leq \neg\neg a \wedge \neg\neg b$ is monotonicity. For the reverse, put $d = \neg\neg a \wedge \neg\neg b$ and $c = d \wedge \neg(a \wedge b)$; then $c \wedge a \wedge b \leq (a \wedge b) \wedge \neg(a \wedge b) = 0$ gives $c \wedge a \leq \neg b$ by residuation, while $c \leq d \leq \neg\neg b$ gives $c \wedge \neg b = 0$; combining the two gives $c \wedge a = 0$, so $c \leq \neg a$, and $c \leq d \leq \neg\neg a$ gives $c \wedge \neg a = 0$, whence $c = 0$. Thus $d \wedge \neg(a \wedge b) = 0$, which by residuation is $d \leq \neg\neg(a \wedge b)$. The last claim: $\neg a = 1$ means $a \to 0 = 1$, which by residuation is $a \wedge 1 = a \leq 0$, that is $a = 0$; the converse is $0 \to 0 = 1$. $\square$

**Remark.** The identity $\neg(a \wedge b) = \neg a \vee \neg b$ fails in general. The down-set lattice of the poset $\{p,q\}$ with $p,q < r$ has the five elements $\emptyset, \{p\}, \{q\}, \{p,q\}, \{p,q,r\}$; writing $a = \{p\}$ and $b = \{q\}$, one has
$$
a \wedge b = \emptyset, \qquad \neg(a \wedge b) = \neg\emptyset = 1, \qquad \neg a \vee \neg b = \{q\} \vee \{p\} = \{p,q\},
$$
so the two sides differ. This failure is exactly the failure of one of De Morgan's laws in intuitionistic logic, and it is the algebraic content of the non-derivability of $\neg(\varphi \wedge \psi) \to \neg\varphi \vee \neg\psi$.

## Regular Elements and the Booleanization

**Definition.** An element $a$ of a Heyting algebra is **regular** if $\neg\neg a = a$. The set of regular elements is written $H_{\neg\neg}$.

**Theorem.** The map $j(a) = \neg\neg a$ is a **nucleus**: it is monotone, extensive ($a \leq j(a)$) and idempotent ($j(j(a)) = j(a)$), and it satisfies $j(a \wedge b) = j(a) \wedge j(b)$. The regular elements are exactly the fixed points of $j$, they contain $0$ and $1$ and every $\neg a$, and they form a Boolean algebra under

$$
a \sqcap b = a \wedge b, \qquad a \sqcup b = \neg\neg(a \vee b), \qquad \neg a, \qquad 0, \qquad 1 .
$$

**Proof.** Monotonicity of $j$ follows from monotonicity of $\neg$ applied twice; extensivity is $a \leq \neg\neg a$; idempotence is $\neg\neg\neg\neg a = \neg\neg a$, which follows from $\neg\neg\neg = \neg$ applied twice. The meet identity is proved above. The fixed points of an idempotent monotone map are its image; $0$ and $1$ are fixed since $\neg\neg 0 = \neg 1 = 0$ and $\neg\neg 1 = \neg 0 = 1$, and $\neg a$ is fixed by $\neg\neg\neg = \neg$. On the regular elements the operations displayed are well defined: $a \sqcap b$ is regular by the meet identity, $a \sqcup b$ is regular since it is $\neg\neg$ of something, and $\neg a$ is regular. The distributive law and complementation hold because $\neg\neg$ turns the Heyting operations into the Boolean ones: $a \sqcup \neg a = \neg\neg(a \vee \neg a) = \neg\neg 1 = 1$ and $a \sqcap \neg a \leq a \wedge \neg a = 0$. Hence $H_{\neg\neg}$ is a Boolean algebra. $\square$

**Theorem (Glivenko).** Let $\vdash_{\mathrm{IPC}}$ and $\vdash_{\mathrm{CPC}}$ denote derivability in intuitionistic and classical propositional logic. For every proposition $\varphi$,

$$
\vdash_{\mathrm{IPC}} \varphi \iff \vdash_{\mathrm{CPC}} \neg\neg\varphi, \qquad \text{and in fact} \qquad \vdash_{\mathrm{IPC}} \neg\varphi \iff \vdash_{\mathrm{CPC}} \neg\varphi .
$$

**Proof.** One direction is immediate: if $\vdash_{\mathrm{IPC}} \neg\neg\varphi$ then $\vdash_{\mathrm{CPC}} \neg\neg\varphi$, and classically $\neg\neg\varphi \to \varphi$, so $\vdash_{\mathrm{CPC}} \varphi$. Conversely, the Gödel–Gentzen negative translation $\varphi \mapsto \varphi^{N}$ satisfies
$$
\vdash_{\mathrm{CPC}} \varphi \implies \vdash_{\mathrm{IPC}} \varphi^{N}, \qquad \vdash_{\mathrm{IPC}} \varphi^{N} \leftrightarrow \neg\neg\varphi,
$$
so $\vdash_{\mathrm{CPC}} \varphi$ implies $\vdash_{\mathrm{IPC}} \neg\neg\varphi$; the second stated equivalence follows by applying the first to $\neg\varphi$. The negative translation and its properties belong to *Proof Theory and Type Theory*. $\square$

Glivenko's theorem is the precise sense in which classical propositional logic is embedded in the intuitionistic one at the level of negations. The class of Heyting algebras is therefore not a conservative extension of the Boolean case, because not every identity of Boolean algebras holds in a Heyting algebra; only the negative identities transfer.

## Heyting Algebras as the Algebra of Intuitionistic Logic

### The Lindenbaum Algebra of IPC

Let $L$ be the propositional language built from the connectives $\wedge, \vee, \to, \neg$, let $T$ be a theory, and define

$$
\varphi \sim_T \psi \iff T \vdash_{\mathrm{IPC}} \varphi \leftrightarrow \psi .
$$

As in the Boolean case, $\sim_T$ is a congruence, and the quotient is a Heyting algebra with the operations induced by the connectives; it is the **Lindenbaum algebra** of $T$. The verification is the same computation as in *Boolean Algebras and Lattices*, with the residuation law replacing the Boolean equivalence; the laws of $H$ are exactly the axioms and rules of the intuitionistic calculus, as stated in *Logic and Proof*.

**Theorem (algebraic completeness).** For every theory $T$ and proposition $\varphi$,

$$
T \vdash_{\mathrm{IPC}} \varphi \iff \text{every Heyting algebra homomorphism satisfying } T \text{ sends } \varphi \text{ to } 1 .
$$

**Proof.** Soundness is induction on the length of the derivation, each axiom being an identity of Heyting algebras and each rule preserving the value $1$. Completeness follows from the Lindenbaum algebra: if $T \nvdash \varphi$, then the class of $\varphi$ is not $1$ in $H = L/\sim_T$, and the quotient map is a homomorphism satisfying $T$ and sending $\varphi$ to a non-top element. Both directions are the standard algebraic-completeness argument; the syntactic proof and the Kripke completeness theorem, which uses partially ordered frames and is the sharper statement, are in *Proof Theory and Type Theory*. $\square$

### The Failure of Finite-Valued Semantics

The Boolean case has a single characteristic algebra $\mathbf{2}$, so classical propositional logic is two-valued. The intuitionistic case is different in kind.

**Theorem (Gödel).** There is no finite set $\{H_1,\dots,H_n\}$ of finite Heyting algebras such that $\vdash_{\mathrm{IPC}} \varphi$ if and only if $\varphi$ takes the value $1$ in every $H_i$ under every assignment; in particular no single finite Heyting algebra characterises $\mathrm{IPC}$.

**Proof.** For $n \geq 1$ let $p_0,\dots,p_n$ be distinct propositional variables and put
$$
D_n = \bigvee_{0 \leq i < j \leq n} (p_i \leftrightarrow p_j), \qquad p_i \leftrightarrow p_j = (p_i \to p_j) \wedge (p_j \to p_i).
$$
In a Heyting algebra with at most $n$ elements every assignment of the $n+1$ variables repeats a value, so some $p_i \leftrightarrow p_j$ receives the value $1$ and $D_n$ receives the value $1$; hence $D_n$ is valid in every Heyting algebra of cardinality at most $n$. Suppose finitely many finite Heyting algebras $H_1,\dots,H_m$ characterise $\mathrm{IPC}$, let $N$ be the largest of their cardinalities, and consider $D_N$. It is valid in each $H_k$ because $\lvert H_k \rvert \leq N$, so by the assumed characterisation $\vdash_{\mathrm{IPC}} D_N$. But $D_N$ is not a theorem: the unit interval $[0,1]$ is a complete chain and hence a Heyting algebra for $a \to b = 1$ when $a \leq b$ and $a \to b = b$ when $a > b$, and the assignment $p_i \mapsto i/(N+1)$ gives $p_i \leftrightarrow p_j = \min(p_i,p_j)$ for $i \neq j$, whose join over all pairs is $N/(N+1) \neq 1$. So $D_N$ is not valid in this Heyting algebra and hence, by soundness, is not a theorem, a contradiction. $\square$

**Remark.** The theorem is the reason $\mathrm{IPC}$ is a *genuinely* non-classical logic rather than a many-valued one in the sense: many-valued logics are finitely or continuously valued, while intuitionistic logic has no finite matrix semantics at all. The algebraic semantics by Heyting algebras is not a finite matrix but a variety, and it is the variety that the Lindenbaum construction uses.

### The Free Heyting Algebra

The contrast with the Boolean case is sharpest in the free algebra. The free Boolean algebra on $n$ generators is finite, of cardinality $2^{2^n}$, by *Boolean Algebras and Lattices*. The free Heyting algebra is not.

**Theorem (Rieger–Nishimura).** Let $F_{\mathrm{HA}}(n)$ be the free Heyting algebra on $n$ generators. For $n = 0$, $F_{\mathrm{HA}}(0) = \mathbf{2}$. For $n = 1$, $F_{\mathrm{HA}}(1)$ is countably infinite, and it is the **Rieger–Nishimura lattice**, the distributive lattice generated by the iterated implications of the generator. For every $n \geq 1$, $F_{\mathrm{HA}}(n)$ is infinite, and it embeds $F_{\mathrm{HA}}(1)$.

**Proof.** The one-generator case is the classical computation of Rieger and Nishimura: the elements are the finite joins of the iterated implications built from the generator, and the resulting distributive lattice is the countable Rieger–Nishimura lattice. The general statement follows because the subalgebra generated by one of the free generators is a quotient of $F_{\mathrm{HA}}(1)$, and the free algebra on one generator embeds in the free algebra on $n$ generators. The detailed enumeration is standard; the result is quoted from the literature. $\square$

This is the algebraic face of the fact that intuitionistic propositional logic has no finite characteristic algebra: the free algebra on one generator already has infinitely many elements, so no finite matrix can decide all of its identities.

### Filters, Homomorphisms and Subdirect Irreducibility

**Definition.** A **filter** of a Heyting algebra $H$ is a subset $F \subseteq H$ containing $1$ and closed under meet and upward inclusion. It is **proper** if $0 \notin F$, and **prime** if it is proper and $a \vee b \in F$ implies $a \in F$ or $b \in F$. The quotient $H/F$ is defined as in *Boolean Algebras and Lattices*.

**Theorem.** The quotient of a Heyting algebra by a filter is a Heyting algebra, and the quotient is nontrivial if and only if the filter is proper. The homomorphisms from a Heyting algebra to $\mathbf{2}$ correspond to the prime filters; a Heyting algebra is a Boolean algebra if and only if every prime filter is maximal, and the subdirectly irreducible Heyting algebras are exactly those with a greatest proper filter.

**Proof.** The quotient inherits the operations, and the implication is well defined because it is determined by the order, which is a congruence property; the nontriviality statement is as in the Boolean case. A homomorphism $h : H \to \mathbf{2}$ has kernel-cokernel $h^{-1}(1)$, a prime filter, and a prime filter $F$ gives a homomorphism $H \to H/F$ composed with the unique nontrivial map of a subdirectly irreducible quotient; the correspondence is the standard one. The Boolean criterion is that in a Boolean algebra every prime filter is maximal, and conversely a proper prime filter that is not maximal yields a quotient that is a Heyting algebra not satisfying double negation. The description of the subdirectly irreducible algebras is the standard one for Heyting algebras: subdirect irreducibility is equivalent to the existence of a greatest element of the lattice of proper filters, i.e. a greatest proper filter, because a subdirect product of nontrivial algebras must separate some pair, forcing a least nontrivial congruence. $\square$

**Remark.** Unlike the Boolean case, where $\mathbf{2}$ is the unique subdirectly irreducible algebra, the Heyting algebras have many subdirectly irreducible members — every finite chain is one — and this is another way to see that $\mathbf{2}$ does not generate the variety. The variety of Heyting algebras is generated by its finite members, by the finite model property of $\mathrm{IPC}$.

## Complete Heyting Algebras and the Frame Boundary

A **complete Heyting algebra** is a complete lattice that is a Heyting algebra with $a \wedge \bigvee_i b_i = \bigvee_i (a \wedge b_i)$ for all families; equivalently, the implication is

$$
a \to b = \bigvee \{c : c \wedge a \leq b\},
$$

the join now being arbitrary. Complete Heyting algebras are exactly the **frames**, and their study is the pointfree topology of that article; the open sets of a topological space, ordered by inclusion, are the standard example, with implication the interior of the complement union, $U \to V = \operatorname{int}\bigl((X \setminus U) \cup V\bigr)$. The present article stops at the finitary theory, which is what the Lindenbaum construction of a finitely generated logic requires, and the topological enrichment — locales, spatiality, sobriety — is left to the frame article.

**Example (open sets).** Let $X$ be a topological space and $H = \mathcal{O}(X)$ its lattice of open sets. Then $H$ is a complete Heyting algebra, with

$$
U \wedge V = U \cap V, \qquad U \vee V = U \cup V, \qquad U \to V = \operatorname{int}\bigl((X \setminus U) \cup V\bigr), \qquad \neg U = \operatorname{int}(X \setminus U).
$$

The identity $\neg\neg U = U$ holds exactly for the **regular open** sets, so $H_{\neg\neg}$ is the Boolean algebra of regular open sets, and for $X = \mathbb{R}$ with its usual topology the regular open sets form a complete Boolean algebra in which the open interval $(0,1)$ is regular but the union $(0,1) \cup (1,2)$ is not. This example is the prototype of the view that intuitionistic logic is the logic of open sets, and it is the bridge to the topological slot of the system.

**Example (the Sierpiński algebra).** The two-element algebra $\mathbf{2}$ is a Heyting algebra and also a topological space with open sets $\{\emptyset, \{1\}, \{0,1\}\}$; its open-set lattice is the three-element chain of the earlier example. The three-element chain is thus both the simplest non-Boolean Heyting algebra and the open-set lattice of the simplest non-discrete space, which is the reason the chain appears throughout pointfree topology.

## Summary

A Heyting algebra is a bounded lattice with a binary operation $\to$ satisfying the residuation law $c \leq a \to b \iff c \wedge a \leq b$; the operation is a right adjoint to the meet with $a$ and is determined by the lattice when it exists. The underlying lattice is distributive, and a finite bounded lattice is a Heyting algebra exactly when it is distributive, the implication being computed by the join of the finitely many $c$ with $c \wedge a \leq b$. The pseudocomplement $\neg a = a \to 0$ satisfies $a \wedge \neg a = 0$, $a \leq \neg\neg a$, $\neg\neg\neg a = \neg a$ and de Morgan's law for joins, but $\neg(a \wedge b) = \neg a \vee \neg b$ and $\neg\neg a = a$ both fail in general, the second already in the three-element chain and the first in the five-element down-set lattice of the poset $\{p,q\}$ with $p,q < r$. The regular elements, the fixed points of $\neg\neg$, form a Boolean algebra, and Glivenko's theorem identifies the negative fragment of intuitionistic propositional logic with the corresponding fragment of the classical one.

The Lindenbaum construction turns any intuitionistic theory into a Heyting algebra, and algebraic completeness states that intuitionistic derivability is exactly validity in all Heyting algebras; the homomorphisms to $\mathbf{2}$ are the prime filters. Unlike the classical case, no finite set of finite Heyting algebras characterises the logic, and the free Heyting algebra on one generator is already countably infinite — the Rieger–Nishimura lattice. Boolean algebras are the Heyting algebras satisfying $\neg\neg a = a$, and the passage from a Heyting algebra to its regular elements is the universal map to a Boolean algebra that preserves the negative identities.

The complete Heyting algebras are the frames, and pointfree topology is the study of the enrichment of this algebra by arbitrary joins. That enrichment, and the relation between frames and spaces, is not covered here; the non-distributive generalisation, in which uniqueness of the complement fails and orthomodular rather than distributive lattices appear, is outside its scope.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H$ | A Heyting algebra |
| $\wedge$, $\vee$ | Meet and join of the underlying lattice |
| $\to$ | Heyting implication, right adjoint to $c \mapsto c \wedge a$ |
| $\neg a$ | Pseudocomplement, $a \to 0$ |
| $0, 1$ | Least and greatest elements |
| $H_{\neg\neg}$ | Boolean algebra of regular elements, $\neg\neg a = a$ |
| $j(a) = \neg\neg a$ | The double-negation nucleus |
| $a \sqcap b$, $a \sqcup b$ | Meet and join in $H_{\neg\neg}$, with $a \sqcup b = \neg\neg(a \vee b)$ |
| $\vdash_{\mathrm{IPC}}$, $\vdash_{\mathrm{CPC}}$ | Derivability in intuitionistic, classical propositional logic |
| $F_{\mathrm{HA}}(n)$ | Free Heyting algebra on $n$ generators |
| $\mathcal{O}(X)$ | Lattice of open sets of a topological space, a complete Heyting algebra |
| $\mathbf{2}$ | The two-element Heyting (and Boolean) algebra |
| $M_3$, $N_5$ | The forbidden sublattices, as in *Order Theory and Lattices* |





## Further Reading

- Arend Heyting, *Die formalen Regeln der intuitionistischen Logik* (Sitzungsberichte der Preussischen Akademie der Wissenschaften, 1930), for the original formulation of the calculus and its algebraic reading.
- Helena Rasiowa and Roman Sikorski, *The Mathematics of Metamathematics* (PWN, Warsaw, 1963), for the algebraic semantics of intuitionistic logic and the Lindenbaum construction.
- Michael Dummett, *Elements of Intuitionism* (Oxford University Press, 2nd ed. 2000), for the BHK reading and the philosophical setting of the connectives.
- Dirk van Dalen, *Logic and Structure* (Springer, 5th ed. 2013), for intuitionistic propositional and predicate logic, Kripke semantics and completeness.
- Saunders Mac Lane and Ieke Moerdijk, *Sheaves in Geometry and Logic* (Springer, 1992), for complete Heyting algebras, frames and the open-set examples.
- Raymond Balbes and Philip Dwinger, *Distributive Lattices* (University of Missouri Press, 1974), for the Rieger–Nishimura lattice and the structure of free Heyting algebras.
- Peter T. Johnstone, *Stone Spaces* (Cambridge University Press, 1982), for frames, locales and the pointfree reading of the algebra.
