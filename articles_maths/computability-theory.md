
# __Computability Theory__

## Introduction

This is the third article of the Natural Numbers system in Part V, and it occupies the **algebra slot** of that system in its effective aspect. The system is again the structure $\mathbb{N}$ of *The Natural Numbers*, and the object of study is the class of functions $\mathbb{N}^k \to \mathbb{N}$ that can be computed by a finite procedure, together with the sets and the reducibility relations that this class induces. Where *Peano Arithmetic and Model Theory* studied the sentences true of $\mathbb{N}$ and the incompleteness of any recursive axiomatisation, this article studies the *effective* content of $\mathbb{N}$: which functions are computable, which sets are decidable or recursively enumerable, and how the undecidable sets are stratified by the arithmetical hierarchy and by the Turing degrees.

The general theory of computation — Turing machines, the universal machine, the Church–Turing thesis, the halting problem in its machine form — is the subject of Part I's *Formal Logic and Computability*, and is used here rather than developed; the incompleteness theorems and the arithmetisation of syntax are from *Proof Theory and Type Theory* and from *Peano Arithmetic and Model Theory*. What is developed here is the *synthetic* theory of the computable functions on $\mathbb{N}$: the primitive recursive and recursive definitions, the enumeration $\varphi_e$ of the partial recursive functions, the recursion theorems, the recursively enumerable sets and their completeness, and the two standard stratifications, the arithmetical hierarchy and the Turing degrees. The material on Diophantine equations connects to the model theory of the previous article; the combinatorial functions on $\mathbb{N}$ are not covered here.

Throughout, computability is that of *Formal Logic and Computability*: a function is **computable**, or **recursive**, if some Turing machine computes it. The partial recursive functions are enumerated as $\varphi_0, \varphi_1, \varphi_2, \dots$, with $W_e = \operatorname{dom}(\varphi_e)$ the $e$-th **recursively enumerable** (c.e.) set, and $\varphi_e(n)\!\downarrow$ means that the computation halts. The set $K$ is the halting set $\{e : \varphi_e(e)\!\downarrow\}$, and $\emptyset'$ is its Turing degree. Reducibilities are written $\leq_m$ and $\leq_T$, and $\emptyset^{(n)}$ is the $n$-th Turing jump of $\emptyset$.

## Recursive Functions

### Primitive Recursion

**Definition.** The **primitive recursive functions** are the smallest class of partial functions $\mathbb{N}^k \to \mathbb{N}$ containing

$$
Z(n) = 0, \qquad S(n) = n+1, \qquad P^k_i(n_1,\dots,n_k) = n_i,
$$

and closed under **composition**, $h(\bar x) = f(g_1(\bar x),\dots,g_m(\bar x))$, and **primitive recursion**,

$$
h(\bar x, 0) = f(\bar x), \qquad h(\bar x, S n) = g(\bar x, n, h(\bar x, n)).
$$

A relation $R \subseteq \mathbb{N}^k$ is **primitive recursive** if its characteristic function is.

**Theorem.** The primitive recursive functions are total and computable, and they are closed under the bounded operations: if $f$ is primitive recursive then so are

$$
\sum_{i \leq n} f(\bar x, i), \qquad \prod_{i \leq n} f(\bar x, i), \qquad \max_{i \leq n} f(\bar x, i), \qquad \min_{i \leq n} f(\bar x, i),
$$

and bounded quantification over primitive recursive relations yields primitive recursive relations.

**Proof.** Each bounded operation is defined by primitive recursion on $n$, and bounded quantification is the bounded sum or product of the characteristic function; the closure of the class under composition and primitive recursion then gives the result. $\square$

**Example.** Addition, multiplication, exponentiation, the factorial, the binomial coefficients, the prime-counting function, the $n$-th prime $p_n$ and the decoding functions of a Gödel numbering are primitive recursive. The pairing function $\langle m, n\rangle = \tfrac12 (m+n)(m+n+1) + m$ and its two inverses are primitive recursive, so finite sequences of natural numbers can be coded by single natural numbers within the class.

**Theorem (Ackermann).** Define $A : \mathbb{N}^2 \to \mathbb{N}$ by

$$
A(0, n) = n + 1, \qquad A(S m, 0) = A(m, 1), \qquad A(S m, S n) = A(m, A(S m, n)).
$$

Then $A$ is total and computable but not primitive recursive.

**Proof.** Totality and computability are by nested recursion. If $A$ were primitive recursive, then so would be the diagonal function $d(n) = A(n,n)$, and one shows by induction on the definition that every primitive recursive function is eventually dominated by $A(m, \cdot)$ for some fixed $m$; but $d$ is not dominated by any $A(m,\cdot)$, since $d(n) = A(n,n) > A(m,n)$ for $n > m$ by the monotonicity of $A$ in its first variable. The domination proof is a routine induction on the clauses defining the primitive recursive functions. $\square$

### Partial Recursion and the Church–Turing Thesis

**Definition.** The **partial recursive functions** are the smallest class containing the primitive recursive functions and closed under **unbounded search**: if $g(\bar x, n)$ is partial recursive and total in its last argument whenever it is defined, then

$$
f(\bar x) = \mu n\, (g(\bar x, n) = 0),
$$

the least $n$ with $g(\bar x, n) = 0$, is partial recursive; the search diverges when no such $n$ exists.

**Theorem (Church–Turing).** A partial function $\mathbb{N}^k \to \mathbb{N}$ is partial recursive if and only if it is computable by a Turing machine. This identification is the **Church–Turing thesis**; it is a thesis because it identifies a formal class with an informal notion.

**Proof.** The direction from machines to functions is a simulation of a machine by primitive recursion on its configurations, with unbounded search for the halting time; the other direction is the encoding of the recursion scheme by a machine. Both simulations are carried out in *Formal Logic and Computability*. $\square$

**Theorem (Kleene normal form).** There is a primitive recursive predicate $T(e, x, s)$ and a primitive recursive function $U$ such that

$$
\varphi_e(x) \simeq U(\mu s\, T(e, x, s)),
$$

where $\simeq$ means equality of partial functions and the search diverges exactly when $\varphi_e(x)$ diverges. In particular the enumeration $\varphi_e$ is itself partial recursive, the universal function $\Phi(e,x) = \varphi_e(x)$ being partial recursive and not total.

**Proof.** $T(e,x,s)$ asserts that $s$ codes a halting computation of the $e$-th machine on input $x$, and $U$ extracts the output; both are primitive recursive by the arithmetisation of *Formal Logic and Computability*, and the definition of $\varphi_e$ is the displayed search. The universal function is partial recursive because it is defined by this formula, and not total because of the existence of a halting problem. $\square$

### The Recursion Theorem

**Theorem (Kleene recursion theorem).** For every total computable function $f : \mathbb{N} \to \mathbb{N}$ there is an index $e$ with

$$
\varphi_e = \varphi_{f(e)} .
$$

**Proof.** By the $s$-$m$-$n$ theorem there is a primitive recursive function $s$ with $\varphi_{s(e)}(x) = \varphi_e(e,x)$. Define the total computable function $h(e) = f(s(e))$ and let $v$ be an index of $h$, so that $\varphi_v(e) = h(e)$ for all $e$. Put $e_0 = s(v)$. Then

$$
\varphi_{e_0}(x) = \varphi_{s(v)}(x) = \varphi_v(v,x) = h(v) = f(s(v)) = f(e_0),
$$

so $\varphi_{e_0} = \varphi_{f(e_0)}$. The computation is Kleene's and uses only the $s$-$m$-$n$ theorem and the totality of $f$. $\square$

**Corollary (self-reference).** There is an index $e$ with $\varphi_e$ the function that prints $e$, that is, the constant function with value $e$; more generally, every computable transformation of programs has a fixed point in the sense of the theorem. This is the precise form of the diagonal construction that underlies the incompleteness theorems.

## Recursively Enumerable Sets

### Decidability and Semi-Decidability

**Definition.** A set $A \subseteq \mathbb{N}$ is **decidable** (recursive) if its characteristic function is computable, and **recursively enumerable** (c.e.) if $A = W_e = \operatorname{dom}(\varphi_e)$ for some $e$, equivalently if $A$ is the range of a partial recursive function, equivalently if a machine lists the elements of $A$ without ever listing a non-element.

**Theorem.** A set $A$ is c.e. if and only if it is empty or it is the range of a total computable function. A set is decidable if and only if it and its complement are both c.e.

**Proof.** If $W_e$ is nonempty, choose $a \in W_e$ and enumerate pairs $(n,s)$ by a primitive recursive bijection; the machine simulates the $e$-th machine for $s$ steps on $n$ and outputs $n$ when it halts, and outputs $a$ otherwise. This gives a total computable function with range $W_e$, and the converse is immediate. For the second statement, if $A$ and its complement are c.e. one decides $A$ by running the two enumerations in parallel; the converse is clear. $\square$

**Theorem (halting problem).** The set $K = \{e : \varphi_e(e)\!\downarrow\}$ is c.e. but not decidable, and there is no total computable function deciding, for given $e$ and $x$, whether $\varphi_e(x)$ converges.

**Proof.** $K$ is c.e. because it is the domain of the partial recursive function $e \mapsto \varphi_e(e)$. If $K$ were decidable with characteristic function $k$, the function

$$
g(e) = \begin{cases} \varphi_e(e) + 1, & k(e) = 1, \\ 0, & k(e) = 0 \end{cases}
$$

would be total computable, and for an index $e_0$ of $g$ one has $g = \varphi_{e_0}$. If $k(e_0) = 1$ then $\varphi_{e_0}(e_0)$ converges and $g(e_0) = \varphi_{e_0}(e_0) + 1 \neq \varphi_{e_0}(e_0)$, a contradiction; if $k(e_0) = 0$ then $\varphi_{e_0}(e_0)$ diverges while $g(e_0) = 0$ is defined, again a contradiction. The uniform statement follows by a parametrised version of the argument. $\square$

**Theorem (Rice).** Let $\mathcal{C}$ be a class of partial recursive functions containing some but not all of them. Then the index set $\{e : \varphi_e \in \mathcal{C}\}$ is undecidable.

**Proof.** If the index set were decidable one could decide whether $\varphi_e$ is the everywhere undefined function, contradicting the halting problem; the reduction is the standard one and is in *Formal Logic and Computability*. $\square$

### m-Completeness

**Definition.** For sets $A, B \subseteq \mathbb{N}$ one writes $A \leq_m B$ if there is a total computable $f$ with $n \in A \iff f(n) \in B$, and $A \equiv_m B$ if both $A \leq_m B$ and $B \leq_m A$. A set $B$ is **m-complete** for the c.e. sets if $B$ is c.e. and $A \leq_m B$ for every c.e. $A$.

**Theorem.** The halting set $K$ is m-complete for the c.e. sets, and every m-complete set is undecidable. The c.e. sets are exactly the sets that are empty or the range of a total computable function, and they form a lattice under union and intersection.

**Proof.** Given a c.e. set $A = W_e$, the reduction $n \mapsto \langle e, n\rangle$ (with $\langle e,n\rangle$ coded so that the machine for $\langle e,n\rangle$ simulates the $e$-th machine on $n$) witnesses $A \leq_m K$; the undecidability follows from that of $K$. Closure under union and intersection is by the parallel simulation of the two enumerations. $\square$

**Theorem (Myhill).** If $A \equiv_m B$ then $A$ and $B$ are isomorphic by a total computable bijection.

**Proof.** The isomorphism is built by a back-and-forth construction in which each step uses the two reductions to match the least unmatched element of one set with an unmatched element of the other; the construction is effective because the reductions are total computable. The details are Myhill's. $\square$

## The Arithmetical Hierarchy and the Turing Degrees

### The Arithmetical Hierarchy

**Definition.** A set $A \subseteq \mathbb{N}$ is $\Sigma_n$ if it is definable by a formula of $\mathcal{L}_A$ of the arithmetical hierarchy with $n$ unbounded existential quantifier blocks, and $\Pi_n$ if it is definable by the dual class; $\Delta_n = \Sigma_n \cap \Pi_n$.

**Theorem.** $\Sigma_1$ and $\Pi_1$ are the c.e. sets and their complements, and $\Delta_1$ is the class of decidable sets. For every $n$, $\Sigma_n \cup \Pi_n \subseteq \Delta_{n+1}$, and the inclusions are strict: there are sets that are $\Sigma_{n+1}$ but not $\Pi_{n+1}$.

**Proof.** The first statement is the normal form of Kleene together with the definition of the arithmetical hierarchy in *Peano Arithmetic and Model Theory*. The inclusions follow by adding a vacuous quantifier, and strictness is witnessed by the $n$-th Turing jump $\emptyset^{(n)}$, which is $\Sigma_n$-complete and not $\Pi_n$ by the relativised halting argument. $\square$

**Theorem (Post).** For every set $A$, a set $B$ is $\Sigma_{n+1}$ in $A$ if and only if $B$ is c.e. in the jump $A'$. In particular $B$ is $\Sigma_{n+1}$ if and only if $B$ is c.e. in $\emptyset^{(n)}$, and $\emptyset^{(n)}$ is $\Sigma_n$-complete.

**Proof.** The relativised normal form expresses $B$ by a $\Sigma_1$ formula over $A'$; the converse is the relativised halting problem. The argument is Post's and is standard. $\square$

**Theorem (Shoenfield limit lemma).** A set $A$ is $\Delta_2$, that is, both $\Sigma_2$ and $\Pi_2$, if and only if there is a total computable function $g(e, n)$ such that $\lim_e g(e,n)$ exists and equals the characteristic function of $A$ at $n$; equivalently, $A \leq_T \emptyset'$.

**Proof.** A $\Delta_2$ definition gives a limit of computable approximations, and conversely a computable approximation with a limit can be expressed in $\Sigma_2$ form. The equivalence with $\leq_T \emptyset'$ follows from Post's theorem at $n = 1$. $\square$

### Turing Reducibility and Degrees

**Definition.** $A \leq_T B$ if there is a machine with an oracle for $B$ that decides $A$; the **Turing degree** of $A$ is its equivalence class, and the set of degrees is written $\mathcal{D}$. The **join** $A \oplus B$ is the degree of $\{(2n : n \in A)\} \cup \{(2n+1 : n \in B)\}$, and the **Turing jump** is $A' = \{e : \varphi_e^A(e)\!\downarrow\}$.

**Theorem.** $\mathcal{D}$ is an upper semilattice with least element $\mathbf{0}$, the degree of the decidable sets, and the jump is strictly increasing and monotone: $A <_T A'$ and $A \leq_T B$ implies $A' \leq_T B'$. The jump operation satisfies $\emptyset^{(n+1)} = (\emptyset^{(n)})'$ and gives an increasing sequence of degrees.

**Proof.** The upper semilattice laws are by coding of finite sets of oracle queries; strictness of the jump is the relativised halting problem, and monotonicity is because a machine with oracle $B$ can simulate one with oracle $A$. The iteration of the jump is immediate from the definition. $\square$

**Theorem (Post's problem; Friedberg–Muchnik).** There exist c.e. sets $A$ and $B$ with $A \not\leq_T B$ and $B \not\leq_T A$; that is, the c.e. degrees are not linearly ordered by $\leq_T$. The c.e. degrees are dense, and they are not a lattice.

**Proof.** The construction builds $A$ and $B$ by a priority argument with requirements $A \neq \varphi_e^B$ and $B \neq \varphi_e^A$, meeting each requirement on a finite initial segment and preserving the finitely many restraints imposed by earlier requirements. The priority method is Friedberg's and Muchnik's; the density and non-lattice results are later refinements of the same method. $\square$

### Diophantine Sets

**Theorem (Matiyasevich, after Davis–Putnam–Robinson).** A set $A \subseteq \mathbb{N}$ is c.e. if and only if it is **Diophantine**: there is a polynomial $P(x, y_1, \dots, y_k)$ with integer coefficients such that

$$
n \in A \iff \exists y_1 \cdots \exists y_k \in \mathbb{N}\ P(n, y_1, \dots, y_k) = 0 .
$$

**Proof.** A Diophantine set is c.e. by searching for the witnesses. The converse, the MRDP theorem, is proved by showing that every c.e. set is Diophantine and then eliminating the bounded universal quantifier by a coding trick of Davis–Putnam–Robinson; the argument is in the references. $\square$

**Corollary (Hilbert's tenth problem).** There is no algorithm deciding, for an arbitrary polynomial with integer coefficients, whether it has a solution in natural numbers; more generally the decision problem for Diophantine equations is undecidable, and this is the effective counterpart of the incompleteness phenomena of *Peano Arithmetic and Model Theory*.

## Kolmogorov Complexity and Randomness

### Description Complexity

**Definition.** Fix a universal partial recursive function $U$ with prefix-free domain. The **prefix-free Kolmogorov complexity** of a finite binary string $x$ is

$$
K(x) = \min\{\lvert p\rvert : U(p) = x\},
$$

the length of the shortest program that prints $x$ and halts, and the **conditional complexity** $K(x \mid y)$ is defined by the same formula with the machine given $y$ as an auxiliary input.

**Theorem (invariance).** The definition is machine-independent up to an additive constant: if $U$ and $V$ are universal prefix-free machines, then there is $c$ with $\lvert K_U(x) - K_V(x)\rvert \leq c$ for all $x$. Consequently one writes $K(x)$ and treats the choice of the universal machine as fixed.

**Proof.** The universality of $U$ means that some program $p_0$ simulates $V$; prefixing $p_0$ to a shortest $V$-program for $x$ gives a $U$-program for $x$ whose length exceeds the bound by the constant $\lvert p_0\rvert$, and the symmetry of the argument gives the reverse inequality. $\square$

**Theorem.** There is a constant $c$ such that for every $n$ all but at most $2^{n-c}$ of the $2^n$ strings of length $n$ satisfy $K(x) \geq n - c$. No partial recursive function computes $K$. In fact the set $\{x : K(x) \geq n\}$ is not decidable uniformly in $n$, and $K$ is not bounded below by any computable function on all strings.

**Proof.** There are $2^n$ strings of length $n$ but fewer than $2^{n-c}$ programs of length less than $n-c$, so most strings are incompressible. A computable bound on $K$ would compute the halting problem, since $K(x)$ large for a suitably designed $x$ rules out a halting computation of bounded length; the undecidability follows from the halting problem. $\square$

### Algorithmic Randomness

**Definition.** A real number $\alpha \in [0,1]$ is **left-computably enumerable** if there is a recursive sequence of rationals increasing to $\alpha$; the **halting probability** of a prefix-free universal machine $U$ is

$$
\Omega = \sum_{p : U(p)\ \text{halts}} 2^{-\lvert p\rvert},
$$

the measure of the set of programs on which $U$ halts.

**Theorem (Chaitin).** $\Omega$ is left-computably enumerable, $\Omega \in (0,1)$, and the halting problem is Turing reducible to $\Omega$: a program $p$ halts if and only if it appears in the computable enumeration of the halting programs once $\Omega$ is known to sufficient precision, and conversely the halting problem enumerates the terms of the series. Consequently $\Omega$ is not computable, and $\Omega \equiv_T \emptyset'$.

**Proof.** The sum is the limit of a recursive increasing sequence of rationals because the halting programs are enumerable; knowing $\Omega$ to sufficient precision decides halting, and conversely the halting problem enumerates the terms, giving the Turing equivalence with the halting set. The argument is in the references. $\square$

**Definition (Martin-Löf).** A sequence $X \in 2^{\mathbb{N}}$ is **Martin-Löf random** if it is not contained in any effective null set: for every uniformly recursively enumerable sequence of open sets $U_n \subseteq 2^{\mathbb{N}}$ with measure at most $2^{-n}$, the sequence lies outside $\bigcap_n U_n$.

**Theorem (Schnorr; Levin).** A sequence $X$ is Martin-Löf random if and only if there is $c$ such that $K(X_1 X_2 \cdots X_n) \geq n - c$ for every $n$: the random sequences are exactly those whose initial segments are incompressible. Moreover $\Omega$ is Martin-Löf random, no Martin-Löf random sequence is computable, and the set of Martin-Löf random sequences has measure $1$.

**Proof.** An effective null set gives a computable way of compressing the initial segments of its elements, and conversely a short description of a long initial segment defines an effective null set containing $X$; the randomness of $\Omega$ is Chaitin's theorem. The details are in the references. $\square$

**Remark.** Kolmogorov complexity is the measure of information content of a finite object, and it gives a definition of randomness that is purely mathematical: a sequence is random when it has no short description. It is the computability-theoretic counterpart of the measure-theoretic probability of Part III, and it is the sharpest form of the statement that almost every sequence is incompressible, since the failure of compressibility is exactly the failure of the sequence to be computable or to lie in an effective null set.

## Summary

The primitive recursive functions are built from the zero, successor and projection functions by composition and primitive recursion; they are total and computable and are closed under bounded sums, products and quantification, and they include addition, multiplication, exponentiation, the factorial, the binomial coefficients and the coding functions for finite sequences. The Ackermann function is total and computable but not primitive recursive, so primitive recursion is strictly weaker than computability. Adding unbounded search gives the partial recursive functions, which by the Church–Turing thesis are exactly the Turing-computable partial functions; Kleene's normal form expresses every partial recursive function as $U(\mu s\, T(e,x,s))$ with $T$ and $U$ primitive recursive, and the recursion theorem gives every total computable transformation of programs a fixed point.

A set is decidable if its characteristic function is computable and recursively enumerable if it is the domain of a partial recursive function, equivalently the range of a total one; a set is decidable exactly when it and its complement are c.e. The halting set $K$ is c.e. but not decidable, it is m-complete for the c.e. sets, and Rice's theorem makes every nontrivial index set undecidable; Myhill's theorem upgrades m-equivalence to a computable isomorphism. The arithmetical hierarchy stratifies the definable sets, with $\Sigma_1$ the c.e. sets and $\Pi_1$ their complements, and Post's theorem identifies $\Sigma_{n+1}$ with the sets c.e. in $\emptyset^{(n)}$; the Shoenfield limit lemma identifies $\Delta_2$ with the sets computable in $\emptyset'$. The Turing degrees form an upper semilattice with least element $\mathbf{0}$ and a strictly increasing jump, the c.e. degrees are dense and contain incomparable elements by the Friedberg–Muchnik theorem, and the MRDP theorem identifies the c.e. sets with the Diophantine sets, making the decision problem for Diophantine equations undecidable. The computability theory of $\mathbb{N}$ is thus the effective algebra of the natural numbers, and with the model theory of the previous article it completes the algebra slot of the system.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Z, S, P^k_i$ | Zero, successor and projection functions |
| $\mu n$ | Unbounded search, least $n$ with a given property |
| $\varphi_e$ | The $e$-th partial recursive function |
| $\varphi_e(x)\!\downarrow$ | The computation halts |
| $W_e$ | $\operatorname{dom}(\varphi_e)$, the $e$-th c.e. set |
| $K$ | Halting set $\{e : \varphi_e(e)\!\downarrow\}$ |
| $T(e,x,s)$, $U$ | Kleene's normal form predicate and output function |
| $A \leq_m B$ | Many-one reducibility |
| $A \leq_T B$ | Turing reducibility, computable in $B$ |
| $A \oplus B$ | Join of two sets |
| $A'$, $\emptyset^{(n)}$ | Turing jump, iterated jumps of the empty set |
| $\Sigma_n, \Pi_n, \Delta_n$ | Levels of the arithmetical hierarchy |
| $K(x)$ | Prefix-free Kolmogorov complexity, $\min\{\lvert p\rvert : U(p) = x\}$ |
| $\Omega$ | Chaitin's halting probability $\sum_{U(p)\downarrow} 2^{-\lvert p\rvert}$ |
| $\mathcal{D}$ | Upper semilattice of Turing degrees |
| $\mathbf{0}$ | Degree of the decidable sets |





## Further Reading

- Alan M. Turing, "On computable numbers, with an application to the Entscheidungsproblem", *Proceedings of the London Mathematical Society* 42 (1936), for the machine model and the undecidability of the halting problem.
- Stephen C. Kleene, *Introduction to Metamathematics* (Van Nostrand, 1952), for the partial recursive functions, the normal form theorem and the recursion theorem.
- Hartley Rogers Jr., *Theory of Recursive Functions and Effective Computability* (McGraw–Hill, 1967), for a systematic treatment of recursive functions, reducibilities and the arithmetical hierarchy.
- Robert I. Soare, *Recursively Enumerable Sets and Degrees* (Springer, 1987), for the c.e. sets, the priority method and the structure of the c.e. degrees.
- Piergiorgio Odifreddi, *Classical Recursion Theory* (North-Holland, 1989), for the full development of recursion theory and the Turing degrees.
- Yuri V. Matiyasevich, *Hilbert's Tenth Problem* (MIT Press, 1993), for the MRDP theorem and its consequences.
- Cristian S. Calude, *Information and Randomness: An Algorithmic Perspective* (Springer, 2nd ed. 2002), for Kolmogorov complexity and the effective content of randomness.
