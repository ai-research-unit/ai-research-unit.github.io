
# __Heyting Algebras and Intuitionistic Logic__

## Introduction

This is the second article of the Boolean system in Part V, and it occupies the **algebra slot** of that system for the *intuitionistic* reading of the two-element domain. The system is still the propositional one, with connectives $\wedge, \vee, \to, \neg$, but the logic is now the intuitionistic propositional calculus rather than the classical calculus, and the algebras are the **Heyting algebras** rather than the Boolean algebras. The article states the algebra, the semantics it supplies, and the precise sense in which the classical case of *Boolean Algebras and Lattices* is the special case in which double negation is the identity.

The boundary against the general theory is again deliberate. The proof theory of intuitionistic logic — natural deduction, the BHK reading, Kripke semantics, the disjunction and existence properties, the negative translation — belongs to *Logic and Proof* and to *Proof Theory and Type Theory*, and is cited rather than re-derived. The complete Heyting algebras, in which arbitrary joins distribute over meet, are the frames, and that topological enrichment is not developed here. The many-valued algebras that stand between the Boolean and the intuitionistic case and the non-distributive case are not covered here.

Throughout, a Heyting algebra is written $(H, \wedge, \vee, \to, 0, 1)$, its order is $\leq$, and its pseudocomplement is $\neg \alpha = \alpha \to 0$. The two-element algebra is $\mathbf{2} = \{0,1\}$, and the power set of a set $X$ is $\mathcal{P}(X)$. The Boolean algebras of *Boolean Algebras and Lattices* are the Heyting algebras in which $\neg\neg \alpha = \alpha$ for every $\alpha$; this is the main theorem of the present article.

## Heyting Algebras

### Definition by Residuation

**Definition.** A **Heyting algebra** is a bounded lattice $(H, \wedge, \vee, 0, 1)$ together with a binary operation $\to$, the **Heyting implication**, subject to the **residuation** law

$$
\gamma \leq \alpha \to \beta \iff \gamma \wedge \alpha \leq \beta
$$

for all $\alpha, \beta, \gamma \in H$. The element $\alpha \to \beta$ is the **relative pseudocomplement** of $\alpha$ in $\beta$, and the **pseudocomplement** of $\alpha$ is

$$
\neg \alpha = \alpha \to 0 .
$$

The defining law is an adjunction: the map $\gamma \mapsto \gamma \wedge \alpha$ is left adjoint to the map $\beta \mapsto \alpha \to \beta$ in the order-theoretic sense, and the general theory of such adjunctions — the **Galois connection** — is in *Order Theory and Lattices*. Because a right adjoint is unique when it exists, the implication is determined by the lattice whenever it exists.

**Theorem.** In a Heyting algebra the following hold for all $\alpha, \beta, \gamma$:

$$
\alpha \to \alpha = 1, \qquad \alpha \wedge (\alpha \to \beta) \leq \beta, \qquad \beta \leq \alpha \to \beta, \qquad \alpha \to 1 = 1, \qquad 1 \to \alpha = \alpha, \qquad 0 \to \alpha = 1 .
$$

Moreover $\alpha \to \beta = 1$ if and only if $\alpha \leq \beta$, and $\alpha \leq \beta$ implies $\alpha \to \beta = 1$.

**Proof.** The first three are the residuation law at $\gamma = 1$, at $\gamma = \alpha \to \beta$, and at $\gamma = \beta$ respectively, using $\beta \wedge \alpha = \alpha \wedge \beta \leq \beta$. The identities $\alpha \to 1 = 1$ and $1 \to \alpha = \alpha$ follow from $\gamma \leq \alpha \to 1 \iff \gamma \wedge \alpha \leq 1$, which is automatic, and from $\gamma \leq 1 \to \alpha \iff \gamma \wedge 1 \leq \alpha \iff \gamma \leq \alpha$. The identity $0 \to \alpha = 1$ follows from $\gamma \leq 0 \to \alpha \iff \gamma \wedge 0 \leq \alpha$, which is automatic. Finally $\alpha \to \beta = 1 \iff 1 \wedge \alpha \leq \beta \iff \alpha \leq \beta$ by residuation at $\gamma = 1$.

**Theorem (monotonicity).** The implication is antitone in its first argument and monotone in its second: if $\alpha' \leq \alpha$ and $\beta \leq \beta'$, then $\alpha \to \beta \leq \alpha' \to \beta'$.

**Proof.** By residuation it suffices to show $(\alpha \to \beta) \wedge \alpha' \leq \beta'$. Now $(\alpha \to \beta) \wedge \alpha' \leq (\alpha \to \beta) \wedge \alpha \leq \beta \leq \beta'$, using $\alpha' \leq \alpha$ and the counit of the adjunction.

### The Underlying Lattice Is Distributive

**Theorem.** The underlying lattice of a Heyting algebra is distributive.

**Proof.** In any lattice $(\alpha \wedge \beta) \vee (\alpha \wedge \gamma) \leq \alpha \wedge (\beta \vee \gamma)$, so it suffices to prove the reverse inequality. Write $D = (\alpha \wedge \beta) \vee (\alpha \wedge \gamma)$. Since $\beta \wedge \alpha \leq D$, residuation gives $\beta \leq \alpha \to D$; since $\gamma \wedge \alpha \leq D$, it gives $\gamma \leq \alpha \to D$. Hence $\beta \vee \gamma \leq \alpha \to D$, and residuation again gives $\alpha \wedge (\beta \vee \gamma) \leq D$, which is the desired inequality.

The converse is not quite automatic in the infinite case but does hold in the finite case, and the precise statement is the following.

**Theorem.** A finite bounded lattice is a Heyting algebra if and only if it is distributive. In a finite distributive lattice, $\alpha \to \beta$ is the join of the finitely many $\gamma$ with $\gamma \wedge \alpha \leq \beta$.

**Proof.** The necessity is the theorem above. For the sufficiency, the set $\{\gamma : \gamma \wedge \alpha \leq \beta\}$ is finite, nonempty (it contains $0$) and directed, since if $\gamma_1 \wedge \alpha \leq \beta$ and $\gamma_2 \wedge \alpha \leq \beta$ then $(\gamma_1 \vee \gamma_2) \wedge \alpha = (\gamma_1 \wedge \alpha) \vee (\gamma_2 \wedge \alpha) \leq \beta$ by distributivity; let $\delta$ be its join. Then $\delta \wedge \alpha = \bigvee \{\gamma \wedge \alpha : \gamma \wedge \alpha \leq \beta\} \leq \beta$ by distributivity again, so $\delta \leq \alpha \to \beta$ if the operation is to satisfy residuation; conversely any $\gamma$ with $\gamma \wedge \alpha \leq \beta$ satisfies $\gamma \leq \delta$ by definition, so $\delta$ is the largest such $\gamma$ and is the required relative pseudocomplement.

**Example (the three-element chain).** Let $H = \{0, u, 1\}$ with $0 < u < 1$. This finite chain is distributive, hence a Heyting algebra, with

$$
u \to 0 = 0, \qquad 0 \to u = 1, \qquad u \to u = 1, \qquad 1 \to u = u .
$$

The pseudocomplement is $\neg u = 0$ and $\neg 0 = 1$, so $\neg\neg u = \neg 0 = 1 \neq u$. The chain is therefore a Heyting algebra that is not a Boolean algebra, and it is the smallest one; it is the algebra of the three-valued Gödel logic, and the existence of such an algebra is the reason intuitionistic logic is not the logic of a single two-valued matrix.

**Example (Boolean algebras).** Every Boolean algebra is a Heyting algebra for the operation $\alpha \to \beta = \neg \alpha \vee \beta$; then $\alpha \to 0 = \neg \alpha \vee 0 = \neg \alpha$, so the Heyting pseudocomplement is the Boolean complement. Residuation reads $\gamma \leq \neg \alpha \vee \beta \iff \gamma \wedge \alpha \leq \beta$, which is the standard Boolean equivalence of *Boolean Algebras and Lattices*. The Boolean algebras are thus the Heyting algebras in which $\neg\neg \alpha = \alpha$ everywhere, by the theorem below.

### Basic Identities of the Pseudocomplement

**Theorem.** In a Heyting algebra, for all $\alpha, \beta$:

$$
\alpha \wedge \neg \alpha = 0, \qquad \alpha \leq \neg \neg \alpha, \qquad \neg \neg \neg \alpha = \neg \alpha, \qquad
\neg(\alpha \vee \beta) = \neg \alpha \wedge \neg \beta, \qquad \neg\neg(\alpha \wedge \beta) = \neg\neg \alpha \wedge \neg\neg \beta,
$$

and $\neg \alpha = 1$ if and only if $\alpha = 0$.

**Proof.** The first is the counit $\alpha \wedge (\alpha \to 0) \leq 0$. The second, $\alpha \leq \neg\neg \alpha$, follows from $\alpha \wedge \neg \alpha = 0$ by residuation. For the third, extensivity applied to $\neg \alpha$ gives $\neg \alpha \leq \neg\neg\neg \alpha$, while antitonicity of $\neg$ applied to $\alpha \leq \neg\neg \alpha$ gives $\neg\neg\neg \alpha \leq \neg \alpha$; hence equality. For the De Morgan law, $\gamma \leq \neg(\alpha \vee \beta) \iff \gamma \wedge (\alpha \vee \beta) \leq 0 \iff (\gamma \wedge \alpha) \vee (\gamma \wedge \beta) \leq 0 \iff \gamma \wedge \alpha \leq 0$ and $\gamma \wedge \beta \leq 0 \iff \gamma \leq \neg \alpha \wedge \neg \beta$, and uniqueness of the adjoint gives the identity. For the meet identity, the inequality $\neg\neg(\alpha \wedge \beta) \leq \neg\neg \alpha \wedge \neg\neg \beta$ is monotonicity. For the reverse, put $\delta = \neg\neg \alpha \wedge \neg\neg \beta$ and $\gamma = \delta \wedge \neg(\alpha \wedge \beta)$; then $\gamma \wedge \alpha \wedge \beta \leq (\alpha \wedge \beta) \wedge \neg(\alpha \wedge \beta) = 0$ gives $\gamma \wedge \alpha \leq \neg \beta$ by residuation, while $\gamma \leq \delta \leq \neg\neg \beta$ gives $\gamma \wedge \neg \beta = 0$; combining the two gives $\gamma \wedge \alpha = 0$, so $\gamma \leq \neg \alpha$, and $\gamma \leq \delta \leq \neg\neg \alpha$ gives $\gamma \wedge \neg \alpha = 0$, whence $\gamma = 0$. Thus $\delta \wedge \neg(\alpha \wedge \beta) = 0$, which by residuation is $\delta \leq \neg\neg(\alpha \wedge \beta)$. The last claim: $\neg \alpha = 1$ means $\alpha \to 0 = 1$, which by residuation is $\alpha \wedge 1 = \alpha \leq 0$, that is $\alpha = 0$; the converse is $0 \to 0 = 1$.

**Remark.** The identity $\neg(\alpha \wedge \beta) = \neg \alpha \vee \neg \beta$ fails in general. The down-set lattice of the poset $\{p,q\}$ with $p,q < r$ has the five elements $\emptyset, \{p\}, \{q\}, \{p,q\}, \{p,q,r\}$; writing $\alpha = \{p\}$ and $\beta = \{q\}$, one has
$$
\alpha \wedge \beta = \emptyset, \qquad \neg(\alpha \wedge \beta) = \neg\emptyset = 1, \qquad \neg \alpha \vee \neg \beta = \{q\} \vee \{p\} = \{p,q\},
$$
so the two sides differ. This failure is exactly the failure of one of De Morgan's laws in intuitionistic logic, and it is the algebraic content of the non-derivability of $\neg(\varphi \wedge \psi) \to \neg\varphi \vee \neg\psi$.

## Regular Elements and the Booleanization

**Definition.** An element $\alpha$ of a Heyting algebra is **regular** if $\neg\neg \alpha = \alpha$. The set of regular elements is written $H_{\neg\neg}$.

**Theorem.** The map $j(\alpha) = \neg\neg \alpha$ is a **nucleus**: it is monotone, extensive ($\alpha \leq j(\alpha)$) and idempotent ($j(j(\alpha)) = j(\alpha)$), and it satisfies $j(\alpha \wedge \beta) = j(\alpha) \wedge j(\beta)$. The regular elements are exactly the fixed points of $j$, they contain $0$ and $1$ and every $\neg \alpha$, and they form a Boolean algebra under

$$
\alpha \sqcap \beta = \alpha \wedge \beta, \qquad \alpha \sqcup \beta = \neg\neg(\alpha \vee \beta), \qquad \neg \alpha, \qquad 0, \qquad 1 .
$$

**Proof.** Monotonicity of $j$ follows from monotonicity of $\neg$ applied twice; extensivity is $\alpha \leq \neg\neg \alpha$; idempotence is $\neg\neg\neg\neg \alpha = \neg\neg \alpha$, which follows from $\neg\neg\neg = \neg$ applied twice. The meet identity is proved above. The fixed points of an idempotent monotone map are its image; $0$ and $1$ are fixed since $\neg\neg 0 = \neg 1 = 0$ and $\neg\neg 1 = \neg 0 = 1$, and $\neg \alpha$ is fixed by $\neg\neg\neg = \neg$. On the regular elements the operations displayed are well defined: $\alpha \sqcap \beta$ is regular by the meet identity, $\alpha \sqcup \beta$ is regular since it is $\neg\neg$ of something, and $\neg \alpha$ is regular. The distributive law and complementation hold because $\neg\neg$ turns the Heyting operations into the Boolean ones: $\alpha \sqcup \neg \alpha = \neg\neg(\alpha \vee \neg \alpha) = \neg\neg 1 = 1$ and $\alpha \sqcap \neg \alpha \leq \alpha \wedge \neg \alpha = 0$. Hence $H_{\neg\neg}$ is a Boolean algebra.

**Theorem (Glivenko).** Let $\vdash_{\mathrm{IPC}}$ and $\vdash_{\mathrm{CPC}}$ denote derivability in intuitionistic and classical propositional logic. For every proposition $\varphi$,

$$
\vdash_{\mathrm{IPC}} \varphi \iff \vdash_{\mathrm{CPC}} \neg\neg\varphi, \qquad \text{and in fact} \qquad \vdash_{\mathrm{IPC}} \neg\varphi \iff \vdash_{\mathrm{CPC}} \neg\varphi .
$$

**Proof.** One direction is immediate: if $\vdash_{\mathrm{IPC}} \neg\neg\varphi$ then $\vdash_{\mathrm{CPC}} \neg\neg\varphi$, and classically $\neg\neg\varphi \to \varphi$, so $\vdash_{\mathrm{CPC}} \varphi$. Conversely, the Gödel–Gentzen negative translation $\varphi \mapsto \varphi^{N}$ satisfies
$$
\vdash_{\mathrm{CPC}} \varphi \implies \vdash_{\mathrm{IPC}} \varphi^{N}, \qquad \vdash_{\mathrm{IPC}} \varphi^{N} \leftrightarrow \neg\neg\varphi,
$$
so $\vdash_{\mathrm{CPC}} \varphi$ implies $\vdash_{\mathrm{IPC}} \neg\neg\varphi$; the second stated equivalence follows by applying the first to $\neg\varphi$. The negative translation and its properties belong to *Proof Theory and Type Theory*.

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

**Proof.** Soundness is induction on the length of the derivation, each axiom being an identity of Heyting algebras and each rule preserving the value $1$. Completeness follows from the Lindenbaum algebra: if $T \nvdash \varphi$, then the class of $\varphi$ is not $1$ in $H = L/\sim_T$, and the quotient map is a homomorphism satisfying $T$ and sending $\varphi$ to a non-top element. Both directions are the standard algebraic-completeness argument; the syntactic proof and the Kripke completeness theorem, which uses partially ordered frames and is the sharper statement, are in *Proof Theory and Type Theory*.

### The Failure of Finite-Valued Semantics

The Boolean case has a single characteristic algebra $\mathbf{2}$, so classical propositional logic is two-valued. The intuitionistic case is different in kind.

**Theorem (Gödel).** There is no finite set $\{H_1,\dots,H_n\}$ of finite Heyting algebras such that $\vdash_{\mathrm{IPC}} \varphi$ if and only if $\varphi$ takes the value $1$ in every $H_i$ under every assignment; in particular no single finite Heyting algebra characterises $\mathrm{IPC}$.

**Proof.** For $n \geq 1$ let $p_0,\dots,p_n$ be distinct propositional variables and put
$$
D_n = \bigvee_{0 \leq i < j \leq n} (p_i \leftrightarrow p_j), \qquad p_i \leftrightarrow p_j = (p_i \to p_j) \wedge (p_j \to p_i).
$$
In a Heyting algebra with at most $n$ elements every assignment of the $n+1$ variables repeats a value, so some $p_i \leftrightarrow p_j$ receives the value $1$ and $D_n$ receives the value $1$; hence $D_n$ is valid in every Heyting algebra of cardinality at most $n$. Suppose finitely many finite Heyting algebras $H_1,\dots,H_m$ characterise $\mathrm{IPC}$, let $N$ be the largest of their cardinalities, and consider $D_N$. It is valid in each $H_k$ because $\lvert H_k \rvert \leq N$, so by the assumed characterisation $\vdash_{\mathrm{IPC}} D_N$. But $D_N$ is not a theorem: the unit interval $[0,1]$ is a complete chain and hence a Heyting algebra for $\alpha \to \beta = 1$ when $\alpha \leq \beta$ and $\alpha \to \beta = \beta$ when $\alpha > \beta$, and the assignment $p_i \mapsto i/(N+1)$ gives $p_i \leftrightarrow p_j = \min(p_i,p_j)$ for $i \neq j$, whose join over all pairs is $N/(N+1) \neq 1$. So $D_N$ is not valid in this Heyting algebra and hence, by soundness, is not a theorem, a contradiction.

**Remark.** The theorem is the reason $\mathrm{IPC}$ is a *genuinely* non-classical logic rather than a many-valued one in the sense: many-valued logics are finitely or continuously valued, while intuitionistic logic has no finite matrix semantics at all. The algebraic semantics by Heyting algebras is not a finite matrix but a variety, and it is the variety that the Lindenbaum construction uses.

### The Free Heyting Algebra

The contrast with the Boolean case is sharpest in the free algebra. The free Boolean algebra on $n$ generators is finite, of cardinality $2^{2^n}$, by *Boolean Algebras and Lattices*. The free Heyting algebra is not.

**Theorem (Rieger–Nishimura).** Let $F_{\mathrm{HA}}(n)$ be the free Heyting algebra on $n$ generators. For $n = 0$, $F_{\mathrm{HA}}(0) = \mathbf{2}$. For $n = 1$, $F_{\mathrm{HA}}(1)$ is countably infinite, and it is the **Rieger–Nishimura lattice**, the distributive lattice generated by the iterated implications of the generator. For every $n \geq 1$, $F_{\mathrm{HA}}(n)$ is infinite, and it embeds $F_{\mathrm{HA}}(1)$.

**Proof.** The one-generator case is the classical computation of Rieger and Nishimura: the elements are the finite joins of the iterated implications built from the generator, and the resulting distributive lattice is the countable Rieger–Nishimura lattice. The general statement follows because the subalgebra generated by one of the free generators is a quotient of $F_{\mathrm{HA}}(1)$, and the free algebra on one generator embeds in the free algebra on $n$ generators. The detailed enumeration is standard; the result is quoted from the literature.

This is the algebraic face of the fact that intuitionistic propositional logic has no finite characteristic algebra: the free algebra on one generator already has infinitely many elements, so no finite matrix can decide all of its identities.

### Filters, Homomorphisms and Subdirect Irreducibility

**Definition.** A **filter** of a Heyting algebra $H$ is a subset $F \subseteq H$ containing $1$ and closed under meet and upward inclusion. It is **proper** if $0 \notin F$, and **prime** if it is proper and $\alpha \vee \beta \in F$ implies $\alpha \in F$ or $\beta \in F$. The quotient $H/F$ is defined as in *Boolean Algebras and Lattices*.

**Theorem.** The quotient of a Heyting algebra by a filter is a Heyting algebra, and the quotient is nontrivial if and only if the filter is proper. The homomorphisms from a Heyting algebra to $\mathbf{2}$ correspond to the prime filters; a Heyting algebra is a Boolean algebra if and only if every prime filter is maximal, and the subdirectly irreducible Heyting algebras are exactly those with a greatest proper filter.

**Proof.** The quotient inherits the operations, and the implication is well defined because it is determined by the order, which is a congruence property; the nontriviality statement is as in the Boolean case. A homomorphism $h : H \to \mathbf{2}$ has kernel-cokernel $h^{-1}(1)$, a prime filter, and a prime filter $F$ gives a homomorphism $H \to H/F$ composed with the unique nontrivial map of a subdirectly irreducible quotient; the correspondence is the standard one. The Boolean criterion is that in a Boolean algebra every prime filter is maximal, and conversely a proper prime filter that is not maximal yields a quotient that is a Heyting algebra not satisfying double negation. The description of the subdirectly irreducible algebras is the standard one for Heyting algebras: subdirect irreducibility is equivalent to the existence of a greatest element of the lattice of proper filters, i.e. a greatest proper filter, because a subdirect product of nontrivial algebras must separate some pair, forcing a least nontrivial congruence.

**Remark.** Unlike the Boolean case, where $\mathbf{2}$ is the unique subdirectly irreducible algebra, the Heyting algebras have many subdirectly irreducible members — every finite chain is one — and this is another way to see that $\mathbf{2}$ does not generate the variety. The variety of Heyting algebras is generated by its finite members, by the finite model property of $\mathrm{IPC}$.

## Complete Heyting Algebras and the Frame Boundary

A **complete Heyting algebra** is a complete lattice that is a Heyting algebra with $\alpha \wedge \bigvee_i \beta_i = \bigvee_i (\alpha \wedge \beta_i)$ for all families; equivalently, the implication is

$$
\alpha \to \beta = \bigvee \{\gamma : \gamma \wedge \alpha \leq \beta\},
$$

the join now being arbitrary. Complete Heyting algebras are exactly the **frames**, and their study is the pointfree topology of that article; the open sets of a topological space, ordered by inclusion, are the standard example, with implication the interior of the complement union, $U \to V = \operatorname{int}\bigl((X \setminus U) \cup V\bigr)$. The present article stops at the finitary theory, which is what the Lindenbaum construction of a finitely generated logic requires, and the topological enrichment — locales, spatiality, sobriety — is left to the frame article.

**Example (open sets).** Let $X$ be a topological space and $H = \mathcal{O}(X)$ its lattice of open sets. Then $H$ is a complete Heyting algebra, with

$$
U \wedge V = U \cap V, \qquad U \vee V = U \cup V, \qquad U \to V = \operatorname{int}\bigl((X \setminus U) \cup V\bigr), \qquad \neg U = \operatorname{int}(X \setminus U).
$$

The identity $\neg\neg U = U$ holds exactly for the **regular open** sets, so $H_{\neg\neg}$ is the Boolean algebra of regular open sets, and for $X = \mathbb{R}$ with its usual topology the regular open sets form a complete Boolean algebra in which the open interval $(0,1)$ is regular but the union $(0,1) \cup (1,2)$ is not. This example is the prototype of the view that intuitionistic logic is the logic of open sets, and it is the bridge to the topological slot of the system.

**Example (the Sierpiński algebra).** The two-element algebra $\mathbf{2}$ is a Heyting algebra and also a topological space with open sets $\{\emptyset, \{1\}, \{0,1\}\}$; its open-set lattice is the three-element chain of the earlier example. The three-element chain is thus both the simplest non-Boolean Heyting algebra and the open-set lattice of the simplest non-discrete space, which is the reason the chain appears throughout pointfree topology.

## Summary

A Heyting algebra is a bounded lattice with a binary operation $\to$ satisfying the residuation law $\gamma \leq \alpha \to \beta \iff \gamma \wedge \alpha \leq \beta$; the operation is a right adjoint to the meet with $\alpha$ and is determined by the lattice when it exists. The underlying lattice is distributive, and a finite bounded lattice is a Heyting algebra exactly when it is distributive, the implication being computed by the join of the finitely many $\gamma$ with $\gamma \wedge \alpha \leq \beta$. The pseudocomplement $\neg \alpha = \alpha \to 0$ satisfies $\alpha \wedge \neg \alpha = 0$, $\alpha \leq \neg\neg \alpha$, $\neg\neg\neg \alpha = \neg \alpha$ and de Morgan's law for joins, but $\neg(\alpha \wedge \beta) = \neg \alpha \vee \neg \beta$ and $\neg\neg \alpha = \alpha$ both fail in general, the second already in the three-element chain and the first in the five-element down-set lattice of the poset $\{p,q\}$ with $p,q < r$. The regular elements, the fixed points of $\neg\neg$, form a Boolean algebra, and Glivenko's theorem identifies the negative fragment of intuitionistic propositional logic with the corresponding fragment of the classical one.

The Lindenbaum construction turns any intuitionistic theory into a Heyting algebra, and algebraic completeness states that intuitionistic derivability is exactly validity in all Heyting algebras; the homomorphisms to $\mathbf{2}$ are the prime filters. Unlike the classical case, no finite set of finite Heyting algebras characterises the logic, and the free Heyting algebra on one generator is already countably infinite — the Rieger–Nishimura lattice. Boolean algebras are the Heyting algebras satisfying $\neg\neg \alpha = \alpha$, and the passage from a Heyting algebra to its regular elements is the universal map to a Boolean algebra that preserves the negative identities.

The complete Heyting algebras are the frames, and pointfree topology is the study of the enrichment of this algebra by arbitrary joins. That enrichment, and the relation between frames and spaces, is not covered here; the non-distributive generalisation, in which uniqueness of the complement fails and orthomodular rather than distributive lattices appear, is outside its scope.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H$ | A Heyting algebra |
| $\wedge$, $\vee$ | Meet and join of the underlying lattice |
| $\to$ | Heyting implication, right adjoint to $\gamma \mapsto \gamma \wedge \alpha$ |
| $\neg \alpha$ | Pseudocomplement, $\alpha \to 0$ |
| $0, 1$ | Least and greatest elements |
| $H_{\neg\neg}$ | Boolean algebra of regular elements, $\neg\neg \alpha = \alpha$ |
| $j(\alpha) = \neg\neg \alpha$ | The double-negation nucleus |
| $\alpha \sqcap \beta$, $\alpha \sqcup \beta$ | Meet and join in $H_{\neg\neg}$, with $\alpha \sqcup \beta = \neg\neg(\alpha \vee \beta)$ |
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
