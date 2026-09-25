
# __Formal Logic and Computability__

## Introduction

This article treats first-order logic as a formal system and the notion of effective computation that the syntax of such a system presupposes. It states the completeness theorem, which makes the syntactic notion of derivability coincide with the semantic notion of validity, and draws its two standard consequences, compactness and the Löwenheim–Skolem theorems. It then turns to computability: Turing machines, recursive functions, the Church–Turing thesis, decidability and undecidability, the halting problem, and the incompleteness theorems of Gödel, which show that any formal system strong enough to describe arithmetic must fail to decide some of its own sentences.

The article stands sixth in the corpus, above the foundational layer of *Sets, Functions and Relations*, *Logic and Proof*, *Order Theory and Lattices*, *Cardinality and the Axiom of Choice* and *Set-Theoretic Foundations*. It uses the language and the inference rules of *Logic and Proof*, the enumeration and diagonal techniques of *Cardinality and the Axiom of Choice*, and the arithmetisation of syntax and the ordinals of *Set-Theoretic Foundations*. Its results are quoted: the compactness theorem is the tool, and the proof-theoretic reading of the completeness and normalisation theorems is not covered here. The present article states the theorems of logic and of computability with proof sketches where the argument is illuminating or short, and with references where it is long; the emphasis is on the statements and the definitions, which the other articles use.

The subject is genuinely part of mathematics, and the article treats it so. Nothing physical is invoked: a Turing machine is a mathematical object, a finite table of instructions, and the claim that it captures intuitive computability is a thesis, not a definition. The results of the article are theorems of the metatheory — of the ordinary mathematical theory of finite objects — and they are proved as such.

## Formal Systems and Derivations

### First-Order Logic Formally

The vocabulary was introduced in *Logic and Proof*: a first-order language $\mathcal{L}$ consists of variables, constant symbols, function symbols with arities, predicate symbols with arities, and the logical symbols $\neg, \wedge, \vee, \to, \leftrightarrow, \forall, \exists, =$. The **terms** and **formulas** of $\mathcal{L}$ are defined by recursion, and an $\mathcal{L}$-**sentence** is a formula with no free variables.

For the metatheory it is essential that the syntax of $\mathcal{L}$ be a set of finite objects that can be listed and manipulated. The alphabet of $\mathcal{L}$ is countable when the language has countably many symbols, and the formulas are finite strings, so the set of $\mathcal{L}$-formulas is countable. This is the hypothesis behind every enumeration argument below: one can assign numbers to formulas and reason about the assignment.

**Definition.** A **formal system** (or **deductive system**) for $\mathcal{L}$ consists of a set of **logical axioms** and a set of **inference rules**. A **derivation** is a finite sequence $\varphi_1, \ldots, \varphi_n$ of $\mathcal{L}$-formulas, each of which is a logical axiom, a member of a given set $T$ of nonlogical axioms (the **theory**), or obtained from earlier formulas by an inference rule. The last formula is the **conclusion**; one writes $T \vdash \varphi$ when some derivation from $T$ concludes with $\varphi$, and $\vdash \varphi$ when $T = \emptyset$.

This article uses the natural-deduction rules of *Logic and Proof*, together with the equality axioms, as its formal system. Other choices — Hilbert systems, sequent calculi, resolution — are equivalent in the sense that they derive the same formulas, and the comparison belongs. The **deduction theorem**, proved for natural deduction as the rule of conditional pro, states that $T \cup \{\varphi\} \vdash \psi$ if and only if $T \vdash \varphi \to \psi$.

**Definition.** A theory $T$ is **consistent** if there is no formula $\varphi$ with $T \vdash \varphi$ and $T \vdash \neg\varphi$; it is **complete** if for every sentence $\sigma$ of its language, $T \vdash \sigma$ or $T \vdash \neg\sigma$; it is **recursively axiomatised** (or **effective**) if the set of its nonlogical axioms is decidable by an algorithm.

The three notions are independent, and the incompleteness theorem is a statement about the third: a recursively axiomatised consistent theory extending arithmetic cannot be complete.

### Soundness

**Theorem (soundness).** Let $T$ be a theory. If $T \vdash \varphi$ then every model of $T$ satisfies $\varphi$; in particular, if $\vdash \varphi$ then $\varphi$ is valid.

**Proof.** Induction on the length of the derivation. Each logical axiom is valid — the propositional tautologies, the equality axioms and the quantifier axioms are checked directly — and each inference rule preserves the property of being satisfied in a model: if $\mathcal{M} \models \varphi$ and $\mathcal{M} \models \varphi \to \psi$ then $\mathcal{M} \models \psi$ by the satisfaction clause for the conditional; universal generalisation is sound because the variable generalised is not free in the hypotheses; and the remaining rules are checked the same way. Hence every formula in the derivation is satisfied by every model of $T$, and the conclusion is. $\square$

**Corollary.** If $T$ has a model then $T$ is consistent.

**Proof.** If $T \vdash \varphi$ and $T \vdash \neg\varphi$ then every model of $T$ satisfies both, which is impossible. $\square$

Soundness is the easy half of the correspondence between $\vdash$ and $\models$; the hard half is completeness, and it is the subject of the next section.

## Completeness, Compactness and Löwenheim–Skolem

### The Completeness Theorem

**Theorem (Gödel completeness).** Let $T$ be a theory in a countable first-order language and let $\varphi$ be a sentence. If $T \models \varphi$ then $T \vdash \varphi$. Equivalently, if $T$ is consistent then $T$ has a model.

**Proof sketch (Henkin construction).** It suffices to prove the second form. Extend the language by countably many new constant symbols $c_0, c_1, \ldots$, one for each formula, and enumerate all formulas of the enlarged language. Build a maximal consistent theory $T^* \supseteq T$ in the enlarged language by going through the enumeration and adding, at each stage, either $\varphi$ or $\neg\varphi$, whichever keeps the theory consistent; such a choice is always possible, since if both choices were inconsistent then $T$ would prove $\neg\varphi$ and $\varphi$. When the formula added at a stage is $\exists x\,\psi(x)$, add also $\psi(c_i)$ for a constant $c_i$ that has not yet appeared, which is the **witness** of the existential statement; consistency is preserved because the constant is fresh. The resulting $T^*$ is maximal, consistent, and has witnesses. Form the **term model** whose elements are the closed terms of the enlarged language modulo the equivalence $t \sim s$ iff $T^* \vdash t = s$, and interpret the symbols in the evident way. Satisfaction is proved by induction on formulas using the maximality and the witnesses, so that $\mathcal{M} \models T^*$ and hence $\mathcal{M} \models T$. $\square$

The completeness theorem has a sharp form: if $T$ is recursively axiomatised, a derivation can be found **effectively** from a proof of unsatisfiability, and the set of valid sentences of a countable language is a computably enumerable set. This is the point at which logic meets computability, and it is the reason the undecidability results below are stated as statements about enumerable sets.

### Compactness

**Theorem (compactness).** Let $T$ be a theory. If every finite subset of $T$ has a model then $T$ has a model. Equivalently, if $T \models \varphi$ then $\Delta \models \varphi$ for some finite $\Delta \subseteq T$.

**Proof.** Assume every finite subset of $T$ has a model. Then every finite subset of $T$ is consistent, by soundness. A derivation is finite and uses only finitely many nonlogical axioms, so $T$ itself is consistent; by completeness $T$ has a model. The second form is the contrapositive of the first applied to $T \cup \{\neg\varphi\}$. $\square$

Compactness is the most used theorem of model theory, and the corpus uses it in the form of the existence of nonstandard models: the theory of arithmetic together with the sentences $c > 0, c > 1, c > 2, \ldots$ for a new constant $c$ is finitely satisfiable, hence satisfiable, giving a model of arithmetic containing an element larger than every numeral.

### The Löwenheim–Skolem Theorems

**Theorem (downward Löwenheim–Skolem).** Let $T$ be a theory in a countable language and suppose $T$ has a model. Then $T$ has a countable model. More generally, if $\kappa$ is an infinite cardinal at least the cardinality of the language and $T$ has a model, then $T$ has a model of cardinality at most $\kappa$.

**Proof sketch.** Given a model $\mathcal{M}$, take any subset $A \subseteq M$ of cardinality at most $\kappa$ and close it under the functions and constants of the language and under the choice of witnesses for the existential formulas satisfied in $\mathcal{M}$; the closure is of cardinality at most $\kappa$, and the substructure with domain the closure satisfies the same sentences with parameters from $A$, by the Tarski–Vaught criterion for elementary substructures. $\square$

**Theorem (upward Löwenheim–Skolem).** Let $T$ be a theory in a language of cardinality $\kappa$ and suppose $T$ has an infinite model. Then $T$ has a model of every cardinality $\lambda \geq \kappa$.

**Proof sketch.** Add $\lambda$ new constant symbols and the sentences $c_\alpha \neq c_\beta$ for $\alpha \neq \beta$; every finite subset of the resulting theory is satisfiable in the given infinite model, so by compactness the whole theory is satisfiable, and any model has cardinality at least $\lambda$; the downward theorem then gives one of cardinality exactly $\lambda$. $\square$

The two theorems together give the **Löwenheim–Skolem paradox**: a first-order theory with an infinite model has models of every infinite cardinality, so no first-order theory can characterise an infinite structure up to isomorphism, and a theory with an infinite model has countable models. The paradox is not a contradiction: a countable model is countable *in the metatheory*, while a statement such as "every bounded subset has a least upper bound" is interpreted internally, over the subsets of the model that the model can see, of which there may be only countably many.

## Computability

### Turing Machines

**Definition.** A **Turing machine** consists of a finite set $Q$ of **states** containing a distinguished **initial state** $q_0$ and a **halting state** $q_{\mathrm{h}}$; a finite **tape alphabet** $\Gamma$ containing a distinguished **blank symbol** $\square$ and a distinguished **input symbol** $1$; and a **transition function**

$$
\delta : (Q \setminus \{q_{\mathrm{h}}\}) \times \Gamma \to Q \times \Gamma \times \{L, R\}.
$$

The machine operates on a **tape**, a function $\mathbb{Z} \to \Gamma$ that is blank outside a finite set, with a **head** at a position; a **configuration** is a triple (state, tape, head position). At each step, if the machine is in state $q$ reading symbol $a$, and $\delta(q,a) = (q', b, D)$, it writes $b$, moves the head one cell in direction $D$, and enters state $q'$. The machine **halts** when it reaches $q_{\mathrm{h}}$, and the output is the content of the tape.

The input is written on the tape as a block of $1$s with the head at its left end, and the machine is started in $q_0$. A partial function $f : \mathbb{N}^k \dashrightarrow \mathbb{N}$ is **Turing-computable** if there is a machine which, started on the input written in unary with the arguments separated by blanks, halts with the value of $f$ written in unary precisely when $f$ is defined at that input.

**Example (successor).** Let $Q = \{q_0, q_{\mathrm{h}}\}$, $\Gamma = \{\square, 1\}$, and let $\delta(q_0, 1) = (q_0, 1, R)$, $\delta(q_0, \square) = (q_{\mathrm{h}}, 1, R)$. Started on $1^n$, the machine moves right across the block of $n$ ones, writes a $1$ in the blank cell to its right, and halts; the tape holds $1^{n+1}$. The machine computes the successor function.

**Example (addition).** Let $Q = \{q_0, q_1, q_2, q_{\mathrm{h}}\}$ and $\Gamma = \{\square, 1\}$, with

$$
\delta(q_0,1)=(q_0,1,R), \quad \delta(q_0,\square)=(q_1,1,R), \quad \delta(q_1,1)=(q_1,1,R),
$$

$$
\delta(q_1,\square)=(q_2,\square,L), \quad \delta(q_2,1)=(q_{\mathrm{h}},\square,R).
$$

Started on $1^n\square 1^m$ with the head at the left end, the machine scans the first block in $q_0$, replaces the separating blank by a $1$, scans the second block in $q_1$, steps left onto the last $1$, and erases it in $q_2$. The tape then holds $1^n\,1\,1^{m-1} = 1^{n+m}$, and the cases $n = 0$ and $m = 0$ are read from the same instructions, a block of length $0$ being simply absent. Thus the machine computes addition.

### Recursive Functions

An equivalent formalism defines the computable functions from the natural numbers by closure conditions.

**Definition.** The **primitive recursive functions** are the least class of functions $\mathbb{N}^k \to \mathbb{N}$ containing the constant functions, the successor $S(n) = n+1$ and the projections $\pi_i^k(x_1,\ldots,x_k) = x_i$, and closed under **composition** $h(\vec x) = f(g_1(\vec x), \ldots, g_m(\vec x))$ and **primitive recursion**

$$
h(\vec x, 0) = f(\vec x), \qquad h(\vec x, n+1) = g(\vec x, n, h(\vec x, n)).
$$

The **recursive** (or **$\mu$-recursive**, or **partial recursive**) functions are obtained by adding the **minimisation** operator: if $g(\vec x, y)$ is recursive then so is the function $f(\vec x) = \mu y\,[g(\vec x,y) = 0]$, the least $y$ with $g(\vec x, y) = 0$, undefined if there is none. A function is **total recursive** if it is recursive and defined everywhere.

**Theorem.** A partial function $\mathbb{N}^k \dashrightarrow \mathbb{N}$ is Turing-computable if and only if it is recursive.

The theorem is proved by arithmetising the configurations of a Turing machine: a computation is a finite sequence of configurations, and both "the sequence is a valid computation" and "it terminates in a halting configuration with the given output" are primitive recursive predicates on numbers. The converse — that every recursive function is Turing-computable — is by constructing machines for the initial functions and composing them. The equivalence is the basis of **Church's thesis**, the identification of the mathematically precise notion of recursive (equivalently, Turing-computable) with the informal notion of effectively computable. The thesis is not a theorem, since the informal notion is not formal, but every proposed formalisation has proved equivalent to it, and the corpus adopts it.

### Computable and Computably Enumerable Sets

**Definition.** A set $A \subseteq \mathbb{N}$ is **decidable** (or **recursive**, or **computable**) if its characteristic function $\chi_A$ is computable; it is **computably enumerable** (c.e., or **recursively enumerable**) if $A$ is empty or is the range of a total computable function, equivalently if $A$ is the set of numbers on which some Turing machine halts.

**Proposition.** Every decidable set is computably enumerable, and the class of decidable sets is closed under complement, finite union and finite intersection; the class of c.e. sets is closed under finite union and intersection but not under complement.

**Proof sketch.** If $A$ is decidable and nonempty, fix $a \in A$ and enumerate the range of a machine that scans $n = 0, 1, 2, \ldots$ and prints $n$ when $\chi_A(n) = 1$ and prints $a$ otherwise; the numbers printed are exactly the elements of $A$. Complement and Boolean combinations are computed by combining the machines. That the c.e. sets are not closed under complement is the content of the undecidability of the halting problem, below. $\square$

The standard **dovetailing** construction — running computations on all inputs in parallel, one step at a time — is the technique behind every closure property of the c.e. sets, and it is used without comment in the proofs below.

## Undecidability

### The Halting Problem

**Theorem (Turing).** The **halting set**

$$
K = \{\langle M, x\rangle : \text{the Turing machine } M \text{ halts on input } x\}
$$

is computably enumerable but not decidable.

**Proof.** $K$ is c.e. because a machine runs $M$ on $x$ and halts exactly when $M$ does. Suppose for contradiction that $K$ were decidable, so that a machine $H$ decides membership in $K$. Define a machine $D$ which, on input $\langle M\rangle$ encoding a machine $M$, runs $H$ on $\langle M, \langle M\rangle\rangle$; if $H$ reports that $M$ halts on $\langle M\rangle$, the machine $D$ enters a loop and never halts, while if $H$ reports that $M$ does not halt on $\langle M\rangle$, the machine $D$ halts and outputs $1$. Then for every machine $M$,

$$
D \text{ halts on } \langle M \rangle \iff M \text{ does not halt on } \langle M \rangle.
$$

Taking $M = D$ gives $D$ halts on $\langle D\rangle$ precisely when $D$ does not halt on $\langle D\rangle$, a contradiction. Hence no such $H$ exists and $K$ is undecidable. $\square$

The argument is the diagonal argument in the setting of computations: the machine $D$ is built so as to disagree with each $M$ at the input $\langle M\rangle$, exactly as Cantor's set $D$ disagrees with each $h(x)$ at $x$.

**Corollary.** The complement of $K$ is not c.e., since a set and its complement that are both c.e. are decidable (run the two enumerations in parallel).

### Undecidable Problems

**Definition.** A **decision problem** is a set $A \subseteq \mathbb{N}$; it is **decidable** if $A$ is decidable and **undecidable** otherwise. A problem $A$ **reduces** to $B$, written $A \leq_{\mathrm{m}} B$, if there is a total computable $f$ with $n \in A \iff f(n) \in B$; if $A$ is undecidable and $A \leq_{\mathrm{m}} B$ then $B$ is undecidable.

**Theorem.** The following decision problems are undecidable.

1. **The halting problem**: whether a given machine halts on a given input.
2. **The uniform halting problem**: whether a given machine halts on every input.
3. **The Post correspondence problem**: whether a finite list of pairs of words over a finite alphabet admits a finite matching sequence; a matching sequence is verified by a computation, and the search for one simulates a machine.
4. **The Entscheidungsproblem**: whether a given first-order sentence is valid.

**Proof sketch.** (1) is the theorem above. (2) reduces the halting problem to the uniform one by a machine that runs a fixed input. (3) is proved by an explicit reduction from the halting problem, exhibiting for each machine a finite list of word pairs whose matching sequences encode the halting computations. (4) follows from the completeness theorem and the arithmetisation of the halting problem: the assertion that a machine halts on an input is an arithmetic sentence, and a machine for deciding validity would decide the halting problem. $\square$

**Remark.** The situation for fragments of first-order logic is delicate. The validity problem for a language with a single binary predicate and no function symbols is undecidable, but for languages with only unary predicates and no function symbols it is decidable, and the decidability of a theory is often the content of a quantifier-elimination theorem. This is the substance, where the decidability of the theories of algebraically closed fields and of real-closed fields is proved by exactly that route.

## Gödel's Incompleteness Theorems

### Arithmetisation of Syntax

The incompleteness theorems concern formal systems that can express elementary arithmetic. Let **Peano arithmetic** (PA) be the theory in the language $\{0, 1, +, \cdot, <\}$ with the usual axioms for the successor, addition, multiplication and order, together with the induction schema: for every formula $\varphi(x, \vec y)$,

$$
\varphi(0,\vec y) \wedge \forall x\,(\varphi(x,\vec y) \to \varphi(x+1,\vec y)) \to \forall x\,\varphi(x,\vec y).
$$

The theory PA is recursively axiomatised, since the induction schema is a decidable set of axioms, and it expresses the arithmetic of $\mathbb{N}$.

**Theorem (arithmetisation).** With each formula $\varphi$ and each derivation one can associate, by a computable procedure, a natural number (its **Gödel number**) in such a way that the syntactic properties of formulas and derivations — being a formula, being an axiom of PA, being a derivation of $\varphi$ from PA — become primitive recursive predicates of their Gödel numbers.

**Proof sketch.** Assign numbers to symbols by an explicit coding, to strings by coding the sequence of symbol numbers (for instance by the prime factorisation of a product of prime powers, or by the Cantor pairing of *Cardinality and the Axiom of Choice*), and to sequences of strings recursively. Being a well-formed formula is then a primitive recursive predicate, because it is defined by a finite grammar with bounded recursion; the property of being an instance of an axiom schema is primitive recursive because the schema has finitely many patterns and the induction schema is indexed by formulas. $\square$

**Definition.** A theory $T$ is **$\Sigma_1$-complete** if it proves every true $\Sigma_1$ sentence, that is, every true statement of the form "there exists $n$ with $P(n)$" for a primitive recursive $P$. Peano arithmetic is $\Sigma_1$-complete, because a terminating computation can be verified step by step inside it.

**Remark.** Gödel's original proof assumed the stronger hypothesis that $T$ is **$\omega$-consistent**: there is no formula $\varphi(x)$ with $T \vdash \exists x\,\varphi(x)$ while $T \vdash \neg\varphi(\bar n)$ for every numeral $\bar n$. The proof below uses only $\Sigma_1$-completeness, which is weaker and is the hypothesis of the theorem in its usual modern form; Rosser's refinement removes the extra hypothesis altogether by comparing the Gödel numbers of a putative proof and a putative refutation.

### The First Incompleteness Theorem

**Definition.** A theory $T$ in the language of arithmetic is **adequate** if it is recursively axiomatised, contains PA (or at least a weak fragment sufficient for the arithmetisation), and its set of theorems is $\Sigma_1$-complete.

**Theorem (Gödel, first incompleteness theorem).** Let $T$ be a consistent, recursively axiomatised theory adequate for arithmetic. Then $T$ is incomplete: there is a sentence $G$ such that neither $T \vdash G$ nor $T \vdash \neg G$.

**Proof sketch.** Arithmetise syntax, and consider the primitive recursive predicate $\mathrm{Pr}_T(m, n)$ asserting that $m$ is the Gödel number of a derivation of the formula with number $n$, and the $\Sigma_1$ formula $\exists m\,\mathrm{Pr}_T(m,n)$ asserting provability, written $\mathrm{Prov}_T(n)$. By the **diagonal lemma**, for every formula $\psi(x)$ there is a sentence $\sigma$ with

$$
T \vdash \sigma \leftrightarrow \psi(\#\sigma),
$$

where $\#\sigma$ is the numeral of the Gödel number of $\sigma$; the lemma is proved by substituting the Gödel number of the formula into itself, exactly the diagonal construction of Cantor's theorem and of the halting problem. Apply it to $\psi(x) = \neg\mathrm{Prov}_T(x)$, obtaining a sentence $G$ with

$$
T \vdash G \leftrightarrow \neg \mathrm{Prov}_T(\# G).
$$

If $T \vdash G$, then $T$ proves that $G$ is provable, that is, $T \vdash \mathrm{Prov}_T(\# G)$, and then $T \vdash \neg G$ by the equivalence, contradicting consistency. If $T \vdash \neg G$, then $T \vdash \mathrm{Prov}_T(\# G)$, so that a derivation of $G$ exists by $\Sigma_1$-completeness, and $T \vdash G$, again contradicting consistency. Hence neither, and $T$ is incomplete. $\square$

The sentence $G$ is a **Gödel sentence**: it asserts its own unprovability. It is true in the standard model $\mathbb{N}$ — because it is indeed unprovable — and hence not provable; this is the sense in which PA is incomplete rather than merely unable to decide a question.

**Corollary.** The sentence $G$ is true in $\mathbb{N}$ and independent of PA.

**Corollary.** The set of sentences true in $(\mathbb{N}, +, \cdot)$ is not recursively axiomatisable, and the theory of arithmetic is undecidable (Church). Consequently there is no algorithm deciding the truth of arithmetic sentences.

### The Second Incompleteness Theorem

**Definition.** Let $\mathrm{Con}_T$ be the sentence $\neg \mathrm{Prov}_T(\#(0=1))$, asserting that $T$ does not prove the contradiction $0 = 1$; it is the arithmetised consistency statement of $T$.

**Theorem (Gödel, second incompleteness theorem).** Let $T$ be a recursively axiomatised theory adequate for arithmetic. If $T$ is consistent, then $T \nvdash \mathrm{Con}_T$.

**Proof sketch.** The proof of the first theorem can be formalised inside $T$, because all the syntactic manipulations are primitive recursive. The formalisation yields

$$
T \vdash \mathrm{Con}_T \to G,
$$

where $G$ is the Gödel sentence. If $T \vdash \mathrm{Con}_T$ then $T \vdash G$, contradicting the first theorem. Hence $T$ does not prove its own consistency. $\square$

The second theorem is the reason consistency cannot be established by elementary means inside the theory: a consistency proof must use principles stronger than the theory, and the **consistency strength** of a theory is measured by which such principles are needed. It is consistent with the theorem that the consistency of PA is provable in ZFC, or in PA together with the assertion that a certain well-ordering is well founded; what is impossible is a proof that can be formalised in PA itself.

**Theorem (Tarski).** The set of Gödel numbers of the sentences true in $(\mathbb{N}, +, \cdot)$ is not definable in $(\mathbb{N}, +, \cdot)$.

**Proof sketch.** If a formula $\mathrm{Tr}(x)$ defined truth, the diagonal lemma applied to $\neg\mathrm{Tr}(x)$ would give a sentence $\lambda$ with $\lambda \leftrightarrow \neg\mathrm{Tr}(\#\lambda)$, which is the liar paradox in formal dress, and it is unsatisfiable. $\square$

## Summary

A first-order language, its terms and formulas, and a formal system of axioms and rules are the syntactic material of the article; $T \vdash \varphi$ means that $\varphi$ has a derivation from $T$, and a derivation is a finite object, so a theory uses only finitely many axioms in each derivation. A theory is consistent when it proves no contradiction, complete when it decides every sentence, and recursively axiomatised when its axioms can be listed by an algorithm. Soundness, proved by induction on derivations, says that derivability implies satisfaction in every model, and hence that a theory with a model is consistent.

The completeness theorem of Gödel says that every consistent theory has a model, and is proved by the Henkin construction of a maximal consistent theory with witnesses and its term model. Compactness is its immediate corollary: a theory is satisfiable if every finite subset is. The Löwenheim–Skolem theorems say that a theory with an infinite model has models of every infinite cardinality at least that of its language, so no first-order theory catches a structure up to isomorphism and every theory of the reals has a countable model.

A Turing machine is a finite table of instructions acting on a tape; a function is Turing-computable when some machine computes it, and equivalently when it is recursive, built from the initial functions by composition, primitive recursion and minimisation. Church's thesis identifies these with the effectively computable functions. Decidable sets have computable characteristic functions, c.e. sets are the ranges of computable functions, and the halting set is c.e. but not decidable, by a diagonal argument over machines; consequently the word problem for groups with unsolvable word problem and the Entscheidungsproblem are undecidable.

Peano arithmetic is the recursively axiomatised theory of the natural numbers. Its syntax can be arithmetised, so that provability becomes a $\Sigma_1$ formula and the diagonal lemma produces a sentence asserting its own unprovability; if the theory is consistent this sentence is neither provable nor refutable, which is the first incompleteness theorem, and the arithmetised statement of consistency is not provable in the theory, which is the second. Tarski's theorem adds that truth in the standard model is not definable in it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{L}$ | A first-order language |
| $T \vdash \varphi$ | $\varphi$ is derivable from the theory $T$ |
| $T \models \varphi$ | $\varphi$ is satisfied in every model of $T$ |
| $T$, $\Delta$ | Theory (set of sentences); finite subtheory |
| $\mathrm{Con}_T$ | Arithmetised consistency of $T$: $\neg\mathrm{Prov}_T(\# 0=1)$ |
| $Q$, $\Gamma$, $\delta$ | States, tape alphabet, transition function of a Turing machine |
| $q_0$, $q_{\mathrm{h}}$, $\square$ | Initial state, halting state, blank symbol |
| $L$, $R$ | Head moves left and right |
| $\langle M, x\rangle$, $\langle M\rangle$ | Codes of a machine with input, and of a machine |
| $K$ | Halting set: $\{\langle M,x\rangle : M \text{ halts on } x\}$ |
| $\leq_{\mathrm{m}}$ | Many-one reduction of decision problems |
| PA | Peano arithmetic |
| $\#\varphi$, $\bar n$ | Gödel number of $\varphi$; numeral of a number |
| $\mathrm{Prov}_T(x)$ | Arithmetised provability in $T$ |
| $G$ | Gödel sentence, asserting its own unprovability |
| c.e. | Computably enumerable |







## Further Reading

- Kurt Gödel, "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I", *Monatshefte für Mathematik und Physik* **38** (1931), 173–198, for the incompleteness theorems and the arithmetisation of syntax.
- Alan M. Turing, "On computable numbers, with an application to the Entscheidungsproblem", *Proceedings of the London Mathematical Society* **42** (1936), 230–265, for Turing machines, the halting problem and the undecidability of first-order logic.
- Stephen Cole Kleene, *Introduction to Metamathematics* (Van Nostrand, 1952), for recursive functions, the equivalence with Turing computability and the arithmetisation.
- Herbert B. Enderton, *A Mathematical Introduction to Logic*, 2nd ed. (Academic Press, 2001), for the completeness, compactness and Löwenheim–Skolem theorems with full proofs.
- Martin Davis, *Computability and Unsolvability* (McGraw-Hill, 1958; reprinted Dover, 1982), for decision problems, reductions and undecidability.
- Hartley Rogers Jr., *Theory of Recursive Functions and Effective Computability* (McGraw-Hill, 1967), for the systematic theory of recursive functions and computably enumerable sets.
- Petr Hájek and Pavel Pudlák, *Metamathematics of First-Order Arithmetic* (Springer, 1993), for the fine structure of Peano arithmetic, its fragments and the consistency statements.
