
# __Proof Theory and Type Theory__

## Introduction

Proof theory studies derivations as mathematical objects rather than as instruments of justification. It asks how a proof is shaped, how one proof can be transformed into another, and what structural properties a system of rules possesses. Its two founding results are the **cut-elimination theorem** of Gentzen for the sequent calculus and the **normalisation theorem** for natural deduction: every derivation can be brought into a canonical form in which no detour occurs, and from which the structure of the conclusion can be read off. Type theory is the other face of the same subject: the observation that a derivation in intuitionistic logic is the same thing as a term of a type, the **Curry–Howard correspondence**, which turns logic into a calculus of functions and makes the study of proofs and the study of programs one subject.

The article is the eighth of the corpus, above *Formal Logic and Computability* and *Model Theory*, and it uses the first-order syntax and the formal systems of *Formal Logic and Computability*, the semantic notions of satisfaction and completeness developed there and in *Model Theory*, and the ordinals of *Set-Theoretic Foundations*. It is the second half of the corpus's logical layer: where the earlier articles treated logic through its models, this one treats it through its proofs. It states the natural-deduction and sequent rules, proves the cut-elimination and normalisation theorems in outline, derives their standard consequences — consistency of the logical systems, the disjunction and existence properties, the subformula property — and develops the lambda calculus and its typed versions far enough to state the Curry–Howard correspondence and to describe the principal type theories.

The article does not develop the categorical reading of the correspondence, which requires the language; it points in that direction and stops. It does not develop the semantics of the intuitionistic propositional calculus, which is the subject of *Model Theory* and of *Set-Theoretic Foundations* through the notion of a Heyting algebra. The results it proves about derivations are finitary and combinatorial, and the only structure it uses beyond first-order syntax is that of the ordinals, for the ordinal analysis at the end.

## Natural Deduction

### Rules and Derivations

**Definition.** A **natural-deduction derivation** is a finite tree whose nodes are formulas, whose leaves are the **assumptions** (each annotated with an assumption class), and whose internal nodes are instances of the **rules of inference**. The rules are the **introduction** and **elimination** rules for each connective and quantifier.

The propositional rules are the following, where a formula above a line is a premise and one below is the conclusion; an assumption class discharged by a rule is written in brackets.

$$
\frac{\varphi \qquad \psi}{\varphi \wedge \psi} \wedge I
\qquad
\frac{\varphi \wedge \psi}{\varphi} \wedge E_1
\qquad
\frac{\varphi \wedge \psi}{\psi} \wedge E_2
$$

$$
\frac{[\varphi]}{\psi} \quad
\frac{}{\varphi \to \psi} \to I
\qquad
\frac{\varphi \to \psi \qquad \varphi}{\psi} \to E
$$

$$
\frac{\varphi}{\varphi \vee \psi} \vee I_1
\qquad
\frac{\psi}{\varphi \vee \psi} \vee I_2
\qquad
\frac{\varphi \vee \psi \quad [\varphi] \quad [\psi]}{\chi} \vee E
$$

with the side condition for $\vee E$ that the assumptions of the two minor premises other than $\varphi$ and $\psi$ remain undischarged. Negation is defined: $\neg\varphi$ abbreviates $\varphi \to \bot$, with the rules $\bot E$, whose conclusion is any formula, and the derived rule $\neg E$, from $\varphi$ and $\neg\varphi$ to $\bot$. The quantifier rules adjoin $\forall I$, from $\varphi$ to $\forall x\,\varphi$ with the **eigenvariable condition** that $x$ not occur free in any undischarged assumption, and $\exists E$, from $\exists x\,\varphi$ and a derivation of $\psi$ from $\varphi$ to conclude $\psi$ with the analogous condition.

**Definition.** A **theory** in natural deduction consists of a set of **nonlogical axioms**, formulas of the language taken as undischarged leaves. A formula $\varphi$ is **derivable** from a theory $T$, written $T \vdash \varphi$, if some derivation with conclusion $\varphi$ has all its undischarged assumptions among the nonlogical axioms and the formulas of $T$. A **proof** is a derivation with no undischarged assumptions.

**Proposition (deduction theorem).** $T \cup \{\varphi\} \vdash \psi$ if and only if $T \vdash \varphi \to \psi$.

**Proof.** From $T \vdash \varphi \to \psi$ and $T \cup \{\varphi\} \vdash \varphi$ one concludes $T \cup \{\varphi\} \vdash \psi$ by $\to E$. Conversely, given a derivation of $\psi$ from $T \cup \{\varphi\}$, add the assumption $\varphi$ at the leaves discharging to $\varphi$ and apply $\to I$ at the root. $\square$

**Definition (sequent notation).** The derivation tree is more compactly written as a **sequent** $\Gamma \vdash \varphi$, where $\Gamma$ is the multiset of undischarged assumptions and $\varphi$ the conclusion. The rules are then displayed with sequents as premises and conclusion. The derivation of the previous proposition is exactly the passage between the two notations.

### Intuitionistic and Classical Logic

The rules above constitute **intuitionistic** logic: the systems of *Logic and Proof* and *Formal Logic and Computability* without the axiom of excluded middle. Classical logic is obtained by adjoining one of the equivalent principles

$$
\varphi \vee \neg\varphi, \qquad \neg\neg\varphi \to \varphi, \qquad (\varphi \to \psi) \to \neg\varphi \vee \psi,
$$

any one of which is derivable from the others in the intuitionistic system together with the rest. The rule of **double-negation elimination** is the official classical addition, and the resulting system is denoted NK, with the intuitionistic one NJ.

**Example.** $\varphi \vee \neg\varphi$ is not derivable in NJ. If it were, a normal derivation of it would exist by the normalisation theorem below, and a derivation of a disjunction that contains no detour must end in a $\vee I$ rule with the same conclusion; it would then be a derivation of $\varphi$ from no assumptions or a derivation of $\neg\varphi$ from no assumptions, and neither is derivable for a general $\varphi$ (a normal derivation of $\neg\varphi$ would end in $\to I$ with conclusion $\varphi \to \bot$, which requires a derivation of $\bot$ from $\varphi$, and no rule introduces $\bot$).

The disjunction property illustrated by the example is proved in general for intuitionistic logic below; it fails for classical logic, since $\varphi \vee \neg\varphi$ is a theorem with neither disjunct a theorem.

**Definition.** A formula is **classically valid** if it holds in every structure in the sense of *Model Theory*; it is **intuitionistically valid** if it is derivable in NJ. Soundness and completeness for NJ are stated with respect to **Kripke models**, and the classical completeness theorem of *Formal Logic and Computability* is the special case of a single world; the corpus cites the standard treatment for the details.

## Sequent Calculi

### Sequents and Rules

A second formulation, more symmetric than natural deduction, is Gentzen's **sequent calculus**.

**Definition.** A **sequent** is an expression $\Gamma \vdash \Delta$ in which $\Gamma$ and $\Delta$ are finite multisets of formulas. Its intended meaning is that the conjunction of $\Gamma$ implies the disjunction of $\Delta$. The **sequent calculus LK** has the following rules, in addition to the **initial sequents** $\varphi \vdash \varphi$ and $\bot \vdash$.

$$
\frac{\Gamma \vdash \Delta, \varphi \qquad \varphi, \Pi \vdash \Lambda}{\Gamma, \Pi \vdash \Delta, \Lambda} \ \text{cut}
\qquad
\frac{\Gamma \vdash \Delta, \varphi \qquad \Gamma \vdash \Delta, \psi}{\Gamma \vdash \Delta, \varphi \wedge \psi} \wedge R
\qquad
\frac{\varphi, \Gamma \vdash \Delta}{\varphi \wedge \psi, \Gamma \vdash \Delta} \wedge L_1
$$

$$
\frac{\varphi, \Gamma \vdash \Delta, \psi}{\Gamma \vdash \Delta, \varphi \to \psi} \to R
\qquad
\frac{\Gamma \vdash \Delta, \varphi \qquad \psi, \Pi \vdash \Lambda}{\varphi \to \psi, \Gamma, \Pi \vdash \Delta, \Lambda} \to L
$$

$$
\frac{\varphi, \Gamma \vdash \Delta \qquad \psi, \Gamma \vdash \Delta}{\varphi \vee \psi, \Gamma \vdash \Delta} \vee L
\qquad
\frac{\Gamma \vdash \Delta, \varphi}{\Gamma \vdash \Delta, \varphi \vee \psi} \vee R_1
\qquad
\frac{\Gamma \vdash \Delta, \varphi(x)}{\Gamma \vdash \Delta, \forall x\,\varphi(x)} \forall R
$$

with the remaining rules for $\neg$, $\forall L$, the two $\exists$ rules and the **structural rules** of weakening and contraction. The system **LJ** for intuitionistic logic restricts $\Delta$ to at most one formula, and the restriction is what excludes the classical derivations of excluded middle.

**Example.** The law of excluded middle has the following LK derivation, read from the initial sequent at the top downwards:

$$
\frac{\varphi \vdash \varphi}{\vdash \varphi, \neg\varphi} \neg R
\quad \longrightarrow \quad
\frac{\vdash \varphi, \neg\varphi}{\vdash \varphi \vee \neg\varphi, \neg\varphi} \vee R_1
\quad \longrightarrow \quad
\frac{\vdash \varphi \vee \neg\varphi, \neg\varphi}{\vdash \varphi \vee \neg\varphi, \varphi \vee \neg\varphi} \vee R_2
\quad \longrightarrow \quad
\frac{\vdash \varphi \vee \neg\varphi, \varphi \vee \neg\varphi}{\vdash \varphi \vee \neg\varphi} CR
$$

The final step is contraction on the right, which is available in LK; in LJ the right side holds at most one formula, so the two copies of $\varphi \vee \neg\varphi$ cannot both appear and the derivation is blocked.

### Cut Elimination

**Definition.** The **cut rule** is the only rule of LK in which a formula, the **cut formula** $\varphi$, disappears in passing from the premises to the conclusion. The **subformula property** of a derivation is that every formula occurring in it is a subformula of the conclusion or of the initial sequents; a derivation with the cut rule need not have it.

**Theorem (Gentzen's Hauptsatz; cut elimination).** Every LK derivation of a sequent has a cut-free derivation of the same sequent. The same holds for LJ.

**Proof sketch.** One assigns to each derivation a **cut rank**, the maximum size of a cut formula, and a measure of the number of cuts of that rank, and shows that a derivation with a cut can be transformed into one with a smaller measure. The essential case is a cut whose cut formula is introduced by the last rules on both sides; it is replaced by two cuts on formulas of smaller size, using the rules that introduced the connectives. The transformation is the **reduction** of the cut, and iterating it terminates by induction on the cut rank, with the number of cuts of maximal rank decreasing at each step. $\square$

**Corollary (subformula property).** Every theorem of LK or LJ has a derivation in which every formula is a subformula of the theorem.

**Corollary (consistency).** LK is consistent: the sequent $\vdash$ (the empty sequent, expressing a contradiction) has no cut-free derivation, since no rule has the empty sequent as conclusion and the initial sequents have formulas on at least one side.

**Corollary (disjunction and existence properties of LJ).** If $\vdash \varphi \vee \psi$ is derivable in LJ, then $\vdash \varphi$ or $\vdash \psi$; if $\vdash \exists x\,\varphi(x)$ is derivable, then $\vdash \varphi(t)$ is derivable for some term $t$.

**Proof sketch.** In a cut-free derivation of $\vdash \varphi \vee \psi$, the last rule must be the introduction of the disjunction, since no other rule can introduce a disjunction on the right without a cut; its premise is a derivation of one of the disjuncts. For the existential statement, the last rule must be $\exists R$, and its premise supplies a witness term. $\square$

Cut elimination is the central theorem of proof theory and the model of every later result of the same shape: it converts a derivation into one whose structure follows the structure of its conclusion, and the byproducts — the subformula property, consistency, the disjunction property — are all immediate from that structure.

**Remark (consistency of arithmetic).** For a system with the induction schema, cut elimination does not suffice, because the axiom of induction is not a rule of the calculus and the cut-elimination argument applies only to the logical rules. Gentzen's consistency proof for arithmetic uses cut elimination on an infinitary version of the calculus together with transfinite induction up to the ordinal $\varepsilon_0 = \sup\{\omega, \omega^\omega, \omega^{\omega^\omega}, \ldots\}$, and the ordinal is the **proof-theoretic ordinal** of the theory. That the well-foundedness of $\varepsilon_0$ is itself unprovable in arithmetic is the content of Gödel's second incompleteness theorem of *Formal Logic and Computability* applied to Gentzen's proof.

## Normalisation

### Normalisation for Natural Deduction

**Definition.** In a natural-deduction derivation, an **introduction followed immediately by an elimination** of the same connective is a **detour** (or **redex**), for instance a derivation of $\varphi \wedge \psi$ by $\wedge I$ used as the premise of $\wedge E_1$, or a derivation of $\varphi \to \psi$ by $\to I$ used as the premise of $\to E$. The **reduction** of a detour replaces it by a derivation of the same conclusion without it.

**Theorem (normalisation).** Every derivation in NJ reduces to a **normal** derivation, in which no detour occurs. Consequently every derivation in NJ reduces to one with the **subformula property**: every formula in it is a subformula of the conclusion or of an undischarged assumption.

**Proof sketch.** Assign to each formula its **degree** and to each derivation the pair (highest degree of a detour, number of detours of that degree). The reduction of a detour of maximal degree produces detours of strictly smaller degree or fewer detours of the same degree, so the pair decreases in the lexicographic order on natural numbers, and the process terminates. The result is a normal derivation. In a normal derivation, an introduction rule cannot be followed by an elimination of the same connective, which forces the derivation to have the **path property**: every formula on a path from a leaf to the root is a subformula of the leaf or of the conclusion, giving the subformula property. $\square$

**Corollary.** NJ is consistent: there is no derivation of $\bot$ from no assumptions. Indeed, $\bot$ has no introduction rule, so a normal derivation of $\bot$ must end in an elimination rule; its major premise is then a formula which, by normality, is the conclusion of an introduction rule, and the two form a detour, unless the major premise is an undischarged assumption — and there is none. Hence no derivation of $\bot$ from no assumptions exists.

### Strong Normalisation for Typed Systems

**Definition.** A term of a typed system is **strongly normalising** if every reduction sequence starting from it terminates. It is **weakly normalising** if some sequence terminates. A system has the **Church–Rosser** (confluence) property if whenever a term reduces to two terms, both reduce to a common term.

**Theorem (strong normalisation).** Every term of the simply typed lambda calculus of the next section is strongly normalising; equivalently, every derivation of intuitionistic propositional logic reduces to a normal form in finitely many steps, whatever the order of reduction.

**Proof sketch.** One assigns to each type a **reducibility candidate**, a set of strongly normalising terms closed under reduction and under application, and proves by induction on the type that every term of that type belongs to the candidate. The argument, due to Tait, is the prototype of the **computability** arguments used throughout proof theory and type theory. $\square$

Strong normalisation is strictly stronger than the normalisation theorem for derivations; it says that no clever choice of reduction order can cause a loop, which is what is needed to run a typed program with the guarantee that it halts. The untyped lambda calculus below fails it.

## The Lambda Calculus

### Syntax and Reduction

**Definition.** The **terms** of the lambda calculus are the variables $x, y, \ldots$, the **applications** $MN$ and the **abstractions** $\lambda x.\,M$, together with the constant for the identity and function formation. **$\alpha$-conversion** renames bound variables, and **substitution** $M[x := N]$ replaces free occurrences of $x$ by $N$, renaming bound variables to avoid capture. The **$\beta$-reduction** is

$$
(\lambda x.\,M)\,N \to_\beta M[x := N],
$$

and **$\eta$-reduction** is $\lambda x.\,Mx \to_\eta M$ when $x$ is not free in $M$. A term is in **$\beta$-normal form** if it contains no $\beta$-redex $(\lambda x.\,M)N$.

**Theorem (Church–Rosser).** The relation $\to_\beta$ is confluent: if $M \to_\beta^* N_1$ and $M \to_\beta^* N_2$ then there is $P$ with $N_1 \to_\beta^* P$ and $N_2 \to_\beta^* P$. Consequently a term has at most one $\beta$-normal form.

The proof is by the **Tait–Martin-Löf** method of parallel reduction, or by the Rosser argument on residuals; either reduces confluence to a diamond property for a suitably defined reduction.

**Example (Church numerals).** The natural numbers are represented by the terms

$$
\bar n = \lambda f.\,\lambda x.\,\underbrace{f(f(\cdots f}_{n}\,x)\cdots),
$$

so that $\bar 0 = \lambda f.\lambda x.x$ and $\bar{n+1} = \lambda f.\lambda x.\,f(\bar n\,f\,x)$. Addition is represented by the term

$$
\mathsf{add} = \lambda m.\lambda n.\lambda f.\lambda x.\,m\,f\,(n\,f\,x),
$$

which reduces as $\mathsf{add}\,\bar m\,\bar n \to_\beta^* \overline{m+n}$. The verification is by induction on $m$ and is the content of the computation below.

**Example (fixed points).** The **fixed-point combinator**

$$
Y = \lambda f.\,(\lambda x.\,f(x\,x))(\lambda x.\,f(x\,x))
$$

satisfies $Y\,f =_\beta f\,(Y\,f)$ for every term $f$, since both sides reduce to $f\big((\lambda x.\,f(x\,x))(\lambda x.\,f(x\,x))\big)$; every term therefore has a fixed point up to $\beta$-conversion. The property is the source of both the computational power of the calculus and its failure to be normalising: the term $\Omega = (\lambda x.\,x\,x)(\lambda x.\,x\,x)$ reduces in one step to itself, so it has no normal form.

### Undecidability and Expressiveness

**Theorem (Church; Turing).** The untyped lambda calculus is computationally universal: every recursive function is represented by a term. Moreover the problem of deciding whether a given term has a normal form, and the problem of deciding whether two terms are $\beta$-convertible, are undecidable.

**Proof sketch.** The Church numerals and the combinators for primitive recursion represent the initial recursive functions of *Formal Logic and Computability*, and minimisation is represented by a search whose termination is tested by a fixed point; the converse representation of terms by natural numbers gives the undecidability by the halting problem. The fixed-point combinator $Y$ is the mechanism that makes the representation of recursion possible. $\square$

## The Curry–Howard Correspondence

### Propositions as Types

The correspondence is a dictionary in which formulas are types, derivations are terms, and the rules of natural deduction are the typing rules of a calculus of functions.

| Logic | Type theory |
|---|---|
| Formula $\varphi$ | Type $A$ |
| Derivation of $\varphi$ from assumptions | Term $M$ of type $A$ in context |
| Assumption $\varphi$ | Variable $x : A$ |
| $\varphi \to \psi$ | Function type $A \to B$ |
| $\varphi \wedge \psi$ | Product type $A \times B$ |
| $\varphi \vee \psi$ | Sum type $A + B$ |
| $\bot$ | Empty type $\mathbf{0}$ |
| $\top$ | Unit type $\mathbf{1}$ |
| $\forall x\,\varphi$ | Dependent function type $\Pi x : A.\,B(x)$ |
| $\exists x\,\varphi$ | Dependent sum type $\Sigma x : A.\,B(x)$ |

**Theorem (Curry–Howard, for implication).** The derivations of the implicational fragment of intuitionistic propositional logic from assumptions $\varphi_1,\ldots,\varphi_n$ correspond exactly to the terms of the simply typed lambda calculus in context $x_1 : \varphi_1, \ldots, x_n : \varphi_n$, with

$$
\frac{\Gamma, x : \varphi \vdash M : \psi}{\Gamma \vdash \lambda x.\,M : \varphi \to \psi} \to I
\qquad
\frac{\Gamma \vdash M : \varphi \to \psi \qquad \Gamma \vdash N : \varphi}{\Gamma \vdash M\,N : \psi} \to E,
$$

and $\beta$-reduction of terms corresponds to the reduction of detours in the derivation, while $\eta$-conversion corresponds to the two-way equivalence of a detour with the derivation obtained by removing it.

**Proof.** Structural induction on derivations and on terms: each rule of NJ corresponds to a typing rule, and each typing rule to a rule of NJ, with the variables of the context corresponding to undischarged assumptions. The reduction of a detour $(\to I)$ followed by $(\to E)$ is exactly the substitution $(\lambda x.M)N \to_\beta M[x:=N]$. $\square$

**Corollary.** Normalisation of NJ derivations is equivalent to weak normalisation of the simply typed lambda calculus, and the disjunction and existence properties of NJ are the **canonicity** properties of the corresponding type theory.

The correspondence extends to the full language: product types realise conjunctions, sum types disjunctions, the empty type falsity, and dependent types the quantifiers. Under it, a proof of a proposition is a program of the corresponding type and the normal form of the program is the canonical proof; the execution of the program is the removal of detours in the proof. This is the reason type theory is the foundation of proof assistants and of the computational reading of constructive mathematics.

### Simply Typed Lambda Calculus

**Definition.** The **simple types** are generated from a set of base types by the rule: if $A$ and $B$ are types, so is $A \to B$. The **simply typed lambda calculus** $\lambda_\to$ has the terms of the lambda calculus together with the typing rules above, the product and sum rules when the corresponding connectives are present, and the base constants. Its reduction is $\beta$ (and $\eta$).

**Theorem.** $\lambda_\to$ has the Church–Rosser property and is strongly normalising. Its definable functions on the natural numbers — those represented by terms of type $(\iota \to \iota) \to \iota \to \iota$ for a base type $\iota$ — are exactly the **extended polynomials**, that is, the functions built from addition, multiplication and the conditional on zero; consequently the untyped fixed-point combinator $Y$ is not typable in $\lambda_\to$.

Strong normalisation is the proof-theoretic strength of $\lambda_\to$: since every term normalises, every function definable in it is total, and the class of definable functions is small. Adding the fixed-point combinator to a typed system destroys strong normalisation, and the programming languages that admit general recursion pay for it with the possibility of nontermination.

### Polymorphism and Dependent Types

**Definition.** **System F** (the second-order lambda calculus, or the polymorphic lambda calculus) adds **type variables** and **quantification over types**: if $A$ is a type, so is $\forall X.\,A$, with the rules

$$
\frac{\Gamma \vdash M : A}{\Gamma \vdash \Lambda X.\,M : \forall X.\,A} \quad (X \text{ not free in } \Gamma)
\qquad
\frac{\Gamma \vdash M : \forall X.\,A}{\Gamma \vdash M\,B : A[X := B]}
$$

and the corresponding $\beta$-reduction $(\Lambda X.M)B \to M[X:=B]$. System F is strongly normalising and its definable functions on the Church numerals are exactly the ones provably total in **second-order arithmetic**, which is the proof-theoretic strength of the system. The impredicativity of $\forall X$ is what gives it that strength: a type may be quantified over all types, including itself.

**Definition.** A **dependent type theory** adds types depending on terms. If $A$ is a type and $B(x)$ a type for $x : A$, then $\Pi x : A.\,B(x)$ is the type of functions taking $x$ to a term of $B(x)$, and $\Sigma x : A.\,B(x)$ is the type of pairs $(a,b)$ with $a : A$ and $b : B(a)$. The **lambda cube** arranges the systems obtained by allowing, independently, terms to depend on types ($\lambda_\to$ and its extension to polymorphism), types to depend on types (type operators) and types to depend on terms (dependency); its eight vertices include $\lambda_\to$, System F, and the **calculus of constructions**, the type theory of the Coq proof assistant.

**Definition.** **Martin-Löf type theory** is a dependent type theory with $\Pi$, $\Sigma$, a type of natural numbers, and **identity types** $\mathrm{Id}_A(a,b)$, whose elements are witnesses that $a$ and $b$ are equal. Its **propositions-as-types** reading strengthens the Curry–Howard correspondence: a proposition is a type, a proof is an element, and the equality of two proofs is itself a type. The identity types are the origin of **homotopy type theory**, in which a type is read as a space and its identity types as path spaces; that reading requires the topological language of Part II and is not developed here.

**Remark.** The correspondence between proofs and terms means that a **proof assistant** is a type checker: a formal proof is a term whose type is the theorem, and the correctness of the proof is the correctness of the typing derivation. The strong normalisation of the underlying type theory is what guarantees that a checked proof cannot be circular, and the impossibility of typing the fixed-point combinator is what forbids a proof from referring to itself. The corpus returns to these systems, where the categorical semantics of the typed calculi — the interpretation of types as objects and terms as morphisms — is available.

## Summary

Natural deduction is a calculus of introduction and elimination rules for each connective and quantifier, with assumptions discharged by the introduction rules and with the deduction theorem relating entailment and implication. The intuitionistic system NJ omits the law of excluded middle, and $\varphi \vee \neg\varphi$ is not derivable in it; classical logic NK is obtained by adding the rule of double-negation elimination. The sequent calculus LK is the symmetric formulation, with initial sequents and structural rules, and LJ is its intuitionistic restriction.

Gentzen's cut-elimination theorem removes the cut rule from every derivation, yielding the subformula property, the consistency of the logical systems, and the disjunction and existence properties of LJ. The normalisation theorem for natural deduction is the same result in a different shape, removing detours from a derivation; the consistency of arithmetic requires the stronger method of ordinal analysis, with proof-theoretic ordinal $\varepsilon_0$.

The lambda calculus has variables, application and abstraction, with $\beta$- and $\eta$-reduction; it is confluent by the Church–Rosser theorem and computationally universal, and the fixed-point combinator $Y$ gives every term a fixed point and produces terms such as $\Omega$ with no normal form, so the calculus is undecidable. The simply typed lambda calculus and its extensions are strongly normalising; the definable functions are the extended polynomials for $\lambda_\to$ and the provably total functions of second-order arithmetic for System F.

The Curry–Howard correspondence identifies propositions with types, derivations with terms, and the reduction of detours with $\beta$-reduction; product, sum, empty and unit types realise conjunction, disjunction, falsity and truth, and dependent types realise the quantifiers. Martin-Löf type theory adds identity types and gives the propositions-as-types reading its strongest form, and the lambda cube arranges the typed systems by what depends on what. The categorical semantics of these calculi belongs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Gamma \vdash \varphi$ | Sequent: $\varphi$ derivable from the assumptions $\Gamma$ |
| $\varphi \to \psi$, $\varphi \wedge \psi$, $\varphi \vee \psi$, $\neg\varphi$, $\bot$, $\top$ | Connectives; falsity and truth |
| $\forall x\,\varphi$, $\exists x\,\varphi$ | Quantifiers |
| $\wedge I, \wedge E$, $\to I, \to E$, $\vee I, \vee E$ | Introduction and elimination rules |
| NJ, NK | Intuitionistic and classical natural deduction |
| LK, LJ | Classical and intuitionistic sequent calculi |
| $\Gamma \vdash \Delta$ | Sequent with multisets on both sides |
| $M[x := N]$ | Substitution of $N$ for free $x$ in $M$ |
| $\lambda x.\,M$, $MN$ | Abstraction and application |
| $\to_\beta$, $\to_\eta$ | $\beta$-reduction, $\eta$-reduction |
| $\bar n$ | Church numeral |
| $Y$, $\Omega$ | Fixed-point combinator; the looping term $(\lambda x.xx)(\lambda x.xx)$ |
| $A \to B$, $A \times B$, $A + B$ | Function, product and sum types |
| $\Pi x : A.\,B(x)$, $\Sigma x : A.\,B(x)$ | Dependent function and sum types |
| $\mathrm{Id}_A(a,b)$ | Identity type |
| $\lambda_\to$, System F | Simply typed and polymorphic lambda calculus |
| $\varepsilon_0$ | Proof-theoretic ordinal of arithmetic |



## Further Reading

- Gerhard Gentzen, "Untersuchungen über das logische Schließen I, II", *Mathematische Zeitschrift* **39** (1935), 176–210 and 405–431, for natural deduction, the sequent calculus and cut elimination.
- Gerhard Gentzen, "Die Widerspruchsfreiheit der reinen Zahlentheorie", *Mathematische Annalen* **112** (1936), 493–565, for the consistency of arithmetic by transfinite induction.
- Dag Prawitz, *Natural Deduction: A Proof-Theoretical Study* (Almqvist and Wiksell, 1965; reprinted Dover, 2006), for normalisation and the structure of normal derivations.
- Jean-Yves Girard, Paul Taylor and Yves Lafont, *Proofs and Types* (Cambridge University Press, 1989), for System F, strong normalisation and the Curry–Howard correspondence.
- Haskell B. Curry and Robert Feys, *Combinatory Logic*, vol. 1 (North-Holland, 1958), for the original formulation of the propositions-as-types idea.
- William A. Howard, "The formulae-as-types notion of construction", in *To H. B. Curry: Essays on Combinatory Logic, Lambda Calculus and Formalism* (Academic Press, 1980), 479–490, for the correspondence in its modern form.
- Per Martin-Löf, *Intuitionistic Type Theory* (Bibliopolis, 1984), for dependent type theory and identity types.
- Henk Barendregt, *The Lambda Calculus: Its Syntax and Semantics*, rev. ed. (North-Holland, 1984), for the untyped calculus, confluence and undecidability.
- Wolfram Pohlers, *Proof Theory: The First Step into Impredicativity* (Springer, 2009), for ordinal analysis and proof-theoretic ordinals.
