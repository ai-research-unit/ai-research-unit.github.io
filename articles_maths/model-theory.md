
# __Model Theory__

## Introduction

Model theory is the study of first-order theories through their models: the structures in which the sentences of a language are true. It asks which classes of structures a language can describe, which properties of a structure are determined by its first-order theory, and how the statements of a theory constrain the objects that satisfy it. Its two central tools are the compactness theorem, which converts the finite satisfiability of every finite part of a theory into the existence of a model, and the construction of ultraproducts, which builds a model from a family of models and an ultrafilter.

The article stands seventh in the corpus, above *Formal Logic and Computability*, and uses the first-order syntax, the satisfaction relation, soundness and completeness, compactness and the Löwenheim–Skolem theorems of that article and of *Logic and Proof*. It develops the vocabulary of the subject — languages and structures, homomorphisms and embeddings, elementary equivalence, definable sets, quantifier elimination — and then applies it to three classes of examples: algebraically closed fields, real-closed fields and valued fields. The algebraic theory of those objects belongs to the other articles of Part I that introduce them; here they are used only as structures for a formal language, and the results quoted are the model-theoretic theorems about them.

The article is written for its own sake and for the use the rest of the corpus makes of it. The ultraproduct construction is used and in the study of infinite groups; the compactness theorem underlies the existence of nonstandard models, which the corpus uses to show that certain statements are not first-order; and quantifier elimination is the standard route to the decidability of a theory. No topology and no distance appears. Where a result has a richer form once a topology is available — the Stone space of types, the topology on the space of models — the article states the order-theoretic or set-theoretic version and defers the enrichment to Part II.

## Languages and Structures

### Signatures and Structures

**Definition.** A **signature** (or **language**) $L$ consists of a set of **function symbols**, a set of **relation symbols** and a set of **constant symbols**, each function and relation symbol being assigned a nonnegative integer, its **arity**. A **structure** $\mathcal{M}$ for $L$ consists of a nonempty set $M$, the **domain** (or **universe**), together with, for each constant symbol $c$, an element $c^{\mathcal{M}} \in M$; for each $n$-ary function symbol $f$, a function $f^{\mathcal{M}} : M^n \to M$; and for each $n$-ary relation symbol $R$, a subset $R^{\mathcal{M}} \subseteq M^n$.

**Example (the language of order).** The signature $L_{\mathrm{ord}}$ has a single binary relation symbol $<$, no function symbols and no constants. A structure for it is a set with a binary relation; the structures in which the relation is a dense linear order without endpoints form the theory DLO, and the orders of the rationals and of the reals of *Rings and Fields* are its two standard models.

**Example (the language of rings).** The signature $L_{\mathrm{ring}}$ has two binary function symbols $+$ and $\cdot$ and two constants $0$ and $1$. A structure for it is a set with two binary operations and two distinguished elements; the **theory of fields** is the set of sentences in this language expressing the field axioms, and its models are exactly the fields. The algebraic development of that notion is; the model-theoretic questions about the theory are what follow here.

**Example (the language of groups).** The signature $L_{\mathrm{grp}}$ has a binary function symbol $\cdot$, a unary function symbol ${}^{-1}$ and a constant $e$. The theory of groups is the set of sentences expressing associativity, the identity law and the inverse law, and its models are the groups. This and the preceding example are the two running examples of the article.

### Terms, Formulas and Satisfaction

The terms of $L$ are the variables, the constants, and the expressions $f(t_1,\ldots,t_n)$; the atomic formulas are $R(t_1,\ldots,t_n)$ and $t_1 = t_2$; and the formulas are built from the atomic ones by the connectives and the quantifiers, exactly as in *Logic and Proof*. A **sentence** is a formula with no free variables.

**Definition.** Let $\mathcal{M}$ be an $L$-structure. An **assignment** is a function $a$ from the variables to $M$. The value $t^{\mathcal{M}}[a]$ of a term and the satisfaction relation $\mathcal{M} \models \varphi[a]$ are defined by recursion:

$$
\mathcal{M} \models R(t_1,\ldots,t_n)[a] \iff (t_1^{\mathcal{M}}[a], \ldots, t_n^{\mathcal{M}}[a]) \in R^{\mathcal{M}},
$$

$$
\mathcal{M} \models \neg\varphi[a] \iff \mathcal{M} \not\models \varphi[a], \quad \mathcal{M} \models \varphi \wedge \psi[a] \iff \mathcal{M} \models \varphi[a] \text{ and } \mathcal{M} \models \psi[a],
$$

$$
\mathcal{M} \models \forall x\,\varphi[a] \iff \mathcal{M} \models \varphi[a'] \text{ for every } a' \text{ agreeing with } a \text{ off } x.
$$

The clauses for $\vee, \to, \leftrightarrow$ are the truth-table clauses, and $\exists$ is treated as $\neg\forall\neg$. A sentence $\sigma$ is **true in** $\mathcal{M}$, written $\mathcal{M} \models \sigma$, if it is satisfied under some assignment, equivalently under every one; a set $T$ of sentences is a **theory** and $\mathcal{M}$ a **model** of $T$ if $\mathcal{M} \models \sigma$ for all $\sigma \in T$.

The satisfaction relation depends only on the isomorphism type of the structure, in the precise sense that an isomorphism preserves satisfaction of every formula; this is the **isomorphism lemma**, and it is proved by induction on formulas.

### Homomorphisms, Embeddings and Substructures

**Definition.** Let $\mathcal{M}$ and $\mathcal{N}$ be $L$-structures. A function $h : M \to N$ is an **$L$-homomorphism** if it preserves the constants, the functions and the relations: $h(c^{\mathcal{M}}) = c^{\mathcal{N}}$, $h(f^{\mathcal{M}}(\vec a)) = f^{\mathcal{N}}(h(\vec a))$, and $\vec a \in R^{\mathcal{M}}$ implies $h(\vec a) \in R^{\mathcal{N}}$ for every relation symbol $R$. It is an **embedding** if in addition $h$ is injective and $\vec a \in R^{\mathcal{M}} \iff h(\vec a) \in R^{\mathcal{N}}$, and an **isomorphism** if it is a bijective embedding. An isomorphism $\mathcal{M} \to \mathcal{M}$ is an **automorphism**.

**Definition.** $\mathcal{N}$ is a **substructure** of $\mathcal{M}$ if $N \subseteq M$, the constants and functions of $\mathcal{N}$ are the restrictions of those of $\mathcal{M}$, and each $R^{\mathcal{N}} = R^{\mathcal{M}} \cap N^n$. The substructure **generated** by a subset $A \subseteq M$ is the least substructure containing $A$, obtained by closing $A$ under the constants and functions; the structure is **finitely generated** if it is generated by a finite set.

**Example.** For $L_{\mathrm{grp}}$, the substructures are the subsets containing $e$ and closed under $\cdot$ and ${}^{-1}$, that is, the subgroups; the substructure generated by $A$ is the subgroup generated by $A$. For $L_{\mathrm{ring}}$, the substructures are the subrings with the same $0$ and $1$.

**Proposition.** A homomorphism preserves the satisfaction of every **positive** formula, that is, a formula built from atomic formulas by $\wedge, \vee$ and the quantifiers (without $\neg$ and without $\to$); an embedding preserves the satisfaction of every **existential** formula, and an isomorphism preserves every formula. If $h$ is an embedding then $\mathcal{M} \models \varphi[a]$ implies $\mathcal{N} \models \varphi[h \circ a]$ for quantifier-free $\varphi$.

**Proof sketch.** Induction on the complexity of $\varphi$. Atomic formulas are preserved by a homomorphism by the definition, and the definition of a homomorphism for relations is one-directional; an embedding is two-directional, which extends the induction through negations; and injectivity together with the substructure conditions extends it through quantifiers for existential formulas. $\square$

## Elementary Equivalence and Elementary Maps

### Elementary Equivalence

**Definition.** Two $L$-structures $\mathcal{M}$ and $\mathcal{N}$ are **elementarily equivalent**, written $\mathcal{M} \equiv \mathcal{N}$, if they satisfy the same $L$-sentences. The **theory** of $\mathcal{M}$ is $\operatorname{Th}(\mathcal{M}) = \{\sigma : \mathcal{M} \models \sigma\}$, so that $\mathcal{M} \equiv \mathcal{N}$ if and only if $\operatorname{Th}(\mathcal{M}) = \operatorname{Th}(\mathcal{N})$.

**Definition.** Let $T$ be a theory. $T$ is **complete** if $T \models \sigma$ or $T \models \neg\sigma$ for every sentence $\sigma$; equivalently, if any two models of $T$ are elementarily equivalent. $T$ is **$\kappa$-categorical** if it has exactly one model of cardinality $\kappa$ up to isomorphism.

**Theorem (Vaught's test).** Let $T$ be a theory in a countable language with no finite models. If $T$ is $\kappa$-categorical for some infinite cardinal $\kappa$, then $T$ is complete.

**Proof.** Let $\mathcal{M}, \mathcal{N} \models T$. By the downward Löwenheim–Skolem theorem of *Formal Logic and Computability*, each has a countable model elementarily equivalent to it; since $T$ has no finite models, those countable models are infinite. By the upward theorem, each has a model of cardinality $\kappa$, and by $\kappa$-categoricity those two models are isomorphic, hence elementarily equivalent. Composing the elementary equivalences gives $\mathcal{M} \equiv \mathcal{N}$. $\square$

Vaught's test is the standard route to completeness, and it is applied to algebraically closed fields and to dense linear orders below. Its hypothesis that the theory have no finite models is essential: the theory with no nonlogical axioms has finite models of every size and is not complete.

### Elementary Embeddings and the Tarski–Vaught Criterion

**Definition.** An embedding $h : \mathcal{M} \to \mathcal{N}$ is **elementary** if for every formula $\varphi(\vec x)$ and every tuple $\vec a \in M$,

$$
\mathcal{M} \models \varphi[\vec a] \iff \mathcal{N} \models \varphi[h(\vec a)].
$$

$\mathcal{M}$ is an **elementary substructure** of $\mathcal{N}$, written $\mathcal{M} \preceq \mathcal{N}$, if the inclusion is elementary.

Elementary equivalence is the case of an elementary embedding in which no parameters are named; an elementary embedding is stronger than an embedding, because it preserves formulas with quantifiers and parameters. The two notions differ: the inclusion $\mathbb{N} \hookrightarrow \mathbb{Z}$ of ordered sets is an embedding, but it is not elementary, because the element $0$ has no predecessor in $\mathbb{N}$, and the density sentence

$$
\forall x \forall y\,(x < y \to \exists z\,(x < z \wedge z < y))
$$

is true in every dense linear order without endpoints and false in $\mathbb{Z}$, where $x = 0$ and $y = 1$ have no element strictly between them. Hence the dense linear orders and the order of $\mathbb{Z}$ are not elementarily equivalent.

**Theorem (Tarski–Vaught criterion).** Let $\mathcal{M}$ be a substructure of $\mathcal{N}$. Then $\mathcal{M} \preceq \mathcal{N}$ if and only if, for every formula $\varphi(x, \vec y)$ and every tuple $\vec a \in M$, whenever $\mathcal{N} \models \exists x\,\varphi(x,\vec a)$ there is $b \in M$ with $\mathcal{N} \models \varphi(b, \vec a)$.

**Proof sketch.** If $\mathcal{M} \preceq \mathcal{N}$, an element witnessing the existential statement in $\mathcal{N}$ may be replaced by one in $M$ using elementarity and the satisfaction of the existential formula in $\mathcal{M}$. Conversely, assume the condition and prove $\mathcal{M} \models \varphi[\vec a] \iff \mathcal{N} \models \varphi[\vec a]$ for all $\vec a \in M$ by induction on $\varphi$: the atomic case is the definition of substructure, the connectives are immediate, and the quantifier case uses the condition to move a witness into $M$. $\square$

The criterion is the working form of the downward Löwenheim–Skolem theorem: given a subset $A$ of a structure, one closes $A$ under the functions and under the choice of witnesses, and the closure is an elementary substructure of cardinality at most $\max(|A|, |L|, \aleph_0)$.

### Definable Sets

**Definition.** Let $\mathcal{M}$ be an $L$-structure and let $\varphi(x_1,\ldots,x_n, \vec y)$ be a formula. For a tuple $\vec b \in M$ the set

$$
\varphi(\mathcal{M}, \vec b) = \{\vec a \in M^n : \mathcal{M} \models \varphi[\vec a, \vec b]\}
$$

is **definable** in $\mathcal{M}$ with **parameters** $\vec b$. A set is **$\varnothing$-definable** (or **definable without parameters**) if it is $\varphi(\mathcal{M})$ for a formula with no free variables beyond $\vec x$. A function is definable if its graph is definable, and a subset $A \subseteq M$ is definable if it is the extension of a formula in one free variable.

**Proposition.** The definable sets in $\mathcal{M}$ with parameters in a fixed set $B$ form a Boolean algebra under union, intersection and complement, and are closed under finite and — when the quantifiers are available — under arbitrary definable images and preimages. They are invariant under automorphisms: if $\sigma$ is an automorphism of $\mathcal{M}$ fixing $B$ pointwise and $D$ is definable with parameters in $B$, then $\sigma(D) = D$.

**Proof.** Union, intersection and complement correspond to $\vee$, $\wedge$ and $\neg$; an image under the projection $(x_1,\ldots,x_n) \mapsto (x_1,\ldots,x_{n-1})$ corresponds to existential quantification, and a preimage to substitution. For the invariance, if $D = \varphi(\mathcal{M}, \vec b)$ and $\sigma$ is an automorphism fixing $\vec b$, then $\vec a \in D$ iff $\mathcal{M} \models \varphi[\vec a, \vec b]$ iff $\mathcal{M} \models \varphi[\sigma(\vec a), \vec b]$ iff $\sigma(\vec a) \in D$, using the isomorphism lemma. $\square$

The invariance under automorphisms gives the standard method for showing that a set is *not* definable: exhibit an automorphism of the structure that does not preserve it. It is used for groups and for fields throughout the corpus.

## Compactness and its Consequences

### The Compactness Theorem

The compactness theorem was proved in *Formal Logic and Computability* and is restated here in its model-theoretic form.

**Theorem (compactness).** A theory $T$ has a model if and only if every finite subset of $T$ has a model.

### Nonstandard Models

**Definition.** Let $T$ be a theory and let $\mathcal{M}$ be a model of $T$. Then $\mathcal{M}$ is a **nonstandard model** if it is not isomorphic to the **standard model** that the theory is intended to describe.

**Example (nonstandard arithmetic).** Let $\operatorname{Th}(\mathbb{N})$ be the set of sentences true in $(\mathbb{N}, +, \cdot, 0, 1, <)$, and add a new constant $c$ together with the sentences $c > \bar n$ for every numeral $\bar n$. Every finite subset is satisfied in $\mathbb{N}$ by interpreting $c$ as a sufficiently large natural number, so by compactness the whole theory has a model $\mathcal{N}$. In $\mathcal{N}$ the element $c^{\mathcal{N}}$ is larger than every standard natural number, and $(\mathbb{N}, +,\cdot,<)$ is an elementary substructure of $\mathcal{N}$. The model $\mathcal{N}$ is nonstandard, and it shows that the property "every element is a numeral" cannot be expressed by finitely many first-order sentences.

**Example (nonstandard analysis).** Applying the same construction to a real-closed ordered field, in the sense of *Real-Closed and Complete Ordered Fields*, produces a real-closed field with infinitesimal elements, the basis of the elementary treatment of the calculus. The construction is quoted here and developed in Part II, where the objects of analysis are available.

### Löwenheim–Skolem Revisited

The Löwenheim–Skolem theorems of *Formal Logic and Computability* take the following form in the present vocabulary.

**Theorem.** Let $T$ be a theory in a language $L$ with $|L| = \kappa$, and suppose $T$ has an infinite model.

1. If $\mathcal{M} \models T$ and $A \subseteq M$, there is an elementary substructure of $\mathcal{M}$ containing $A$ of cardinality at most $\max(|A|, \kappa, \aleph_0)$.
2. $T$ has a model of every cardinality $\lambda \geq \max(\kappa, \aleph_0)$.

**Proof sketch.** (1) is the Tarski–Vaught criterion applied to the closure of $A$ under the constants, the functions and a choice of witnesses, iterated $\omega$ times; the closure has the required cardinality and is elementary. (2) adds $\lambda$ constants with the sentences $c_\alpha \neq c_\beta$ and applies compactness and (1). $\square$

The **Löwenheim–Skolem paradox** is the special case in which a theory such as the theory of fields has a countable model: a countable field can be algebraically closed, and the statement "every nonconstant polynomial has a root" is satisfied in it because the polynomial is an element of the model and its root is found inside the model. Cardinality in the metatheory and cardinality as seen by the model are different notions, and the paradox disappears once they are distinguished.

## Quantifier Elimination

### The Notion and its Consequences

**Definition.** A theory $T$ **admits quantifier elimination** if for every formula $\varphi(\vec x)$ there is a quantifier-free formula $\psi(\vec x)$ with

$$
T \models \forall \vec x\,(\varphi(\vec x) \leftrightarrow \psi(\vec x)).
$$

**Proposition.** If $T$ admits quantifier elimination then every definable set in a model of $T$ is a finite Boolean combination of the sets defined by the atomic formulas. If in addition $T$ is recursively axiomatised and the quantifier-free sentences of its language are decidable, then $T$ is complete and decidable.

**Proof sketch.** The first statement is immediate from the definition. For the second, a sentence is equivalent modulo $T$ to a quantifier-free sentence; if the quantifier-free sentences are decidable then so is the set of sentences provable from $T$, by enumerating derivations (which is possible by the completeness theorem) and deciding equivalence, and completeness follows because either $\sigma$ or $\neg\sigma$ reduces to a quantifier-free sentence that is decided. $\square$

**Theorem (quantifier-elimination criterion).** $T$ admits quantifier elimination if and only if for every quantifier-free formula $\varphi(\vec x, \vec y)$, every pair of models $\mathcal{M}, \mathcal{N}$ of $T$ with a common substructure $\mathcal{A}$, and every tuple $\vec a \in A$,

$$
\mathcal{M} \models \exists \vec x\,\varphi(\vec x, \vec a) \iff \mathcal{N} \models \exists \vec x\,\varphi(\vec x, \vec a).
$$

**Proof sketch.** If $T$ admits quantifier elimination, then $\exists\vec x\,\varphi(\vec x,\vec y)$ is equivalent modulo $T$ to a quantifier-free formula $\psi(\vec y)$; for $\vec a$ in the common substructure $\mathcal{A}$, the truth of $\psi(\vec a)$ is decided inside $\mathcal{A}$ and hence is the same in $\mathcal{M}$ and in $\mathcal{N}$. Conversely, the criterion permits the construction, by induction on the number of quantifiers, of a quantifier-free equivalent for each formula, the quantifier step being handled by showing that the set of tuples satisfying $\exists\vec x\,\varphi$ is already quantifier-free definable. $\square$

The criterion reduces quantifier elimination to the solvability of quantifier-free formulas over a common substructure, and it is the standard verification. It is applied in the two examples below.

### Algebraically Closed Fields

**Definition.** The theory $\mathrm{ACF}$ of **algebraically closed fields** is the theory of fields together with, for each $n \geq 1$, the sentence

$$
\forall a_0 \ldots \forall a_{n-1}\, \exists x\,(x^n + a_{n-1}x^{n-1} + \cdots + a_0 = 0)
$$

and the sentence $1 \neq 0$. For a prime $p$ or $p = 0$, the theory $\mathrm{ACF}_p$ adds the sentences $1 + \cdots + 1 = 0$ ($p$ summands) when $p$ is prime, or the sentences $n \cdot 1 \neq 0$ for all $n$ when $p = 0$. The **characteristic** of a field is the prime $p$ with $p \cdot 1 = 0$, or $0$ if no such prime exists.

**Theorem (Tarski; Chevalley; Robinson).** $\mathrm{ACF}$ admits quantifier elimination. Each theory $\mathrm{ACF}_p$ is complete, decidable and $\kappa$-categorical for every uncountable $\kappa$.

**Proof sketch.** Quantifier elimination is verified by the criterion: the substructures of a field are its subrings, and a quantifier-free formula with parameters in a subring $A$ is a finite Boolean combination of polynomial equations $f(\vec x) = 0$. Whether such a combination has a solution in an algebraically closed field containing $A$ is decided by the ideal generated by the polynomials together with the equations and inequations of the combination, and the decision is expressible by quantifier-free conditions on the coefficients: this is the content of Chevalley's theorem on the constructible image of a constructible set, and the details are in the standard references. Completeness follows from Vaught's test, since $\mathrm{ACF}_p$ has no finite models and is $\kappa$-categorical for uncountable $\kappa$; decidability follows from the quantifier elimination because the quantifier-free sentences of the language of rings reduce to equations between integers, which are decidable. $\square$

**Corollary.** Two algebraically closed fields are elementarily equivalent if and only if they have the same characteristic. In particular any two uncountable algebraically closed fields of the same characteristic are elementarily equivalent.

The result explains why the theory of algebraically closed fields is "tame": the first-order language cannot see the transcendence degree, only the characteristic. The finer classification by transcendence degree is a theorem of algebra, stated as standard.

### Real-Closed Fields

**Definition.** An **ordered field** is a field with a total order compatible with the operations: $x \leq y$ implies $x + z \leq y + z$, and $x \geq 0$ and $y \geq 0$ imply $xy \geq 0$. An ordered field is **real-closed** if every positive element has a square root and every polynomial of odd degree has a root; equivalently, if it has no proper ordered algebraic extension.

**Theorem (Tarski–Seidenberg).** The theory $\mathrm{RCF}$ of real-closed fields, in the language of ordered rings, admits quantifier elimination and is complete and decidable.

**Proof sketch.** Quantifier elimination is verified by the criterion in the form of a sign-changing argument: for a quantifier-free formula $\varphi(x,\vec a)$ whose atomic parts are polynomial equations and inequalities, the set of $x$ satisfying $\varphi$ is a finite union of intervals and points, and whether it is nonempty is decided by evaluating the polynomials at the finitely many roots of the polynomials occurring in $\varphi$ and their derivatives together with the parameters, using the intermediate value property of odd-degree polynomials. Completeness follows because any two real-closed fields satisfy the same sentences, which is the algebraic form of Tarski's theorem in *Real-Closed and Complete Ordered Fields*; decidability follows from the quantifier elimination and the decidability of the quantifier-free sentences. $\square$

**Definition.** A theory $T$ extending the theory of ordered fields is **o-minimal** if every definable subset of the domain in one variable is a finite union of points and intervals with endpoints in the model.

**Theorem.** $\mathrm{RCF}$ is o-minimal.

**Proof sketch.** By quantifier elimination, a definable subset of the line is a finite Boolean combination of sets $\{x : f(x) = 0\}$ and $\{x : f(x) > 0\}$ for polynomials $f$ with parameters; the zero set of a nonzero polynomial is finite, and the sign of a polynomial changes only at its roots, so the set is a finite union of points and intervals. $\square$

O-minimality is the tameness property of real-closed fields: every definable set is built from intervals, so definable sets have finitely many connected pieces and definable functions are piecewise monotone. The definitions of connectedness and of a cell decomposition require a topology and belong to Part II; the order-theoretic content, that definable sets are finite unions of points and intervals, is the statement proved here, and it is the one the corpus uses.

### Valued Fields

**Definition.** A **valuation** on a field $K$ is a surjective map $v : K \to \Gamma \cup \{\infty\}$, where $\Gamma$ is an ordered abelian group and $\infty$ is greater than every element of $\Gamma$, satisfying

$$
v(xy) = v(x) + v(y), \qquad v(x+y) \geq \min(v(x), v(y)), \qquad v(x) = \infty \iff x = 0.
$$

The set $\mathcal{O}_v = \{x \in K : v(x) \geq 0\}$ is the **valuation ring**, a subring of $K$ containing the identity, and $\mathfrak{m}_v = \{x : v(x) > 0\}$ is its unique maximal ideal; the **residue field** is $\mathcal{O}_v/\mathfrak{m}_v$. The triple $(K, \mathcal{O}_v)$ is a **valued field**.

**Theorem (Ax–Kochen; Ershov).** Let $(K, v)$ and $(L, w)$ be Henselian valued fields with the same residue characteristic and value group, and suppose that the residue fields are elementarily equivalent or that both are algebraically closed. Then $(K,v)$ and $(L,w)$ are elementarily equivalent; if the residue fields are elementarily equivalent and the value groups are elementarily equivalent as ordered groups, then the valued fields are elementarily equivalent.

The theorem is the model-theoretic content of the classical result that a Henselian field is determined by its residue field and value group, and its proof uses quantifier elimination in a language enriched by predicates for the valuation ring and by a **cross-section** for the value group. The algebraic theory of valuations belongs and the ordered abelian groups to the articles on ordered structures; the theorem is quoted here as an example of the reach of quantifier elimination.

## Ultraproducts

### Ultrafilters and Ultraproducts

The notion of an ultrafilter is that of *Cardinality and the Axiom of Choice*, where it was shown that every filter extends to an ultrafilter.

**Definition.** Let $I$ be a set and let $U$ be an ultrafilter on $I$. For a family $(\mathcal{M}_i)_{i \in I}$ of $L$-structures, the **ultraproduct** $\prod_U \mathcal{M}_i$ is the quotient of the product $\prod_{i \in I} M_i$ by the relation

$$
(f \sim_U g) \iff \{i \in I : f(i) = g(i)\} \in U.
$$

The relation is an equivalence relation because $U$ is a filter; the quotient carries the structure defined coordinatewise and interpreted modulo $U$, and when all $\mathcal{M}_i$ equal a fixed $\mathcal{M}$ the result is the **ultrapower** $\mathcal{M}^I/U$.

**Theorem (Łoś).** For every formula $\varphi(x_1,\ldots,x_n)$ and every tuple $[f_1],\ldots,[f_n]$ of the ultraproduct,

$$
\prod_U \mathcal{M}_i \models \varphi[[f_1],\ldots,[f_n]] \iff \{i \in I : \mathcal{M}_i \models \varphi[f_1(i),\ldots,f_n(i)]\} \in U.
$$

**Proof sketch.** Induction on the complexity of $\varphi$. For an atomic formula the statement is the definition of the coordinatewise interpretation modulo $U$. For a conjunction, the two sets whose membership in $U$ is asserted are the intersection of the two sets for the conjuncts, and an ultrafilter is closed under finite intersections and contains a set exactly when it contains its supersets. For a negation, use that an ultrafilter contains exactly one of a set and its complement. For a quantifier, the existential case is the substantive one: if the set of indices at which a witness exists lies in $U$, one chooses a witness at each such index using the axiom of choice and glues them into a function; the axiom of choice is used exactly here. $\square$

### Consequences

**Corollary (compactness again).** The compactness theorem follows from Łoś's theorem: given a family of models $\mathcal{M}_i$ of the finite subsets of a theory $T$, indexed by the finite subsets themselves and ordered by inclusion, an ultrafilter extending the filter of cofinal sets makes the ultraproduct a model of $T$, since each sentence of $T$ holds in all sufficiently large finite subsets.

**Theorem.** Every structure $\mathcal{M}$ embeds elementarily in its ultrapower $\mathcal{M}^I/U$ by the diagonal map $m \mapsto [\text{constant } m]$, and the embedding is an isomorphism if and only if $U$ is principal. If $U$ is a nonprincipal ultrafilter on $\mathbb{N}$ and $\mathcal{M}$ is infinite, the ultrapower contains elements not in the image of the diagonal embedding.

**Proof sketch.** The diagonal map is elementary by Łoś's theorem, since a sentence true in $\mathcal{M}$ is true at every index. If $U$ is principal at $k$, the projection to the $k$-th coordinate is an isomorphism. If $U$ is nonprincipal and $\mathcal{M}$ is infinite, let $f$ be a function whose values enumerate infinitely many distinct elements; the set of indices at which $f$ agrees with a fixed constant is finite, hence not in $U$, so $[f]$ differs from every constant. $\square$

Ultraproducts give a uniform construction of elementary extensions and are the tool behind **saturation**, the property that a structure realises every finitely satisfiable type over a small parameter set; the language of types, and the topology of the space of types, belong to the further development of the subject and to Part II.

## Summary

A signature fixes the function, relation and constant symbols of a language; an $L$-structure interprets them in a nonempty domain, and satisfaction of a formula under an assignment is defined by recursion. Homomorphisms preserve the positive formulas, embeddings the quantifier-free formulas and isomorphisms every formula; the theory $\operatorname{Th}(\mathcal{M})$ is the set of sentences true in $\mathcal{M}$, and elementary equivalence is equality of theories. Elementary embeddings preserve all formulas with parameters, and the Tarski–Vaught criterion characterises elementary substructures by the existence of witnesses inside the smaller structure; it yields the downward Löwenheim–Skolem theorem.

Definable sets are the extensions of formulas with parameters; they form a Boolean algebra and are invariant under automorphisms fixing the parameters, which is the standard tool for proving non-definability. Compactness, proved in *Formal Logic and Computability*, gives nonstandard models of arithmetic and of analysis, and the Löwenheim–Skolem theorems give models of every infinite cardinality at least that of the language, dissolving the Löwenheim–Skolem paradox.

Quantifier elimination reduces every formula to a quantifier-free one and makes definable sets Boolean combinations of atomic ones; with a decidable quantifier-free part it gives completeness and decidability, and the criterion for it is the extendability of quantifier-free formulas to substructures. The theory of algebraically closed fields admits quantifier elimination, is complete and decidable, and is determined up to elementary equivalence by the characteristic; the theory of real-closed fields admits quantifier elimination, is complete, decidable and o-minimal, so that definable subsets of the line are finite unions of points and intervals; Henselian valued fields are governed by the Ax–Kochen–Ershov theorems relating them to their residue fields and value groups. Ultraproducts, built from a family of structures and an ultrafilter, satisfy Łoś's theorem, which reproduces compactness and constructs elementary extensions; a nonprincipal ultrapower of an infinite structure is a proper elementary extension.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L$, $\mathcal{L}$ | Signature (language): function, relation and constant symbols with arities |
| $\mathcal{M}, \mathcal{N}$; $M, N$ | Structures and their domains (universes) |
| $\mathcal{M} \models \varphi[a]$ | Satisfaction of $\varphi$ in $\mathcal{M}$ under assignment $a$ |
| $\operatorname{Th}(\mathcal{M})$ | Theory of $\mathcal{M}$: sentences true in it |
| $\mathcal{M} \equiv \mathcal{N}$ | Elementary equivalence |
| $\mathcal{M} \preceq \mathcal{N}$ | Elementary substructure |
| $L_{\mathrm{ord}}, L_{\mathrm{ring}}, L_{\mathrm{grp}}$ | Languages of order, of rings, of groups |
| $\varphi(\mathcal{M}, \vec b)$ | Definable set with parameters $\vec b$ |
| $T$, $\mathrm{ACF}$, $\mathrm{ACF}_p$, $\mathrm{RCF}$, DLO | Theories; algebraically closed fields; real-closed fields; dense linear order |
| $v : K \to \Gamma \cup \{\infty\}$ | Valuation, value group $\Gamma$, valuation ring $\mathcal{O}_v$ |
| $\mathfrak{m}_v$ | Maximal ideal of the valuation ring; residue field $\mathcal{O}_v/\mathfrak{m}_v$ |
| $U$ | Ultrafilter on an index set $I$ |
| $\prod_U \mathcal{M}_i$, $\mathcal{M}^I/U$ | Ultraproduct; ultrapower |
| $[f]$ | Equivalence class of $f$ modulo $U$ |



## Further Reading

- Wilfrid Hodges, *Model Theory* (Cambridge University Press, 1993), for the systematic development of structures, elementary equivalence, quantifier elimination and ultraproducts.
- David Marker, *Model Theory: An Introduction* (Springer, 2002), for the applications to algebraically closed, real-closed and valued fields.
- Chang Chen Chung and H. Jerome Keisler, *Model Theory*, 3rd ed. (North-Holland, 1990), for compactness, ultraproducts and Łoś's theorem.
- Abraham Robinson, *Introduction to Model Theory and to the Metamathematics of Algebra* (North-Holland, 1963), for the model-theoretic treatment of algebra and the Ax–Kochen theorems.
- Alfred Tarski, *A Decision Method for Elementary Algebra and Geometry*, 2nd ed. (University of California Press, 1951), for quantifier elimination in real-closed fields.
- Lou van den Dries, *Tame Topology and O-minimal Structures* (Cambridge University Press, 1998), for o-minimality and its consequences.
- James Ax and Simon Kochen, "Diophantine problems over local fields I, II", *American Journal of Mathematics* **87** (1965), 605–630 and 631–648, for the model theory of valued fields.
