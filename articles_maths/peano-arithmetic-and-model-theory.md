
# __Peano Arithmetic and Model Theory__

## Introduction

This is the second article of the Natural Numbers system in Part V, and it occupies the **algebra slot** of that system in its model-theoretic aspect. The system is the structure $\mathbb{N}$ of the previous article, read now through a first-order language, and the object of study is the theory **PA** of Peano arithmetic together with the class of its models. The subject is therefore *model-theoretic* rather than synthetic: the question is not how to define addition and multiplication — that was done in *The Natural Numbers* — but which first-order sentences hold of them, which structures satisfy those sentences, and how far the nonstandard models depart from $\mathbb{N}$.

The general theory of languages, satisfaction, compactness, elementary equivalence, elementary extensions and the Löwenheim–Skolem theorems is the subject of Part I's *Model Theory*, and is used here rather than developed. The proof-theoretic results — the incompleteness theorems, the arithmetical hierarchy, the undefinability of truth — belong to *Proof Theory and Type Theory* and *Formal Logic and Computability*, and are cited. The computability of the arithmetic functions is treated elsewhere and is not used here. The synthetic construction of $\mathbb{N}$ and the recursion and induction principles are from *The Natural Numbers*.

Throughout, the language of arithmetic is $\mathcal{L}_A = \{0, S, +, \cdot, <\}$, with $0$ a constant, $S$ a unary function symbol, $+$ and $\cdot$ binary function symbols and $<$ a binary relation symbol, all interpreted on $\mathbb{N}$ in the evident way. The structure $\mathbb{N} = (\mathbb{N}, 0, S, +, \cdot, <)$ is the **standard model**, PA is the first-order theory displayed below, Q is Robinson arithmetic, and $\operatorname{Th}(\mathbb{N})$ is the set of sentences true in the standard model. A model of PA is written $\mathcal{M}$, its domain $M$, and its standard part is the initial segment isomorphic to $\mathbb{N}$.

## The Theory of Peano Arithmetic

### The Axioms

**Definition.** The theory **PA** of **Peano arithmetic** has the following non-logical axioms in the language $\mathcal{L}_A$:

| | Axiom |
|---|---|
| (PA1) | $\forall x\, (S x \neq 0)$ |
| (PA2) | $\forall x \forall y\, (S x = S y \to x = y)$ |
| (PA3) | $\forall x\, (x \neq 0 \to \exists y\, x = S y)$ |
| (PA4) | $\forall x\, (x + 0 = x)$ |
| (PA5) | $\forall x \forall y\, (x + S y = S(x + y))$ |
| (PA6) | $\forall x\, (x \cdot 0 = 0)$ |
| (PA7) | $\forall x \forall y\, (x \cdot S y = x \cdot y + x)$ |
| (PA8) | $\forall x \forall y\, (x < y \leftrightarrow \exists z\, (x + S z = y))$ |

together with the **induction schema**: for every formula $\varphi(x, \bar y)$ of $\mathcal{L}_A$, the sentence

$$
\forall \bar y\, \Bigl( \varphi(0, \bar y) \wedge \forall x\, \bigl(\varphi(x, \bar y) \to \varphi(S x, \bar y)\bigr) \to \forall x\, \varphi(x, \bar y) \Bigr).
$$

Axioms (PA1)–(PA3) are the successor axioms, (PA4)–(PA7) define addition and multiplication by recursion, and (PA8) defines the order. The induction schema is a *schema*: it is one axiom for each formula, and it is this schema, rather than the single second-order induction axiom of *The Natural Numbers*, that makes PA a first-order theory.

**Definition.** **Robinson arithmetic** Q is the theory with the single successor axiom (PA2) together with (PA1), (PA3)–(PA7) and the order axiom; that is, Q is PA without the induction schema. It is finitely axiomatised, whereas PA is not.

**Remark.** The induction schema is not redundant over the other axioms: Q is strictly weaker than PA, and there are models of Q in which induction fails for a definable set. Q is nevertheless strong enough to prove the basic arithmetic facts needed for the incompleteness theorems, and this is the content of the standard quantifier-free representation lemmas of *Proof Theory and Type Theory*.

### Elementary Consequences

**Theorem.** PA proves the following, for all $x, y, z$:

$$
x + y = y + x, \qquad (x+y)+z = x+(y+z), \qquad x \cdot y = y \cdot x, \qquad (x \cdot y)\cdot z = x\cdot(y\cdot z),
$$

$$
x \cdot (y + z) = x\cdot y + x \cdot z, \qquad x + 0 = x = 0 + x, \qquad x \cdot 1 = x, \qquad x \cdot 0 = 0 ,
$$

and the relation $<$ is a discrete linear order with least element $0$ in which every element has an immediate successor and every nonzero element has an immediate predecessor.

**Proof.** Each semiring law is proved by induction, using the appropriate instance of the induction schema; the proofs are the formal counterparts of the inductions of *The Natural Numbers*. The order properties follow from (PA8): trichotomy and transitivity by induction on the witnesses, discreteness because $S x$ is the immediate successor of $x$ and every nonzero element is a successor by (PA3). $\square$

**Theorem.** PA proves the division algorithm and the existence and uniqueness of prime factorisation; that is, the arithmetic of $\mathbb{N}$ developed in *The Natural Numbers* is formalised in PA.

**Proof.** The division algorithm is proved by induction on the dividend, using (PA8) to compare remainders. The existence of factorisations is proved by strong induction, which is derivable from the induction schema, and uniqueness uses the formalised Euclidean algorithm; the details are standard and are in the references. $\square$

**Theorem (arithmetical hierarchy).** The formulas of $\mathcal{L}_A$ are stratified by the **arithmetical hierarchy** $\Sigma_n$, $\Pi_n$: $\Sigma_0 = \Pi_0$ is the class of formulas with only bounded quantifiers, $\Sigma_{n+1}$ is the class of formulas $\exists \bar x\, \psi$ with $\psi \in \Pi_n$, and $\Pi_{n+1}$ is the class of formulas $\forall \bar x\, \psi$ with $\psi \in \Sigma_n$. PA is **$\Sigma_1$-complete**: every true $\Sigma_1$ sentence is a theorem of PA, and every true $\Sigma_1$ sentence is provable already in Q.

**Proof.** The $\Sigma_1$-completeness is proved by formalising the computation of the witnesses inside PA, using the fact that the proof predicate is primitive recursive and that Q proves the defining equations of the primitive recursive functions. The argument is in *Proof Theory and Type Theory*. $\square$

## Models of Arithmetic

### The Standard Part and Elementary Equivalence

**Theorem.** Every model $\mathcal{M}$ of PA has a unique initial segment isomorphic to $\mathbb{N}$, and the embedding $\mathbb{N} \hookrightarrow \mathcal{M}$ is elementary for quantifier-free formulas and preserves the successor, addition, multiplication and order.

**Proof.** Define $j : \mathbb{N} \to M$ by $j(0) = 0^{\mathcal{M}}$ and $j(S n) = S^{\mathcal{M}}(j(n))$; this is the universal map of the Peano system and it is injective by the argument of *The Natural Numbers*, formalised in PA. Its image is closed under the operations and is an initial segment because $\mathcal{M} \models$ (PA3) and (PA8); uniqueness follows because any two such embeddings agree on the generated substructure, which is all of the image. $\square$

**Definition.** The image of $j$ is the **standard part** of $\mathcal{M}$; an element outside it is **nonstandard**. A model is **standard** if it has no nonstandard elements, so that it is isomorphic to $\mathbb{N}$.

**Theorem.** PA is not complete. A nonstandard model is either elementarily equivalent to $\mathbb{N}$, in which case it is an **elementary extension** of $\mathbb{N}$, or it is not; both kinds exist. The elementary extensions are produced by the upward Löwenheim–Skolem theorem and the compactness theorem, and a model of the second kind is supplied by $\mathrm{PA} + \neg\mathrm{Con}_{\mathrm{PA}}$, which is consistent whenever PA is consistent and cannot be elementarily equivalent to $\mathbb{N}$ because $\mathbb{N} \models \mathrm{Con}_{\mathrm{PA}}$. The set $\operatorname{Th}(\mathbb{N})$ is not recursively axiomatisable, so no finite and no recursively enumerable set of axioms has it as its set of consequences.

**Proof.** For the first kind, apply the upward Löwenheim–Skolem theorem to $\mathbb{N}$ and the compactness theorem as in the existence theorem above. For the second, if PA is consistent then by Gödel's second theorem PA does not prove $\mathrm{Con}_{\mathrm{PA}}$, so the theory $\mathrm{PA} + \neg\mathrm{Con}_{\mathrm{PA}}$ is consistent and has a model, which is not elementarily equivalent to $\mathbb{N}$ because $\mathbb{N} \models \mathrm{Con}_{\mathrm{PA}}$. The non-axiomatisability of $\operatorname{Th}(\mathbb{N})$ is the theorem of Tarski and Church; it is proved in *Formal Logic and Computability*, and it implies that no finite or recursively enumerable set of sentences has exactly the standard model's theory as its consequences. $\square$

### Nonstandard Models

**Theorem (existence).** There are models of PA that are not isomorphic to $\mathbb{N}$. Indeed, for every infinite cardinal $\kappa$ there is a model of PA of cardinality $\kappa$.

**Proof.** Add to $\mathcal{L}_A$ a new constant $c$ and the sentences $c \neq 0$, $c \neq S0$, $c \neq SS0$, and so on. Every finite subset of the resulting theory is satisfiable in $\mathbb{N}$ by interpreting $c$ as a sufficiently large natural number. By the compactness theorem of *Model Theory*, the whole theory has a model $\mathcal{M}$, and the interpretation of $c$ in $\mathcal{M}$ is a nonstandard element. For the cardinal statement, apply the upward Löwenheim–Skolem theorem to that model. $\square$

**Theorem (order type).** Let $\mathcal{M}$ be a nonstandard model of PA and let $N$ be its standard part. Then $\mathcal{M}$ is the disjoint union of $N$ and of the **$\mathbb{Z}$-blocks** $B_a = \{a + n : n \in \mathbb{Z}\}$ for nonstandard $a$, each of which has order type $\mathbb{Z}$ and is an interval in $M$; the set of blocks is densely ordered and has no endpoints, so the order type of $\mathcal{M}$ is

$$
\mathbb{N} + \sum_{q \in D} \mathbb{Z},
$$

where $D$ is a dense linear order without endpoints.

**Proof.** For nonstandard $a$, the map $n \mapsto a + n$ for $n \in \mathbb{Z}$ is injective and order-preserving by cancellation in $\mathcal{M}$, and the set $B_a = \{a + n : n \in \mathbb{Z}\}$ is convex in $M$; so each block has order type $\mathbb{Z}$. The blocks are ordered by $B_a < B_b$ if $a < b$, and this order is dense: if $a < b$ lie in distinct blocks, then $b - a$ is greater than every standard number, and $c = \lfloor (a+b)/2 \rfloor$, computed in $\mathcal{M}$, is nonstandard and satisfies $a < c < b$, so $B_a < B_c < B_b$. There is no least block above the standard part, because for nonstandard $a$ the element $\lfloor a/2 \rfloor$ is nonstandard and lies in a strictly lower block, and no greatest block, because $2a$ lies in a strictly higher one. Hence the nonstandard part is a densely ordered family of $\mathbb{Z}$-blocks with no endpoints. $\square$

**Theorem (overspill).** Let $\mathcal{M}$ be a nonstandard model of PA and let $\varphi(x)$ be a formula with parameters in $M$ such that $\mathcal{M} \models \varphi(n)$ for every standard $n$. Then there is a nonstandard $b \in M$ with $\mathcal{M} \models \varphi(b)$.

**Proof.** Let $A = \{x \in M : \mathcal{M} \models \varphi(x)\}$. Then $A$ contains the standard part and is closed under successor there, because the successor of a standard element is standard and satisfies $\varphi$. If $A$ contained no nonstandard element, then $A$ would be exactly the standard part, and the formula $\varphi$ would satisfy $\mathcal{M} \models \varphi(0) \wedge \forall x(\varphi(x) \to \varphi(Sx))$, since every element of $A$ is standard and has its successor in $A$. The induction schema in $\mathcal{M}$ would then give $\mathcal{M} \models \forall x\, \varphi(x)$, contradicting that $\mathcal{M}$ has nonstandard elements outside $A$. Hence $A$ contains a nonstandard element. $\square$

**Corollary.** The standard part is not definable in any nonstandard model, and there is no formula $\sigma(x)$ of $\mathcal{L}_A$ such that $\mathcal{M} \models \sigma(a)$ for exactly the standard $a$. If a definable subset of $M$ is bounded above by a standard element, then it is finite and contained in the standard part, since no element below a standard element is nonstandard.

**Corollary (underspill).** Let $\varphi(x)$ hold for all sufficiently small nonstandard $x$ in the sense that there is a nonstandard $b$ with $\mathcal{M} \models \forall x < b\, \varphi(x)$. Then $\varphi(n)$ holds for some standard $n$.

**Proof.** Suppose $\varphi(n)$ fails for every standard $n$. The formula $x < b \wedge \neg\varphi(x)$ then holds at every standard $x$, because $b$ is nonstandard and $\neg\varphi(n)$ holds by the supposition; overspill gives a nonstandard $c$ satisfying it, so $c < b$ and $\neg\varphi(c)$, contradicting $\mathcal{M} \models \forall x < b\, \varphi(x)$. $\square$

## Incompleteness and the Arithmetic of Provability

### Gödel's Theorems

**Theorem (Gödel, first incompleteness theorem).** If PA is consistent, then there is a sentence $G$ of $\mathcal{L}_A$ such that PA does not prove $G$ and PA does not prove $\neg G$; moreover $G$ is true in the standard model. The sentence $G$ can be taken to be $\Pi_1$, and it asserts its own unprovability.

**Proof.** Gödel's diagonal construction produces a sentence $G$ with

$$
\mathrm{PA} \vdash G \leftrightarrow \neg \mathrm{Prov}_{\mathrm{PA}}(\#G),
$$

where $\mathrm{Prov}$ is the arithmetised proof predicate, using the representability of the recursive functions in Q and the diagonal lemma. If PA proved $G$ then $\mathrm{Prov}(\#G)$ would hold and, by $\Sigma_1$-completeness, PA would prove it, contradicting the equivalence; if PA proved $\neg G$ and PA is consistent, then $G$ is not provable and, by $\Sigma_1$-completeness of the negation, PA would prove $\mathrm{Prov}(\#G)$, again contradicting the equivalence. The argument is Gödel's and is given in *Proof Theory and Type Theory*. $\square$

**Theorem (Gödel, second incompleteness theorem).** If PA is consistent, then PA does not prove its own consistency statement

$$
\mathrm{Con}_{\mathrm{PA}} = \neg \mathrm{Prov}_{\mathrm{PA}}(\#0 = 1),
$$

which is a $\Pi_1$ sentence.

**Proof.** The second theorem is obtained by formalising the first inside PA; the formalised statement is that $\mathrm{Con}_{\mathrm{PA}}$ implies $G$, so a proof of $\mathrm{Con}_{\mathrm{PA}}$ would give a proof of $G$, which the first theorem excludes. The Hilbert–Bernays–Löb derivability conditions are the hypothesis, and they are verified for PA; the argument is in *Proof Theory and Type Theory*. $\square$

**Corollary.** PA is incomplete, and no recursively axiomatisable consistent theory extending PA is complete; in particular $\operatorname{Th}(\mathbb{N})$ is not recursively axiomatisable. The independent sentences include the consistency statement $\mathrm{Con}_{\mathrm{PA}}$, the Rosser sentence, the Paris–Harrington sentence and the Goodstein sentences.

**Theorem (Tarski).** The set $\operatorname{Th}(\mathbb{N})$ is not definable in $\mathbb{N}$: there is no formula $\tau(x)$ of $\mathcal{L}_A$ such that for every sentence $\sigma$, $\mathbb{N} \models \tau(\#\sigma) \leftrightarrow \sigma$.

**Proof.** If such a $\tau$ existed, the diagonal lemma applied to $\neg\tau(x)$ would produce a sentence $\lambda$ with $\mathbb{N} \models \lambda \leftrightarrow \neg \tau(\#\lambda)$, contradicting the definition of $\tau$ at $\sigma = \lambda$. This is Tarski's undefinability theorem. $\square$

### Decidable Fragments and Definability

**Theorem (Presburger).** The theory of $(\mathbb{N}, 0, S, +, <)$ is complete, decidable and admits quantifier elimination after the addition of the divisibility predicates $n \mid x$ for each positive integer $n$.

**Proof.** The quantifier-elimination procedure is Presburger's and the decidability follows because the resulting quantifier-free sentences are decidable by computation; the details are in *Model Theory* and *Formal Logic and Computability*. $\square$

**Theorem (Skolem).** The theory of $(\mathbb{N}, \cdot)$ is decidable.

**Proof.** The multiplicative structure of $\mathbb{N}$ is the free commutative monoid on the primes of *The Natural Numbers*, and its first-order theory is decidable; the result is Skolem's and is quoted. $\square$

**Remark.** The contrast between the decidability of Presburger and Skolem arithmetic and the undecidability of PA is the model-theoretic expression of the fact that induction over an arbitrary formula is what makes PA strong. Presburger arithmetic has quantifier elimination because the definable sets are eventually periodic; PA cannot have it, because the definable sets are the arithmetical sets, and Tarski's theorem shows that truth is not among them. The real analogue is the quantifier elimination of real closed fields, which makes the theory of $(\mathbb{R}, +, \cdot, <)$ decidable, and this is the model-theoretic theme taken up.

## Provable Totality and the Fast-Growing Hierarchy

### Provably Total Functions

**Definition.** A recursive function $f : \mathbb{N}^k \to \mathbb{N}$ is **provably total** in a theory $T$ containing a suitable fragment of arithmetic if $T$ proves that for every input there is exactly one output computing $f$; informally, if $T$ proves that the algorithm defining $f$ halts on every input.

**Theorem.** Every primitive recursive function is provably total in PA, and every function defined by recursion on a well-founded ordering of the natural numbers that PA recognises is provably total. The class of provably total functions of PA is strictly larger than the primitive recursive functions but is contained in the class of functions elementary in the fast-growing hierarchy below the ordinal $\varepsilon_0$.

**Proof.** PA formalises the recursion equations and proves the induction needed for the termination; the characterisation of the provably total functions is the Wainer theorem, which identifies them with the $\alpha$-recursive functions for $\alpha < \varepsilon_0$. It is quoted from the references. $\square$

### Independence from PA

**Theorem (Paris–Harrington).** There is a true arithmetical statement, the strengthened finite Ramsey theorem, that is not provable in PA; it is provable in the stronger systems of second-order arithmetic, and it is an instance of the incompleteness phenomenon in which the unprovable statement has combinatorial content.

**Theorem (Goodstein).** Goodstein's theorem, asserting that every Goodstein sequence terminates, is not provable in PA, although the statement is true and is provable in the stronger systems of second-order arithmetic; the unprovability is a consequence of the fact that the termination requires induction up to $\varepsilon_0$.

**Proof.** The theorems are Paris and Harrington's and Goodstein's, with the unprovability following from the ordinal analysis of PA by Gentzen, which assigns the proof-theoretic ordinal $\varepsilon_0$ to the theory. The proofs are in the references. $\square$

**Remark.** The pair of results shows that the boundary of the provable is not the boundary of the true: PA proves the totality of a large and well-understood class of recursive functions, and it fails to prove the totality of functions whose termination requires an induction stronger than the one it permits. The fast-growing hierarchy measures the strength of a theory by the functions whose totality it can prove, and this makes the incompleteness of arithmetic a quantitative phenomenon.

## Summary

Peano arithmetic PA is the first-order theory in the language $\{0, S, +, \cdot, <\}$ consisting of the three successor axioms, the recursion equations for addition and multiplication, the definition of the order, and the induction schema, one instance for each formula. It formalises the arithmetic of *The Natural Numbers*: it proves the semiring laws, cancellation, the discreteness and linearity of the order, the division algorithm and the uniqueness of prime factorisation. Robinson arithmetic Q is PA without the induction schema; it is finitely axiomatised and strictly weaker, but it proves the defining equations of the recursive functions and is $\Sigma_1$-complete, and PA is $\Sigma_1$-complete as well.

Every model of PA contains a unique initial segment isomorphic to $\mathbb{N}$, the standard part; models with elements outside it are the nonstandard models, and they exist in every infinite cardinality by compactness and Löwenheim–Skolem. A nonstandard model has order type $\mathbb{N}$ followed by a dense order of blocks each of order type $\mathbb{Z}$, and the overspill and underspill lemmas express the failure of the standard part to be definable. Elementary extensions of $\mathbb{N}$ are nonstandard and elementarily equivalent to it, while models of $\text{PA} + \neg \mathrm{Con}_{\mathrm{PA}}$ are not, so elementary equivalence does not single out the standard model and no single first-order sentence captures the standard part; $\operatorname{Th}(\mathbb{N})$ is not recursively axiomatisable.

Gödel's first incompleteness theorem produces, for any consistent recursively axiomatisable theory extending PA, a $\Pi_1$ sentence neither provable nor refutable and true in the standard model; the second theorem states that PA does not prove its own consistency statement, a $\Pi_1$ sentence. Tarski's theorem shows that truth in $\mathbb{N}$ is not definable in $\mathbb{N}$. By contrast the theories of $(\mathbb{N}, +, <)$ and of $(\mathbb{N}, \cdot)$ are decidable, the first admitting quantifier elimination after divisibility predicates are added. The model theory of the natural numbers is thus the meeting point of the synthetic construction of the previous article and the general model theory of Part I, and it is the source of the incompleteness that distinguishes the arithmetic of $\mathbb{N}$ from its algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{L}_A$ | Language of arithmetic, $\{0, S, +, \cdot, <\}$ |
| $\mathbb{N}$ | Standard model $(\mathbb{N}, 0, S, +, \cdot, <)$ |
| PA | Peano arithmetic, the axioms (PA1)–(PA8) plus the induction schema |
| Q | Robinson arithmetic, PA without induction |
| $\mathcal{M}$ | A model of PA, with domain $M$ |
| $N$ | Standard part of $\mathcal{M}$, an initial segment isomorphic to $\mathbb{N}$ |
| $\Sigma_n$, $\Pi_n$ | Levels of the arithmetical hierarchy |
| $\mathrm{Prov}_{\mathrm{PA}}(\#\sigma)$ | Arithmetised proof predicate |
| $\mathrm{Con}_{\mathrm{PA}}$ | Consistency statement, a $\Pi_1$ sentence |
| $G$ | Gödel sentence, $\mathrm{PA} \vdash G \leftrightarrow \neg \mathrm{Prov}(\#G)$ |
| $\operatorname{Th}(\mathbb{N})$ | Set of sentences true in the standard model |
| $\mathcal{M} \equiv \mathbb{N}$ | Elementary equivalence of models |
| $B_a$ | $\mathbb{Z}$-block of a nonstandard element $a$ |



## Further Reading

- Kurt Gödel, "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I", *Monatshefte für Mathematik und Physik* 38 (1931), for the incompleteness theorems and the arithmetisation of syntax.
- Stephen G. Simpson, *Subsystems of Second Order Arithmetic* (Cambridge University Press, 2nd ed. 2009), for the proof-theoretic strength of fragments of arithmetic and the hierarchy of induction.
- Richard Kaye, *Models of Peano Arithmetic* (Oxford University Press, 1991), for nonstandard models, overspill, order types and recursive saturation.
- Petr Hájek and Pavel Pudlák, *Metamathematics of First-Order Arithmetic* (Springer, 1993), for a systematic treatment of PA, its fragments and its models.
- Joseph R. Shoenfield, *Mathematical Logic* (Addison-Wesley, 1967), for the arithmetical hierarchy, the incompleteness theorems and Tarski's undefinability theorem.
- Mojżesz Presburger, "Über die Vollständigkeit eines gewissen Systems der Arithmetik", *Comptes Rendus du I Congrès des Mathématiciens des Pays Slaves* (1929), for the decidability and quantifier elimination of $(\mathbb{N}, +, <)$.
- Alexandra Shlapentokh, *Hilbert's Tenth Problem: Diophantine Classes and Extensions to Global Fields* (Cambridge University Press, 2007), for the undecidability phenomena that separate PA from its decidable fragments.
