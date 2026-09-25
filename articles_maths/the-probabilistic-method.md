
# __The Probabilistic Method__

## Introduction

The probabilistic method is the technique of proving the existence of a mathematical object by choosing it at random and showing that the probability that it has the required property is positive. The proof is not constructive — it exhibits no object — but it is complete, and it settles questions that have no known constructive solution. The method was introduced by Erdős in his proof that the Ramsey numbers grow at least exponentially, and it has developed into a body of technique — the first and second moment methods, the Lovász local lemma, the alteration method, the entropy method and the container method — that decides problems in combinatorics, in graph theory, in number theory and in group theory.

This article develops the method and its principal techniques. It sets out the counting and union-bound arguments that reduce an existence statement to an expectation, proves the second moment criterion, states the Lovász local lemma with its proof and its standard applications, exhibits the alteration method on the classical construction of graphs of large girth and large chromatic number, develops the entropy and container methods, and records the concentration inequalities — Chernoff, Hoeffding, Azuma and McDiarmid — that supply the quantitative form of the method. The examples are the classical ones of the subject.

The place of the article is fixed by four boundaries.

- The **probability** — the probability space, the expectation, the moments, the inequalities of Markov and Chebyshev, the independence, the laws of large numbers, the martingales and the entropy — is the block *Measure-Theoretic Probability* through *Ergodic Theory*, and this article uses those results throughout: the Markov and Chebyshev inequalities are the first-moment and second-moment engines, the Azuma inequality is the martingale concentration inequality, and the entropy method of the last sections uses the Kolmogorov–Sinai entropy of *Ergodic Theory* and the Shannon entropy of *Measure-Theoretic Probability*.
- The **combinatorics, the graph theory and the extremal problems** — the Ramsey numbers, the chromatic number, the independence number, the set systems, the hypergraphs, the discrepancy of set systems and the counting arguments — are the subject of the Part I articles on combinatorics and of *Combinatorial Group Theory*, and the finite counting under the action of a group — the orbit-counting lemma, the cycle index, the symmetric group, the generation of a finite group by random elements — is *Combinatorial Group Theory* and the group-theory articles of Part I. The probabilistic statements about the generation of a group and about the Cayley graphs are proved by the method and quoted from there.
- The **number-theoretic** uses of the method — the random sieve, the distribution of arithmetic functions, the random multiplicative functions and the limiting distributions — areand the **arithmetic articles** of Part I, in particularand *Analytic Number Theory*, supply the objects. This article does not develop number theory.
- The **random walks on groups** and the random walks whose trajectories are the objects of the method areand the **applications of the method to the analysis of a fixed number system** are Part V's. No physics is invoked.

Throughout, $(\Omega,\mathcal{F},\mathbb{P})$ is a probability space as in *Measure-Theoretic Probability*, $\mathbb{E}$ is the expectation, $\mathbf{1}_A$ is the indicator of an event, $\ln$ and $\log$ are natural logarithms, and $X, Y$ are random variables with finite moments when their moments are used. For a finite set $\Omega$ with the uniform probability and a subset $A \subseteq \Omega$ one has $\mathbb{P}(A) = |A|/|\Omega|$, and the **first moment method** refers to the inequality of Markov, the **second moment method** to the inequality of Chebyshev and its refinements, and $O(\cdot)$, $o(\cdot)$ to the usual asymptotic notation.

## The Union Bound and the First Moment Method

### The Two Elementary Inequalities

**Proposition (union bound).** For any finite or countable family of events $\{A_i\}$,

$$
\mathbb{P}\!\left(\bigcup_i A_i\right) \leq \sum_i\mathbb{P}(A_i).
$$

**Proposition (first moment method).** Let $X \geq 0$ be a random variable taking values in a countable set. If $\mathbb{E}[X] < 1$ then $\mathbb{P}(X = 0) > 0$; more generally, if $\mathbb{E}[X] \leq k$ then $\mathbb{P}(X \leq k) > 0$. When $X$ counts the defects of a random object, the object is defect-free with positive probability.

*Proof.* Markov's inequality gives $\mathbb{P}(X \geq 1) \leq \mathbb{E}[X] < 1$, so $\mathbb{P}(X = 0) > 0$. For the second statement, $\mathbb{P}(X \geq k+1)\leq \mathbb{E}[X]/(k+1) < 1$. $\square$

The two propositions are the workhorses of the method, and they are the measure-theoretic statements behind the whole technique: the union bound controls the event that some bad configuration occurs, and the first moment bound controls the expected number of bad configurations. The usual pattern is: define a random object, count the expected number of defects, and if the expectation is below one, conclude that a defect-free object exists.

### Ramsey Numbers

**Definition.** The **Ramsey number** $R(k,\ell)$ is the least $n$ such that every red-blue colouring of the edges of $K_n$ contains a red $K_k$ or a blue $K_\ell$. The diagonal case is $R(k,k)$.

**Theorem (Erdős).** For every $k \geq 3$, $R(k,k) > 2^{k/2}$.

*Proof.* Colour the edges of $K_n$ independently red or blue with probability $1/2$ each. For a fixed set $S$ of $k$ vertices let $A_S$ be the event that all edges inside $S$ have the same colour. Then $\mathbb{P}(A_S) = 2\cdot 2^{-\binom{k}{2}} = 2^{1-\binom{k}{2}}$, and the expected number of monochromatic $K_k$ is

$$
\mathbb{E}[X] = \binom{n}{k}2^{1-\binom{k}{2}} < \frac{n^k}{k!}\,2^{1-k(k-1)/2}.
$$

Taking $n = \lfloor 2^{k/2}\rfloor$ gives $\mathbb{E}[X] < 2^{k/2+1}/k!$, and $k! \geq 2^{k/2+1}$ for $k \geq 3$; hence $\mathbb{E}[X] < 1$, so $\mathbb{P}(X = 0) > 0$: there is a colouring with no monochromatic $K_k$, and $R(k,k) > n$. $\square$

The proof is the original application of the method and it remains its model: a probabilistic construction proves a lower bound that no explicit construction matches, and the gap between the bound $2^{k/2}$ and the upper bound $R(k,k) \leq 4^k$ remains one of the classical open problems.

**Example (the tournament and the digraph).** The same argument proves the existence of a tournament on $n$ vertices with no transitive subtournament of size $k$ for $k = 2\log_2n - 2\log_2\log_2n + O(1)$; the count of transitive subtournaments is $\binom{n}{k}k!\,2^{-\binom{k}{2}}$, and the first moment bound makes it below one.

### Set Systems and Hypergraph Colouring

**Theorem (property B).** Every $k$-uniform hypergraph with fewer than $2^{k-1}$ edges is 2-colourable in the sense that no edge is monochromatic.

*Proof.* Colour the vertices independently red or blue with probability $1/2$. For a fixed edge $E$ of size $k$ the probability that $E$ is monochromatic is $2^{1-k}$, so the expected number of monochromatic edges is $m2^{1-k} < 1$ when $m < 2^{k-1}$; the first moment method gives a colouring with no monochromatic edge. $\square$

The bound is the first and simplest of the colouring results, and it is the entry point of the local lemma, which replaces the counting of all edges by the counting of the edges through each vertex.

## The Second Moment Method

### The Variance Criterion

**Theorem (second moment method).** Let $X \geq 0$ be a random variable with finite second moment and $\mathbb{E}[X] > 0$. Then

$$
\mathbb{P}(X = 0) \leq \frac{\operatorname{Var}(X)}{\mathbb{E}[X]^2}, \qquad \text{and hence} \qquad \mathbb{P}(X > 0) \geq 1 - \frac{\operatorname{Var}(X)}{\mathbb{E}[X]^2}.
$$

*Proof.* By the Cauchy–Schwarz inequality, $\mathbb{E}[X]^2 = \mathbb{E}[X\mathbf{1}_{\{X>0\}}]^2 \leq \mathbb{E}[X^2]\,\mathbb{P}(X > 0)$, whence $\mathbb{P}(X>0) \geq \mathbb{E}[X]^2/\mathbb{E}[X^2]$; subtracting from $1$ and using $\mathbb{E}[X^2] = \operatorname{Var}(X) + \mathbb{E}[X]^2$ gives the stated form. $\square$

The second moment criterion converts a variance computation into a lower bound on the probability that a random object has at least one of the desired configurations, and it is the standard tool of the threshold phenomena: when $\operatorname{Var}(X) = o(\mathbb{E}[X]^2)$ the count $X$ is concentrated near its mean, so almost surely $X>0$ whenever $\mathbb{E}[X]\to\infty$.

**Example (the number of triangles in a random graph).** Let $G(n,p)$ be the random graph with each edge present independently with probability $p$ and let $X$ be its number of triangles. Then $\mathbb{E}[X] = \binom{n}{3}p^3$ and a computation of the second moment shows $\operatorname{Var}(X) \leq Cn^4p^5 + Cn^3p^3$; hence for $p = \omega(n)/n$ the graph contains a triangle with probability tending to $1$, which is the lower half of the classical threshold at $p = 1/n$.

### The Paley Graph and the Quadratic Residues

**Example (Paley graphs).** Let $q \equiv 1 \pmod 4$ be a prime power and let the **Paley graph** on the field $\mathbb{F}_q$ join $x$ and $y$ when $x - y$ is a nonzero square. The graph is self-complementary and its clique number is of order $\log q$: the count of $k$-cliques is controlled by the Weil bound for the relevant character sums, which bounds the discrepancy of the edge count from the pseudorandom prediction, and the standard first and second moment computations applied to that prediction give the matching lower bound. The example shows the interaction of the method with the arithmetic articles: the input is a character sum, and the conclusion is a graph-theoretic bound.

## The Lovász Local Lemma

### The Statement

**Definition.** Let $\{A_i\}_{i\in I}$ be events in a probability space. A **dependency graph** for the family is a graph on $I$ such that $A_i$ is independent of the $\sigma$-algebra generated by all the $A_j$ with $j$ not adjacent to $i$ in the graph. Equivalently, $A_i$ is independent of the events $\{A_j : j \notin N(i)\cup\{i\}\}$.

**Theorem (Lovász local lemma; symmetric form).** Let $\{A_1,\dots,A_n\}$ be events with $\mathbb{P}(A_i) \leq p$ for every $i$, admitting a dependency graph in which every vertex has degree at most $d$. If

$$
ep(d + 1) \leq 1,
$$

then $\mathbb{P}(\bigcap_i A_i^c) > 0$.

*Proof (sketch).* One shows, by induction on $|S|$, that

$$
\mathbb{P}\!\left(A_i \bigm\mid \bigcap_{j\in S}A_j^c\right) \leq x_i
$$

for every $i$ and every $S$ disjoint from $N(i)\cup\{i\}$. The induction splits $S$ into $S_1 = S\cap N(i)$ and $S_2 = S\setminus N(i)$: the events indexed by $S_2$ are independent of $A_i$ and drop out of the conditional probability, while the events indexed by $S_1$ are estimated by the induction hypothesis and the product in the hypothesis. Then

$$
\mathbb{P}\!\left(\bigcap_iA_i^c\right) = \prod_i\left(1 - \mathbb{P}\!\left(A_i\bigm\mid \bigcap_{j<i}A_j^c\right)\right) > 0,
$$

since every factor is at least $1-x_i > 0$; in the symmetric form one takes $x_i = 1/(d+1)$, for which $\prod_{j\in N(i)}(1-x_j) \geq (1-\frac1{d+1})^d$, and $ep(d+1)\leq1$ makes the product inequality hold. $\square$

**Theorem (general form).** If there exist $x_i \in [0,1)$ with

$$
\mathbb{P}(A_i) \leq x_i\prod_{j \in N(i)}(1 - x_j) \qquad \text{for every } i,
$$

then $\mathbb{P}(\bigcap_iA_i^c) > 0$; the symmetric form is the case $x_i = 1/(d+1)$.

The local lemma is the union bound with the intersections controlled: the union bound requires the sum of the probabilities to be below one, whereas the local lemma requires only that each event be unlikely relative to the number of events on which it depends. This relaxation is what makes the lemma powerful, and its proof is the standard induction on the number of conditioned events.

### Applications

**Theorem (LLL for hypergraph colouring).** Every $k$-uniform hypergraph in which every edge intersects at most $d$ other edges is 2-colourable with no monochromatic edge, provided $e\,2^{1-k}(d+1) \leq 1$.

*Proof.* Colour independently; let $A_E$ be the event that the edge $E$ is monochromatic, so $\mathbb{P}(A_E) = 2^{1-k}$, and the dependency graph joins two edges that intersect. The degree is at most $d$ by hypothesis and the symmetric local lemma applies. $\square$

The result is strictly stronger than the first moment bound on the number of edges, since the count of edges through a vertex can be large. The other standard applications are the satisfiability of a $k$-CNF formula in which each clause shares a variable with at most $2^{k-1}/e - 1$ other clauses, and the existence of Ramsey lower bounds with the alteration step, where the local lemma sharpens the constant.

## The Alteration Method

### Graphs of Large Girth and Large Chromatic Number

**Theorem (Erdős).** For every $g \geq 3$ and every $\chi \geq 3$ there is a graph of girth greater than $g$ and chromatic number greater than $\chi$.

*Proof (sketch).* Let $G = G(n,p)$ with $p = n^{\theta-1}$ for a fixed $\theta \in (0,1)$. The expected number of cycles of length at most $g$ is $O(n^{\theta g})$ and the expected number of independent sets of size $s = \lceil 3\ln n/p\rceil$ is $o(1)$; more precisely, a first moment estimate bounds the probability that some $s$-set is independent by
$\binom{n}{s}(1-p)^{\binom{s}{2}} \leq (ne^{-p(s-1)/2})^s = o(1)$.
Alter the graph by deleting one vertex from each short cycle: the graph that remains has girth exceeding $g$ and its chromatic number is at least $n/(2s)$ — because every colour class is an independent set of size at most $s$, and at most $n/(2s)$ vertices were deleted when $n$ is large — which exceeds $\chi$ for $n$ large. $\square$

The alteration method is the second of the classical techniques: one first produces a random object with few defects, then repairs the defects by discarding them, and shows that the repair costs little relative to the size of the object. It is the technique behind the construction of graphs of large girth and large chromatic number, the Ramsey lower bound $\frac{k}{e\sqrt2}2^{k/2}$ of Spencer, and many of the constructions of extremal combinatorics.

## The Entropy and Container Methods

### The Entropy Method

**Theorem (Shearer's inequality; Kahn).** Let $X = (X_1,\dots,X_n)$ be a random vector with values in a finite product and, for a family $\mathcal{F}$ of subsets of $\{1,\dots,n\}$ covering every coordinate, let $X_F$ be the restriction to $F$. Then

$$
H(X) \leq \sum_{F\in\mathcal{F}}H(X_F),
$$

where $H$ is the Shannon entropy. In particular the number of independent sets of a graph can be bounded by the entropy of a random independent set conditioned on its restriction to the vertices of higher degree, and the bound is asymptotically sharp for regular graphs.

The entropy method replaces the union bound by an entropy inequality, and it is the quantitative refinement of the first moment method: the logarithm of the number of configurations is bounded by the sum of the entropies of the local restrictions, and the local entropies are computed from the degrees. For a graph on $n$ vertices with maximum degree $d$, applying the inequality to the covering family of the closed neighbourhoods of the vertices bounds the number of independent sets by $2^{n(1+o(1))\log_2(d+1)/d}$; the method was introduced by Kahn to determine the asymptotic number of independent sets and proper colourings of a graph, and it is the discrete form of the counting arguments of statistical mechanics.

### The Container Method

**Theorem (containers; Balogh–Morris–Samotij, Saxton–Thomason).** Let $H$ be a $k$-uniform hypergraph on $n$ vertices in which every set of $d$ vertices lies in at most $\ell$ edges. Then there is a family $\mathcal{C}$ of at most $\binom{n}{\leq t}$ sets such that every independent set of $H$ is contained in some $C\in\mathcal{C}$ and each $C$ has at most $Cn^{1-1/(k-1)}$ edges, where $t$ and $C$ depend on $k, d, \ell$.

The container theorem packages the entropy method into a structural statement: the independent sets of a sparse hypergraph are contained in a small family of "containers" each of which is very sparse. It is the tool behind the recent determinations of the number of $k$-free graphs, the asymptotics of the Ramsey numbers on bounded-degree host graphs, and the counting of the combinatorial structures of *Combinatorial Group Theory*; the proof iterates the hypergraph removal of the vertices of high degree and uses the entropy inequality of the previous theorem at each step.

## Concentration Inequalities

The method also requires quantitative bounds on the deviation of a random variable from its mean, and the standard inequalities are the following; the martingale case is the Azuma–Hoeffding inequality of *Martingales*.

**Theorem (Chernoff bounds).** Let $X_1,\dots,X_n$ be independent Bernoulli$(p)$ variables and $S = \sum_iX_i$, $\mu = np$. Then for $0 < \delta < 1$,

$$
\mathbb{P}(S \geq (1+\delta)\mu) \leq \exp\!\left(-\frac{\delta^2\mu}{3}\right), \qquad \mathbb{P}(S \leq (1-\delta)\mu) \leq \exp\!\left(-\frac{\delta^2\mu}{2}\right).
$$

**Theorem (Hoeffding).** Let $X_1,\dots,X_n$ be independent with $a_i \leq X_i \leq b_i$ and let $S = \sum_iX_i$. Then

$$
\mathbb{P}(S - \mathbb{E}[S] \geq t) \leq \exp\!\left(-\frac{2t^2}{\sum_i(b_i-a_i)^2}\right).
$$

**Theorem (Azuma–Hoeffding).** Let $\{M_n\}$ be a martingale with $|M_k - M_{k-1}| \leq c_k$ a.s. Then

$$
\mathbb{P}(|M_n - M_0| \geq t) \leq 2\exp\!\left(-\frac{t^2}{2\sum_{k\leq n}c_k^2}\right).
$$

**Theorem (McDiarmid; bounded differences).** Let $X_1,\dots,X_n$ be independent and let $f$ satisfy the bounded-difference condition $|f(x) - f(x')| \leq c_i$ whenever $x, x'$ differ only in the $i$-th coordinate. Then

$$
\mathbb{P}(f(X) - \mathbb{E}[f(X)] \geq t) \leq \exp\!\left(-\frac{2t^2}{\sum_ic_i^2}\right).
$$

The four inequalities are the standard concentration tools, and they are proved by the exponential moment method of *Measure-Theoretic Probability*: the Chernoff bound by the Markov inequality and the computation of $\mathbb{E}[e^{\lambda S}]$; Hoeffding by the lemma that a bounded centred variable has a subgaussian moment generating function; Azuma by the martingale version of the same computation, using the conditional expectation; and McDiarmid by exposing the coordinates one at a time and applying Azuma to the resulting martingale. The last two are the form in which the method applies to a function of many independent variables, and they are the reason the probabilistic method yields not only existence but also the typical behaviour of the objects.

## Summary

The probabilistic method proves existence by probability: a random object is chosen, the expected number of defects is computed, and if the expectation is below one then a defect-free object exists. The first moment method and the union bound are the first tools, with Erdős's lower bound $R(k,k) > 2^{k/2}$ for the Ramsey numbers as the classical application and the 2-colourability of a $k$-uniform hypergraph with fewer than $2^{k-1}$ edges as the elementary one. The second moment method turns a variance computation into a lower bound on the probability of the existence of a configuration, $\mathbb{P}(X=0)\leq\operatorname{Var}(X)/\mathbb{E}[X]^2$, and it is the tool of the threshold phenomena and of the pseudorandom constructions such as the Paley graphs.

The Lovász local lemma replaces the global union bound by a local condition: if every event has probability at most $p$ and depends on at most $d$ others, then $ep(d+1)\leq1$ implies that no event occurs with positive probability, and the general form replaces the constants by a system of inequalities. The alteration method produces a random object, repairs its defects by deletion, and shows that the repair is cheap relative to the object; it is the technique behind Erdős's construction of graphs of large girth and large chromatic number and behind the sharpened Ramsey lower bounds. The entropy method bounds the logarithm of the number of configurations by the sum of the local entropies, and the container method packages the entropy method into the statement that the independent sets of a sparse hypergraph are covered by a small family of sparse containers; both are used in the recent counting results of extremal combinatorics and of *Combinatorial Group Theory*.

The method is completed by the concentration inequalities — Chernoff, Hoeffding, the martingale Azuma–Hoeffding inequality of *Martingales*, and the bounded-difference inequality of McDiarmid — which are proved by the exponential moment method and which convert an expectation estimate into a statement about the typical case. The number-theoretic applications of the same method and the random walks on groups whose generation properties are proved probabilistically lie outside this article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\Omega,\mathcal{F},\mathbb{P})$, $\mathbb{E}$ | Probability space and expectation, as in *Measure-Theoretic Probability* |
| union bound | $\mathbb{P}(\bigcup_iA_i)\le\sum_i\mathbb{P}(A_i)$ |
| first moment method | $\mathbb{E}[X]<1\Rightarrow\mathbb{P}(X=0)>0$ |
| second moment method | $\mathbb{P}(X=0)\le\operatorname{Var}(X)/\mathbb{E}[X]^2$ |
| $R(k,\ell)$ | Ramsey number |
| $A_S$, dependency graph | monochromatic clique event; graph encoding independence |
| LLL (general form) | $\{A_i\}$ with $\mathbb{P}(A_i)\le x_i\prod_{j\in N(i)}(1-x_j)$ |
| $k$-uniform hypergraph | every edge has $k$ vertices |
| alteration | delete one vertex per defective configuration |
| $H(X)$, $H(X_F)$ | Shannon entropy and local entropy |
| container theorem | small family of sparse sets covering all independent sets |
| Chernoff, Hoeffding, Azuma, McDiarmid | concentration inequalities |
| $G(n,p)$ | random graph with independent edges of probability $p$ |
| Paley graph | graph on $\mathbb{F}_q$ joining square differences |





## Further Reading

- Paul Erdős and Joel Spencer, *Probabilistic Methods in Combinatorics* (Academic Press, 1974), for the original systematic account of the method.
- Noga Alon and Joel H. Spencer, *The Probabilistic Method* (Wiley, 4th edition, 2016), for the first and second moment methods, the local lemma, the alteration method and the concentration inequalities.
- Paul Erdős, "Some remarks on the theory of graphs", *Bulletin of the American Mathematical Society* 53 (1947), 292–294, for the probabilistic lower bound for the Ramsey numbers.
- László Lovász, "Combinatorial problems and exercises" (North-Holland, 1979), and Paul Erdős and László Lovász, "Problems and results on 3-chromatic hypergraphs and some related questions", in *Infinite and Finite Sets* (North-Holland, 1975), 609–627, for the local lemma.
- Jeff Kahn, "An entropy approach to the hard-core model on bipartite graphs", *Combinatorics, Probability and Computing* 10 (2001), 219–237, for the entropy method.
- József Balogh, Robert Morris and Wojciech Samotij, "Independent sets in hypergraphs", *Journal of the American Mathematical Society* 28 (2015), 669–709, and David Saxton and Andrew Thomason, "Hypergraph containers", *Inventiones Mathematicae* 201 (2015), 925–992, for the container method.
- Herman Chernoff, "A measure of asymptotic efficiency for tests of a hypothesis based on the sum of observations", *Annals of Mathematical Statistics* 23 (1952), 493–507, and Wassily Hoeffding, "Probability inequalities for sums of bounded random variables", *Journal of the American Mathematical Society* 58 (1963), 13–30, for the concentration inequalities.
- Kazuoki Azuma, "Weighted sums of certain dependent random variables", *Tohoku Mathematical Journal* 19 (1967), 357–367, and Colin McDiarmid, "On the method of bounded differences", in *Surveys in Combinatorics* (Cambridge University Press, 1989), 148–188, for the martingale and bounded-difference inequalities.
- Joel Spencer, "Six standard deviations suffice", *Transactions of the American Mathematical Society* 289 (1985), 679–706, for the discrepancy bound obtained by the method.
