
# __Logic and Proof__

## Introduction

This article treats logic as the grammar of mathematical assertion and proof as the activity of deriving one assertion from others. It is the second entry of the corpus, below only *Sets, Functions and Relations*, and it supplies the connectives, the quantifiers and the rules of inference that every other article uses without comment. The mathematics of the article is the classical two-valued propositional and predicate calculus, together with the proof principles — direct proof, contraposition, contradiction, induction and recursion — that the corpus applies at every level.

The treatment is foundational but not formalist. The propositional calculus is presented semantically, through truth tables, and syntactically, through a system of inference rules; the two are shown to agree for propositional logic. The predicate calculus is presented as far as the language and its semantics require, with substitution, binding and validity; the completeness and compactness theorems are stated in outline and not developed. The axioms of the ambient set theory in which the models live are not covered here, and the algebra of propositions is recognised here as an instance of the Boolean algebras of Part V and of the power-set algebra of *Sets, Functions and Relations*.

Two boundaries are worth fixing at the outset. This article is about the logic used throughout the corpus, not about the metalogical study of formal systems: the arithmetisation of syntax, the incompleteness theorems, decidability and the halting problem, the semantics of first-order theories — elementary equivalence, quantifier elimination, ultraproducts — and the proof-theoretic study of calculi and the type-theoretic reading of proofs all lie outside this article. The present article uses none of those results and points to each of them where the subject begins.

## Propositional Logic

### Propositions and Connectives

A **proposition** is an assertion that is either true or false, and not both. Propositions are built from **atomic** propositions — denoted $p, q, r, \ldots$ or $p_1, p_2, \ldots$ — by means of the **connectives**, which combine simpler propositions into compound ones:

| Connective | Symbol | Read as |
|---|---|---|
| negation | $\neg p$ | not $p$ |
| conjunction | $p \wedge q$ | $p$ and $q$ |
| disjunction | $p \vee q$ | $p$ or $q$ |
| implication | $p \to q$ | if $p$ then $q$ |
| biconditional | $p \leftrightarrow q$ | $p$ if and only if $q$ |

The symbols $\wedge$, $\vee$, $\neg$ are the **algebraic** connectives; $\to$ and $\leftrightarrow$ are **defined** from them by

$$
p \to q \;:\equiv\; \neg p \vee q, \qquad p \leftrightarrow q \;:\equiv\; (p \to q) \wedge (q \to p).
$$

The definition of implication is the material one: $p \to q$ is false exactly when $p$ is true and $q$ is false. It is not a statement of causation. A compound proposition built from a fixed finite list of atoms is a **formula**, written $\varphi, \psi, \chi$.

Formulas are defined recursively: every atom is a formula, and if $\varphi$ and $\psi$ are formulas then so are $\neg \varphi$, $(\varphi \wedge \psi)$, $(\varphi \vee \psi)$, $(\varphi \to \psi)$ and $(\varphi \leftrightarrow \psi)$. Nothing else is a formula. This **inductive definition** is the first example of the principle of structural recursion treated below, and it is why every property of formulas can be proved by induction on their construction.

### Truth Tables and Tautologies

An **assignment** (or **valuation**) is a function $v$ from the atoms to the set $\{0, 1\}$ of truth values, where $1$ means true and $0$ means false. Every assignment extends uniquely to all formulas by the rules

| $p$ | $q$ | $\neg p$ | $p \wedge q$ | $p \vee q$ | $p \to q$ | $p \leftrightarrow q$ |
|---|---|---|---|---|---|---|
| $0$ | $0$ | $1$ | $0$ | $0$ | $1$ | $1$ |
| $0$ | $1$ | $1$ | $0$ | $1$ | $1$ | $0$ |
| $1$ | $0$ | $0$ | $0$ | $1$ | $0$ | $0$ |
| $1$ | $1$ | $0$ | $1$ | $1$ | $1$ | $1$ |

The table defines each connective by the truth values it returns; a larger table is filled in column by column, the columns for subformulas being computed before the columns for the formulas containing them. The uniqueness of the extension is a recursion theorem, proved below.

**Definition.** A formula $\varphi$ is a **tautology** (or is **valid**) if $v(\varphi) = 1$ for every assignment $v$; a **contradiction** if $v(\varphi) = 0$ for every $v$; and **satisfiable** if $v(\varphi) = 1$ for at least one $v$. Two formulas are **logically equivalent**, written $\varphi \equiv \psi$, if $v(\varphi) = v(\psi)$ for every assignment.

**Example.** The formula $p \vee \neg p$ (the law of excluded middle) is a tautology, and $p \wedge \neg p$ is a contradiction. The formula $p \to p$ is a tautology; $p \to \neg p$ is satisfiable but not valid, being true when $p$ is false. The formulas $p \to q$ and $\neg q \to \neg p$ are logically equivalent: their tables agree in all four rows.

**Proposition.** For all formulas $\varphi, \psi$ the following hold.

1. $\varphi \equiv \psi$ if and only if $\varphi \leftrightarrow \psi$ is a tautology.
2. $\varphi \equiv \psi$ if and only if $\varphi \to \psi$ and $\psi \to \varphi$ are both tautologies.
3. $\varphi$ is a tautology if and only if $\neg \varphi$ is a contradiction.

**Proof.** (1) $\varphi \leftrightarrow \psi$ is true exactly when $\varphi$ and $\psi$ have the same truth value, so the biconditional is a tautology exactly when the values agree under every assignment. (2) is (1) together with the definition of the biconditional, and (3) is the definition of the negation table. $\square$

### The Algebra of Propositions

The logical equivalences below are the laws of the **algebra of propositions**; each is verified from the truth tables, and the verification is left to the reader in the cases that repeat ones already done for the algebra of subsets.

1. **Idempotence.** $\varphi \wedge \varphi \equiv \varphi$, $\varphi \vee \varphi \equiv \varphi$.
2. **Commutativity.** $\varphi \wedge \psi \equiv \psi \wedge \varphi$, $\varphi \vee \psi \equiv \psi \vee \varphi$.
3. **Associativity.** $(\varphi \wedge \psi) \wedge \chi \equiv \varphi \wedge (\psi \wedge \chi)$, and likewise for $\vee$.
4. **Distributivity.** $\varphi \wedge (\psi \vee \chi) \equiv (\varphi \wedge \psi) \vee (\varphi \wedge \chi)$ and dually.
5. **Absorption.** $\varphi \wedge (\varphi \vee \psi) \equiv \varphi$ and $\varphi \vee (\varphi \wedge \psi) \equiv \varphi$.
6. **De Morgan.** $\neg(\varphi \wedge \psi) \equiv \neg \varphi \vee \neg \psi$ and $\neg(\varphi \vee \psi) \equiv \neg \varphi \wedge \neg \psi$.
7. **Double negation.** $\neg \neg \varphi \equiv \varphi$.
8. **Excluded middle and contradiction.** $\varphi \vee \neg \varphi$ is a tautology and $\varphi \wedge \neg \varphi$ is a contradiction.
9. **Contraposition.** $\varphi \to \psi \equiv \neg \psi \to \neg \varphi$.

The list is formally identical to the laws of the algebra of subsets in *Sets, Functions and Relations*, and the correspondence is not an accident. Fix atoms $p_1, \ldots, p_n$ and regard an assignment as a point of the **truth set** $\{0,1\}^n$. To each formula $\varphi$ in these atoms attach the set

$$
[[\varphi]] = \{v \in \{0,1\}^n : v(\varphi) = 1\}
$$

of assignments making it true. Then

$$
[[\neg\varphi]] = \{0,1\}^n \setminus [[\varphi]], \qquad [[\varphi \wedge \psi]] = [[\varphi]] \cap [[\psi]], \qquad [[\varphi \vee \psi]] = [[\varphi]] \cup [[\psi]],
$$

so the map $\varphi \mapsto [[\varphi]]$ carries the logic of $n$ atoms onto the power-set algebra of a set with $2^n$ points. Tautologies are the formulas with $[[\varphi]] = \{0,1\}^n$; contradictions are those with $[[\varphi]] = \emptyset$; and logical equivalence is equality of truth sets. This is the precise sense in which the algebra of propositions and the algebra of subsets are one structure, and both are instances of the **Boolean algebras** developed in Part V. The number $2^n$ is a cardinality, computed.

### Logical Consequence

**Definition.** A formula $\psi$ is a **logical consequence** of formulas $\varphi_1, \ldots, \varphi_n$, written $\varphi_1, \ldots, \varphi_n \models \psi$, if every assignment making all the $\varphi_i$ true makes $\psi$ true.

Logical consequence is a relation on formulas, not a connective: $\models$ is a statement *about* the formulas, made in the metalanguage, whereas $\to$ is a symbol *inside* the language. The two are related by the following standard fact.

**Theorem (deduction theorem, semantic form).** $\varphi_1, \ldots, \varphi_n \models \psi$ if and only if $\varphi_1 \wedge \cdots \wedge \varphi_n \to \psi$ is a tautology. In particular $\varphi \models \psi$ if and only if $\varphi \to \psi$ is a tautology.

**Proof.** Both sides say that there is no assignment making every $\varphi_i$ true and $\psi$ false: the left says it by the definition of consequence, the right because a conditional fails exactly at an assignment that makes its antecedent true and its consequent false. $\square$

A set $\Gamma$ of formulas is **satisfiable** if some single assignment makes every formula in $\Gamma$ true. A finite set is satisfiable exactly when its conjunction is satisfiable. The **compactness** of propositional logic — that $\Gamma$ is satisfiable if every finite subset of $\Gamma$ is — follows from the finiteness of the truth tables and is stated, with its first-order analogue.

## Predicate Logic

### Variables, Predicates and Quantifiers

Propositional logic analyses the way statements combine; predicate logic analyses their internal structure. A **first-order language** consists of **variables** $x, y, z, \ldots$; **constant symbols** $c, d, \ldots$; **function symbols** $f, g, \ldots$ each with a prescribed **arity**; **predicate symbols** $P, Q, R, \ldots$ each with an arity; and the **logical symbols** $\neg, \wedge, \vee, \to, \leftrightarrow, \forall, \exists, =$. Given a language, the **terms** are the variables, the constants, and the expressions $f(t_1, \ldots, t_k)$ for a $k$-ary function symbol $f$ and terms $t_i$; the **atomic formulas** are $P(t_1, \ldots, t_k)$ for a $k$-ary predicate symbol $P$ and terms $t_i$, together with the equations $t_1 = t_2$; and the **formulas** are built from the atomic ones by the connectives and the two **quantifiers**

$$
\forall x \, \varphi \quad (\text{for all } x, \varphi), \qquad \exists x \, \varphi \quad (\text{there exists } x \text{ such that } \varphi).
$$

The quantifier $\exists x \, \varphi$ is definable as $\neg \forall x \, \neg \varphi$, just as $\to$ and $\leftrightarrow$ were defined in the propositional case. Whether the corpus adopts the quantifier $\exists$ as primitive or defined is a convention; its meaning is fixed by the semantics below.

The **semantics** of a first-order language is a **structure** $\mathcal{M}$: a nonempty set $M$, the **domain** (or universe), together with an element $c^{\mathcal{M}} \in M$ for each constant, a function $f^{\mathcal{M}} : M^k \to M$ for each $k$-ary function symbol, and a subset $P^{\mathcal{M}} \subseteq M^k$ for each $k$-ary predicate symbol. An assignment sends each variable to an element of $M$; a term is then evaluated to an element of $M$ by recursion, and a formula is **satisfied**, written $\mathcal{M} \models \varphi[a]$ for the assignment $a$, by the familiar clauses:

$$
\mathcal{M} \models P(t_1,\ldots,t_k)[a] \iff (t_1^{\mathcal{M}},\ldots,t_k^{\mathcal{M}}) \in P^{\mathcal{M}},
$$

$$
\mathcal{M} \models \forall x\,\varphi[a] \iff \mathcal{M} \models \varphi[a'] \text{ for every assignment } a' \text{ agreeing with } a \text{ off } x.
$$

A formula with no free variables is a **sentence**, written $\sigma$; a sentence is **true in** $\mathcal{M}$, written $\mathcal{M} \models \sigma$, if it is satisfied under every assignment, equivalently under any one, since satisfaction of a sentence is independent of the assignment. A sentence is **valid** if it is true in every structure for the language, and a set of sentences $T$ is a **theory**; $\mathcal{M}$ is a **model** of $T$, written $\mathcal{M} \models T$, if it satisfies every sentence of $T$. The systematic study of this notion — elementary equivalence, the compactness and Löwenheim–Skolem theorems, quantifier elimination — isand the formal proof systems and their completeness are. Here only the vocabulary is being fixed.

### Free and Bound Occurrences

Quantification binds a variable, and the resulting distinction between free and bound occurrences is what separates a formula from a sentence.

**Definition.** In a formula, an occurrence of a variable $x$ is **bound** if it lies inside a quantifier $\forall x$ or $\exists x$; otherwise it is **free**. A variable is **free in** $\varphi$ if it has a free occurrence, and $\varphi$ is a **sentence** (or **closed**) if no variable is free in it. The **scope** of an occurrence of $\forall x$ or $\exists x$ is the subformula following it.

**Example.** In $\forall x\,(P(x) \to Q(x, y))$ the occurrences of $x$ are bound by $\forall x$ and the occurrence of $y$ is free; the formula is not a sentence. In $\forall x\, P(x) \vee Q(x)$ the scope of $\forall x$ is $P(x)$ only, so the occurrence of $x$ in $Q(x)$ is free and the formula says "(every $x$ satisfies $P$) or ($x$ satisfies $Q$)". Scoping is therefore a syntactic matter, and a formula is read by its bracketing, not by the apparent grouping of its symbols.

The notation $\varphi(x_1, \ldots, x_n)$ records that the free variables of $\varphi$ are among $x_1, \ldots, x_n$. Two formulas that differ only in the names of their bound variables are **alpha-equivalent** and are not distinguished; the renaming of a bound variable to a fresh one is **alpha-conversion**.

### Substitution

**Definition.** The **substitution** of a term $t$ for a variable $x$ in a formula $\varphi$, written $\varphi[t/x]$, is the result of replacing every free occurrence of $x$ in $\varphi$ by $t$.

Substitution is defined by recursion on formulas, with the one delicate clause being the quantifier clause: the occurrences of $x$ bound in $\varphi$ are not replaced, and if the quantifier binds a variable occurring in $t$, that variable must first be renamed to avoid **capture**.

**Example.** Let $\varphi$ be $\exists y\, (x < y)$, so that $x$ is free. Substituting the term $y$ for $x$ gives $\exists y\, (y < y)$, which says something different from the intended "$y$ is less than something": the free $y$ has been captured by the quantifier. The correct substitution first renames the bound variable, giving $\exists z\,(x < z)$ and then $\exists z\,(y < z)$.

**Convention.** In this corpus substitution is always understood to be **capture-avoiding**: bound variables are renamed as necessary before the substitution is performed. This is the standard convention, and it is why alpha-conversion is treated as an invisible operation.

## Rules of Inference and the Structure of a Proof

### Inference Rules and Formal Proofs

A **proof** in mathematics is a finite sequence of assertions, each of which is a hypothesis, an axiom or a consequence of earlier assertions by a rule of inference. A **rule of inference** has **premisses** and a **conclusion**; writing the premisses above a line and the conclusion below records that whenever the premisses hold, the conclusion may be asserted. The rules of the corpus are the standard ones of classical logic.

**Propositional rules.**

1. **Modus ponens.** From $\varphi$ and $\varphi \to \psi$, infer $\psi$.
2. **Modus tollens.** From $\neg \psi$ and $\varphi \to \psi$, infer $\neg \varphi$.
3. **Conjunction introduction.** From $\varphi$ and $\psi$, infer $\varphi \wedge \psi$; **conjunction elimination.** From $\varphi \wedge \psi$, infer $\varphi$, and infer $\psi$.
4. **Disjunction introduction.** From $\varphi$, infer $\varphi \vee \psi$; **disjunction elimination.** From $\varphi \vee \psi$, $\varphi \to \chi$ and $\psi \to \chi$, infer $\chi$.
5. **Conditional proof.** If $\psi$ has been derived from the hypothesis $\varphi$, infer $\varphi \to \psi$ and discharge the hypothesis.
6. **Reductio ad absurdum.** If a contradiction has been derived from the hypothesis $\neg \varphi$, infer $\varphi$ and discharge the hypothesis.

**Quantifier rules.**

7. **Universal instantiation.** From $\forall x\,\varphi$, infer $\varphi[t/x]$ for any term $t$.
8. **Universal generalisation.** From $\varphi$, where $x$ is not free in any undischarged hypothesis, infer $\forall x\,\varphi$.
9. **Existential introduction.** From $\varphi[t/x]$, infer $\exists x\,\varphi$; **existential elimination.** From $\exists x\,\varphi$ and $\forall x\,(\varphi \to \psi)$, where $x$ is not free in $\psi$, infer $\psi$.
10. **Equality rules.** $t = t$ is an axiom; from $t_1 = t_2$ and $\varphi[t_1/x]$, infer $\varphi[t_2/x]$.

The rules 5 and 6 are the ones that make a proof a *structured* object rather than a linear list, because they introduce and later discharge a hypothesis. A derivation is written as a tree or as an indented block, and the discipline of tracking which hypotheses remain undischarged is what distinguishes a correct proof from an assertion.

### Direct Proof

A **direct proof** of an implication $\varphi \to \psi$ assumes $\varphi$ and derives $\psi$. It is the shape of most proofs in the corpus: the hypotheses are fixed, the definitions are unfolded, and the conclusion is obtained by the rules above. The conditional is then inferred by rule 5.

**Example.** To prove that the sum of two even integers is even, assume $m = 2a$ and $n = 2b$; then $m + n = 2(a+b)$ is even, the last assertion being the definition. The proof is direct: the hypothesis is used, not its negation.

Direct proof also covers the proof of a universal statement: to prove $\forall x\, \varphi(x)$, one proves $\varphi(x)$ for a general $x$ and applies rule 8. The variable $x$ must be arbitrary — no special property of it may be used — and the restriction in rule 8 is exactly this requirement, since a special property would appear as an undischarged hypothesis mentioning $x$.

### Proof by Contrapositive

**Proposition.** $\varphi \to \psi$ and $\neg \psi \to \neg \varphi$ are logically equivalent.

**Proof.** This is the contraposition law of the algebra of propositions, verified by the truth table. $\square$

A **proof by contrapositive** of $\varphi \to \psi$ is a direct proof of $\neg \psi \to \neg \varphi$; the proposition above converts it into a proof of the original. The method is useful when the negation of the conclusion is a more pliable hypothesis than the hypothesis itself.

**Example.** To prove that if $n^2$ is even then $n$ is even, prove the contrapositive: if $n$ is odd, say $n = 2a + 1$, then $n^2 = 4a^2 + 4a + 1$ is odd. The direct approach would have to extract a square root; the contrapositive uses only the definition of oddness.

### Proof by Contradiction

A **proof by contradiction** of a statement $\varphi$ derives a contradiction from the hypothesis $\neg \varphi$ and concludes $\varphi$ by reductio ad absurdum (rule 6). It is a distinct method from proof by contrapositive: contraposition proves an implication by proving another implication, whereas contradiction proves any statement at all by refuting its negation, and it uses the law of excluded middle through rule 6.

**Example.** To prove that $\sqrt{2}$ is irrational, assume that $\sqrt{2} = m/n$ in lowest terms with $n \neq 0$; squaring and rearranging give $m^2 = 2n^2$, so $m^2$ and hence $m$ is even, say $m = 2k$; then $4k^2 = 2n^2$, so $n^2 = 2k^2$ and $n$ is even, contradicting the choice of $m/n$ in lowest terms. The contradiction refutes the assumption and proves the statement. The proof uses the parity result of the preceding example.

**Remark.** A statement proved by contradiction can often be proved directly or by contraposition, and the choice is one of exposition. The corpus prefers the shortest correct argument and states which method is being used when the method is not evident.

### Proof by Cases and by Equivalence

Two further shapes recur.

A **proof by cases** uses disjunction elimination: to prove $\chi$ from a hypothesis known to be $\varphi \vee \psi$, prove $\varphi \to \chi$ and $\psi \to \chi$ and conclude. The case distinction must be exhaustive, and each case may assume its own hypothesis.

A **proof of an equivalence** $\varphi \leftrightarrow \psi$ is a pair of direct proofs, one of $\varphi \to \psi$ and one of $\psi \to \varphi$. When the statements are not an implication chain, one proves $\varphi \to \psi$ and $\neg \varphi \to \neg \psi$, or $\varphi \to \psi$ and $\psi \to \varphi$ simultaneously, and either supplies the equivalence.

**Example.** To prove that an integer is even if and only if its square is even, prove both implications: if $n$ is even then $n^2$ is even directly, and if $n$ is odd then $n^2$ is odd by the contrapositive argument above.

## Induction and Recursion

### The Principle of Induction

The natural numbers $\mathbb{N}$ are ordered by $\leq$, and every nonempty subset has a least element; this **well-ordering** of $\mathbb{N}$ is taken as a basic property and is discussed from the set-theoretic side.

**Theorem (principle of induction).** Let $P$ be a property of natural numbers. If $P(0)$ holds and $P(n)$ implies $P(n+1)$ for every $n \in \mathbb{N}$, then $P(n)$ holds for every $n \in \mathbb{N}$.

**Proof.** Suppose not, and let $S = \{n \in \mathbb{N} : P(n) \text{ fails}\}$ be nonempty. By well-ordering $S$ has a least element $m$. Since $P(0)$ holds, $m \neq 0$, so $m = k + 1$ for some $k$. By minimality of $m$ the property $P(k)$ holds, and the induction step then gives $P(k+1) = P(m)$, contradicting $m \in S$. $\square$

The proof shows that induction is a consequence of well-ordering. The conditions of the theorem are the **base case** $P(0)$ and the **induction step** $P(n) \Rightarrow P(n+1)$; in the step, the assumption $P(n)$ is the **induction hypothesis**.

**Example.** $\sum_{k=0}^{n} k = n(n+1)/2$ for all $n$. The base case $n = 0$ reads $0 = 0$. For the step, assume the identity at $n$; then

$$
\sum_{k=0}^{n+1} k = \frac{n(n+1)}{2} + (n+1) = \frac{(n+1)(n+2)}{2},
$$

which is the identity at $n + 1$.

### Variants

Three variants are used in the corpus.

**Strong induction.** If $P(k)$ holds for all $k < n$ implies $P(n)$, then $P(n)$ holds for all $n$. The strong form is equivalent to the weak form and follows from well-ordering by the same argument, with the minimal counterexample $m$ satisfying $P(k)$ for all $k < m$ by minimality. It is used when the step needs more than the immediately preceding case, as in the Euclidean algorithm's correctness or the proof that every integer $> 1$ is a product of primes.

**Induction from a base.** If $P(n_0)$ holds and $P(n) \Rightarrow P(n+1)$ for all $n \geq n_0$, then $P(n)$ holds for all $n \geq n_0$. The statement for $n \geq n_0$ is proved by applying the theorem to the property $Q(n) :\equiv P(n + n_0)$.

**The well-ordering principle.** Every nonempty subset of $\mathbb{N}$ has a least element. This is equivalent to induction: the theorem above deduced induction from well-ordering, and conversely, if $S \subseteq \mathbb{N}$ had no least element, then $0 \notin S$, and if $0, 1, \ldots, n$ all lie outside $S$ then $n+1 \notin S$ as well, since otherwise $n+1$ would be the least element of $S$; strong induction would then give $S = \emptyset$. So induction implies that a set with no least element is empty, which is well-ordering.

### Recursive Definitions

Induction justifies not only proofs but **definitions** that specify a value at $n+1$ in terms of earlier values.

**Theorem (recursion).** Let $A$ be a set, $a \in A$, and let $F : \mathbb{N} \times A \to A$ be a function. There is exactly one function $u : \mathbb{N} \to A$ with $u(0) = a$ and $u(n+1) = F(n, u(n))$ for all $n$.

**Proof sketch.** Define $u$ to be the union of all finite functions $u_N$ on $\{0, \ldots, N\}$ satisfying the two conditions for $n < N$; each $u_N$ exists by induction on $N$ and is unique, and the $u_N$ agree on their common domains by induction. Their union is then a function on all of $\mathbb{N}$ with the required properties. Uniqueness of $u$ follows because two solutions agree at $0$ and, if they agree at $n$, at $n+1$. $\square$

The theorem licenses the familiar definitions of $n!$, of $a^n$, of the Fibonacci sequence, and of any function given by a recurrence. Without it a "definition" by recurrence would be an assertion about an infinite object that had not been constructed.

### Structural Induction

The same principle applies to any set whose elements are generated by finitely many constructors, and formulas are the standard example.

**Theorem (structural induction on formulas).** Let $P$ be a property of formulas of a language. If $P$ holds for every atomic formula, and $P(\varphi)$ and $P(\psi)$ together imply $P(\neg\varphi)$, $P(\varphi \wedge \psi)$, $P(\varphi \vee \psi)$ and $P(\varphi \to \psi)$, then $P$ holds for every formula.

**Proof.** By the definition of formulas, every formula is built from atomic ones by a finite number of applications of the connectives, and the hypotheses of the theorem reproduce the closure conditions of that definition; a formula of least construction length for which $P$ fails would then be atomic, or built from formulas of smaller length satisfying $P$, either of which is impossible. $\square$

Structural induction is used throughout the article implicitly: the unique extension of a valuation to all formulas, the definition of substitution and the proof that capture-avoiding substitution preserves meaning are all arguments of this shape. The analogous principle for the terms of a type theory appears.

## Consistency and Completeness in Outline

A **deductive system** consists of axioms and inference rules; a **derivation** is a finite sequence of formulas each of which is an axiom or follows from earlier ones by a rule. One writes $\vdash \varphi$ when $\varphi$ is derivable.

**Soundness.** Every derivable formula is valid: if $\vdash \varphi$ then $\models \varphi$. Soundness is proved by induction on the length of the derivation, checking that each axiom is valid and that each rule preserves validity.

**Completeness.** Every valid formula is derivable: if $\models \varphi$ then $\vdash \varphi$. For propositional logic this follows from the truth tables, a proof by induction on the number of atoms. For first-order logic it is the **Gödel completeness theorem**, and the enumeration of symbols and the construction of a term model that its proof requires — together with the compactness and Löwenheim–Skolem theorems and the limits imposed by Gödel's incompleteness theorems — are not covered here. The present article states the two directions and uses them; it does not prove the first-order completeness theorem, which is a theorem of the metatheory.

**Convention.** The corpus is classical: the law of excluded middle and the rule of reductio ad absurdum are available. **Intuitionistic** logic, which drops them and is the logic of the type-theoretic reading of proofs, is treated, and the corpus uses it only there. No article of the corpus proves a mathematical result that depends on rejecting classical logic, and the standard corpus vocabulary is classical.

## Summary

Propositions are combined by the connectives $\neg, \wedge, \vee, \to, \leftrightarrow$, whose meaning is fixed by truth tables; a valuation assigns truth values to the atoms and extends uniquely to all formulas. Tautologies and contradictions are formulas valid under every valuation and under none; logical equivalence is agreement of truth values; a formula is a logical consequence of others when every valuation making the others true makes it true. The algebra of propositions satisfies idempotence, commutativity, associativity, distributivity, absorption, the De Morgan laws, double negation and the excluded middle, and it is the same structure as the power-set algebra of *Sets, Functions and Relations*; both are Boolean algebras, developed in Part V.

First-order languages add variables, constants, function and predicate symbols, terms, atomic formulas and the quantifiers $\forall$ and $\exists$. A structure interprets the symbols in a domain, and satisfaction is defined by recursion; a sentence satisfied in every structure is valid, and a set of sentences is a theory. An occurrence of a variable inside a quantifier is bound, otherwise free; a formula with no free variable is a sentence; substitution replaces free occurrences and is carried out so as to avoid capture.

Proof is derivation by rules of inference: modus ponens and modus tollens, introduction and elimination for $\wedge$ and $\vee$, conditional pro, reductio ad absurdum, and the quantifier and equality rules. The standard shapes are direct pro, proof by contrapositive, proof by contradiction, proof by cases and proof of an equivalence. Induction follows from the well-ordering of $\mathbb{N}$ and comes in weak, strong and base-shifted forms; the recursion theorem licenses definitions by recurrence; and structural induction applies to formulas and to any inductively generated set. Soundness and completeness relate derivability to validity, soundness by induction on derivations and completeness for propositional logic by truth tables, while first-order completeness, compactness and the incompleteness phenomena belong .

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $p, q, r$; $p_1, p_2, \ldots$ | Atomic propositions |
| $\neg, \wedge, \vee, \to, \leftrightarrow$ | Negation, conjunction, disjunction, implication, biconditional |
| $\varphi, \psi, \chi$ | Formulas of a propositional or first-order language |
| $v : \text{atoms} \to \{0,1\}$ | Truth assignment (valuation) |
| $\models \varphi$, $\equiv$ | Validity (tautology); logical equivalence |
| $[[\varphi]]$ | Truth set of $\varphi$: assignments making it true |
| $\varphi_1, \ldots, \varphi_n \models \psi$ | Logical consequence |
| $\forall x$, $\exists x$ | Universal and existential quantifiers |
| $t, t_1, t_2$ | Terms of a first-order language |
| $P, Q, R$; $f, g$ | Predicate and function symbols |
| $\mathcal{M} = (M, \ldots)$ | A structure with domain $M$ |
| $\mathcal{M} \models \varphi[a]$ | Satisfaction of $\varphi$ in $\mathcal{M}$ under assignment $a$ |
| $\sigma$, $T$ | Sentence; theory (set of sentences) |
| $\mathcal{M} \models T$ | $\mathcal{M}$ is a model of $T$ |
| $\varphi[t/x]$ | Substitution of term $t$ for free occurrences of $x$ |
| $\vdash \varphi$ | Derivability of $\varphi$ in a deductive system |
| $\mathbb{N}$ | The natural numbers, well-ordered by $\leq$, with least element $0$ |
| $P(n)$, $P(k)$ for $k<n$ | Induction hypothesis; strong induction hypothesis |
| $u(0)=a$, $u(n+1)=F(n,u(n))$ | Recursive definition of a function $u : \mathbb{N} \to A$ |





## Further Reading

- Stephen Cole Kleene, *Introduction to Metamathematics* (Van Nostrand, 1952), for the classical presentation of propositional and predicate logic, truth tables and the rules of inference.
- Herbert B. Enderton, *A Mathematical Introduction to Logic*, 2nd ed. (Academic Press, 2001), for the semantic and syntactic development of first-order logic, soundness and completeness.
- Dirk van Dalen, *Logic and Structure*, 5th ed. (Springer, 2013), for a concise account of the connectives, quantifiers, derivations and the completeness theorem.
- Elliott Mendelson, *Introduction to Mathematical Logic*, 6th ed. (CRC Press, 2015), for formal proof systems and the metatheorems of classical logic.
- Paul R. Halmos and Steven Givant, *Logic as Algebra* (Mathematical Association of America, 1998), for the identification of propositional logic with Boolean algebra that underlies the algebra of propositions.
- Kenneth Kunen, *The Foundations of Mathematics* (College Publications, 2009), for the set-theoretic approach to induction, recursion and the construction of $\mathbb{N}$.
- Jean-Yves Girard, *Proofs and Types* (Cambridge University Press, 1989), for the natural-deduction presentation of the rules used here and its type-theoretic reading.
