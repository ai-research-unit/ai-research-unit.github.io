
# __Algorithmic Randomness and Chaitin's $\Omega$__

## Introduction

This article stands in *Foundations of Analysis*, immediately after *Measure Theory and Integration*, and it is the effective refinement of that measure theory: the null sets are replaced by the effective null sets, and the reals that lie in no such set are the random reals. Both ingredients are above. The measure, the null sets and the measure algebra are *Measure Theory and Integration*, directly above; the computability, the computably enumerable sets and the halting problem are *Formal Logic and Computability*, in Part I, and the effective refinement of the real numbers is not redefined here. The article is in Part III for exactly this reason: it needs measure, which is a Part III object, and placing it in Part I would make a Part I article depend on Part III.

Two boundaries are respected throughout. The article does not build a probability space of its own and does not use the martingale or the betting definitions of randomness; that apparatus belongs to *Probability and Ergodic Theory*, elsewhere in this Part. And the article does not use the combinatorial definitions of complexity beyond what it states; the complexity of a finite string is defined here in the two forms needed, with the theorems cited.

---

## Effective Measure Theory

**Definition.** A real number is **computable** if there is a computable sequence of rationals converging to it with a computable rate of convergence, that is a computable function $n \mapsto q_n \in \mathbb{Q}$ with $|x - q_n| < 2^{-n}$ for every $n$. A set is **computably enumerable** if it is the range of a partial computable function, as in *Formal Logic and Computability*, above; a **computably enumerable real** is the limit of a computable increasing sequence of rationals, that is a real whose left Dedekind cut is computably enumerable.

**Definition.** A **computable open set** is a union $\bigcup_n (a_n, b_n)$ of rational intervals whose endpoints are given by a computable sequence. An **effective null set** is a set of the form

$$
\bigcap_{n \geq 0} U_n ,
$$

where $(U_n)$ is a computable sequence of computable open sets with $U_n \subseteq (0,1)$ and Lebesgue measure $\lambda(U_n) \leq 2^{-n}$ for every $n$. A real $x$ is **Martin-Löf random** if it lies in no effective null set.

**Theorem.** The effective null sets are null sets of *Measure Theory and Integration*, above; their union has measure zero, and consequently the set of Martin-Löf random reals has measure one.

**Proof.** Each effective null set is contained in a null set of the measure theory, since it is contained in $U_n$ for every $n$ and $\lambda(U_n) \to 0$, as in *Measure Theory and Integration*, above. The union of the effective null sets is itself an effective null set: enumerate the computable sequences of rational intervals, and for the $n$-th effective null set inside the enumeration absorb a factor $2^{-n}$, so that the union has measure zero. Hence the union of the effective null sets is null and its complement, the set of random reals, has measure one. $\square$

**Remark.** The definition is the effective form of "almost every": a property holds for almost every real when the set where it fails is null, and it holds for random reals when the failure set is effectively null. The two notions agree in that every effective null set is null, and they differ in that not every null set is effective: there are null sets that contain random reals, so the effective null sets are the ones a computable test can name. The article uses only the effective notion, and the refinement of the Borel sets to the effective hierarchy belongs to *Descriptive Set Theory*, elsewhere in this Part.

---

## Complexity of Finite Strings

**Definition.** Fix a universal partial computable function $U$ on binary strings, as in *Formal Logic and Computability*, above. The **Kolmogorov complexity** of a finite binary string $x$ is

$$
C(x) = \min \{ |p| : U(p) = x \} ,
$$

the length of the shortest program that outputs $x$; the **prefix complexity** $K(x)$ is the same with $U$ required to be prefix-free, that is to have no two inputs one of which is a proper initial segment of the other.

**Theorem (invariance).** The quantities $C$ and $K$ depend on the choice of $U$ only up to an additive constant: for any two universal machines there is a constant $c$ with $|C_1(x) - C_2(x)| \leq c$ for every $x$, and likewise for $K$.

**Proof.** A universal machine can simulate another with a fixed overhead: the simulation program has a fixed finite length, and the simulating machine is universal, so the shortest program on one machine for $x$ is at most the shortest program on the other plus the length of the simulator. The argument for $K$ is the same, the prefix-free requirement being preserved by prefixing a fixed program. $\square$

**Theorem (the counting bound).** For every $n$ and every constant $c$, the number of strings $x$ of length $n$ with $C(x) \leq n - c$ is at most $2^{n-c+1} - 1$; hence the number of strings of length $n$ that are incompressible to within $c$, that is with $C(x) > n - c$, is at least $2^n - 2^{n-c+1}$, a fraction at least $1 - 2^{1-c}$ of all of them.

**Proof.** There are exactly $2^m$ programs of length $m$, so the programs of length at most $n - c$ number $2^{n-c+1} - 1$, and each string has at most one shortest program, so at most that many strings of length $n$ have $C(x) \leq n - c$. The rest follow by subtracting, and the fraction is that number divided by $2^n$. $\square$

**Remark.** The counting bound is the finite form of the statement that almost every real is random: a string of length $n$ that has no short program is incompressible, and the theorem says that all but a fraction $2^{1-c}$ of the strings of length $n$ are incompressible to within $c$. The infinite form is the theorem of the next section.

---

## Chaitin's $\Omega$

**Definition.** Fix a prefix-free universal partial computable function $U$, as in the definition of $K$. **Chaitin's constant** is

$$
\Omega = \sum_{p : U(p) \text{ halts}} 2^{-|p|} ,
$$

the halting probability of $U$: the measure of the set of infinite binary sequences that begin with a program on which $U$ halts.

**Theorem.** The series defining $\Omega$ converges, and $\Omega$ is a real number in $(0,1)$. It is a computably enumerable real: its left Dedekind cut is computably enumerable, by enumerating the halting programs and summing the dyadic contributions.

**Proof.** The prefix-free condition makes the cylinders of the programs pairwise disjoint, so the total measure of their union is $\sum 2^{-|p|}$, which is at most the measure of the whole space, namely $1$; hence the series converges and its sum lies in $[0,1]$. It is positive because some program halts. It is less than $1$: if the sum were $1$ the cylinders of the halting programs would cover the whole space, so every program would be comparable in the prefix order with a halting program; the halting problem would then be decidable, by enumerating the halting programs until one comparable with a given program appears, the prefix-free condition turning that appearance into a decision, and this contradicts *Formal Logic and Computability*, above. The enumeration is the dovetailing of the computations of $U$: when a program of length $|p|$ is found to halt, add $2^{-|p|}$ to the partial sum, which gives a computable increasing sequence of rationals with limit $\Omega$. $\square$

**Theorem (Chaitin).** $\Omega$ is a Martin-Löf random real. Consequently $\Omega$ is not computable, and the halting problem is computable from the binary expansion of $\Omega$: there is an algorithm that, given an oracle for the bits of $\Omega$, decides whether $U(p)$ halts.

**Proof.** That $\Omega$ is random is the standard theorem of the subject, cited from the literature: if $\Omega$ lay in an effective null set, then the incompressibility of the initial segments of $\Omega$ would fail, and the counting bound above would be contradicted infinitely often; the proof uses the prefix complexity $K$ and the fact that the initial segments of a random real are incompressible. That no random real is computable is the fact proved below, so $\Omega$ is not computable. For the last statement, the algorithm enumerates the halting programs until the partial sums exceed the rational number obtained by truncating the expansion of $\Omega$, and the comparison with the truncated value decides halting; the argument is the standard one and is cited. $\square$

**Corollary.** $\Omega$ is transcendental.

**Proof.** Every algebraic real is computable: a defining polynomial with integer coefficients is evaluated exactly at rationals, its roots are isolated by rational intervals, and bisection on such an interval computes the real to any prescribed precision. No computable real is random, by the theorem below, and $\Omega$ is random; so $\Omega$ is not algebraic. $\square$

**Corollary (incompressibility criterion).** A real $x$ is Martin-Löf random exactly when there is a constant $c$ with

$$
K(x \upharpoonright n) \geq n - c
$$

for every $n$, where $x \upharpoonright n$ is the first $n$ bits of $x$.

**Proof.** If $x$ has incompressible initial segments then no effective null set contains $x$, because membership in an effective null set is certified by a computable sequence of tests each of which could be used to compress the initial segments; conversely if $x$ is random then the set of reals whose initial segments are compressible by more than a fixed amount is an effective null set, by the counting bound, so randomness forbids it. The equivalence is the standard one, cited from the literature. $\square$

---

## Immunity and the Failure of Closure

**Theorem.** Every Martin-Löf random real is incomputable: no computable real is random.

**Proof.** Let $x$ be computable. Then the set of reals whose first $n$ bits agree with those of $x$ is a computable open set of measure $2^{-n}$, given by a computable sequence of intervals; the intersection over $n$ of the sets obtained by taking the first $n$ bits and absorbing the factor is an effective null set containing $x$, since the $n$-th open set has measure $2^{-n}$. Hence $x$ is not random. $\square$

**Theorem (immunity).** Let a real $x$ be identified with the set of positions of the ones in its binary expansion. If $x$ is Martin-Löf random, then the set is **immune**: it has no infinite computably enumerable subset. The complement of the set is immune as well.

**Proof.** If $A \subseteq \mathbb{N}$ were an infinite computably enumerable subset of the set of positions of ones of $x$, then the reals whose binary expansion has ones at all elements of $A$ would form an effective null set containing $x$, since $A$ is enumerated by a computable process and the measure of the set of reals with ones prescribed on $n$ elements of $A$ is $2^{-n}$, which can be made to tend to zero computably; so randomness forbids an infinite computably enumerable subset. The same argument with zeros in place of ones gives the statement for the complement. $\square$

**Remark.** Immunity is not sparsity. The effective form of the law of large numbers — that the set of reals whose first $n$ bits contain fewer than $n/3$ ones for infinitely many $n$ is an effective null set, since the measures of the successive events are bounded by a summable sequence — shows that for a random real the number of ones among the first $n$ bits is at least $n/3$ for all large $n$; hence some computable function, say $n \mapsto 3n + c$ for a suitable integer $c$, dominates the principal function of the set, and the set of ones of a random real is dense in the computable sense rather than sparse. What randomness forbids is the existence of an infinite computably enumerable subset, and that is what the theorem states.

**Theorem (failure of closure under arithmetic).** The Martin-Löf random reals are not closed under addition and not closed under multiplication: for every random real $x$ there is a random real $y$ with $x + y$ computable and a random real $z$ with $xz$ computable.

**Proof.** Let $x$ be random and put $y = 1 - x$. The map $t \mapsto 1 - t$ is an isometry of the interval with computable inverse, so it carries a computable open set to a computable open set and preserves Lebesgue measure; hence it carries effective null sets to effective null sets, $y$ is random, and $x + y = 1$ is computable. For the product, let $z = 1/x$, which is defined because a random real is incomputable and hence nonzero; the map $t \mapsto 1/t$ is a computable homeomorphism of the non-zero reals with computable inverse, and that it preserves Martin-Löf randomness is the standard invariance of the notion under computable homeomorphisms, cited from the literature. Hence $z$ is random, while $xz = 1$ is computable. So the sum, and the product, of two random reals can be a computable real, and the classes are not closed. $\square$

**Remark.** The failures above are the standard content of the statement that randomness is not preserved by the arithmetic operations; the set of random reals is large, being of measure one, and it is not closed under the most elementary maps of the field. The corresponding statement for the effective refinement of a general measure space is the theory of the effective null sets, and the refinement of convergence and of probability belongs to *Probability and Ergodic Theory* and to *Modes of Convergence*, elsewhere in this Part, and is not used here.

---

## Summary

The effective refinement of measure theory replaces the null sets of *Measure Theory and Integration*, above, by the effective null sets, the sets of the form $\bigcap_n U_n$ with $(U_n)$ a computable sequence of computable open sets of measure at most $2^{-n}$, and defines the Martin-Löf random reals as those lying in no effective null set; the union of the effective null sets is null and the random reals therefore have measure one. The Kolmogorov and prefix complexities $C$ and $K$ measure the length of the shortest program for a finite string, depend on the machine only up to an additive constant, and satisfy the counting bound, which gives the incompressibility criterion: a real is random exactly when its initial segments are incompressible. Chaitin's $\Omega$ is the halting probability of a prefix-free universal machine, a computably enumerable real that is Martin-Löf random and therefore not computable, and the halting problem is computable from its bits. Every random real is incomputable, the set of ones of a random real and its complement each contain no infinite computably enumerable subset, and the random reals are not closed under addition or multiplication: the sum, and the product, of two random reals can be computable.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Omega$ | Chaitin's halting probability, a computably enumerable real |
| $C(x)$, $K(x)$ | The Kolmogorov and prefix complexity of a finite binary string |
| $U$ | A prefix-free universal partial computable function |
| $x \upharpoonright n$ | The first $n$ bits of a real $x$ |
| $U_n$, $\bigcap_n U_n$ | A computable sequence of computable open sets, and an effective null set |
| $\lambda$ | Lebesgue measure, of *Measure Theory and Integration*, above |
| computably enumerable real | The limit of a computable increasing sequence of rationals |
| Martin-Löf random | Lying in no effective null set |
| immune | Containing no infinite computably enumerable subset |
| $\{0,1\}^{\mathbb{N}}$ | The space of binary sequences, whose cylinders carry the halting probability |

## Further Reading

- R. G. Downey and D. R. Hirschfeldt, *Algorithmic Randomness and Complexity* (Springer, 2010), for the Martin-Löf definition, the complexity of finite strings and the immunity properties of random sets.
- P. Martin-Löf, *The definition of random sequences* (Information and Control, 1966), for the original definition by effective null sets.
- A. Nies, *Computability and Randomness* (Oxford University Press, 2009), for the incompressibility criterion, the halting probability and the failure of closure under the arithmetic operations.
- G. J. Chaitin, *A theory of program size formally identical to information theory* (Journal of the ACM, 1975), for the halting probability and its randomness.
- M. Li and P. Vitányi, *An Introduction to Kolmogorov Complexity and Its Applications* (Springer, 3rd ed. 2008), for the invariance theorem, the counting bound and the two forms of complexity.

