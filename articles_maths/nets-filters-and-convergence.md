
# __Nets, Filters and Convergence__

## Introduction

A sequence is a function on the natural numbers, and in a metric space sequences detect everything: the closure, the continuity and the compactness are all tested by the sequences. In a general topological space none of these statements survives — a point can lie in the closure of a set without being the limit of any sequence from it, and a map can preserve every sequential limit without being continuous. The failure is the failure of the index set: the convergence of a sequence is indexed by a countable *linearly* ordered set, while the neighbourhood filter of a point may need uncountably many sets with no countable cofinal family among them.

Two remedies are available, and they are equivalent. The first keeps the idea of an indexed family but replaces $\mathbb{N}$ by a **directed set**, an ordered set in which every two elements have an upper bound; the resulting family is a **net**, and every topological statement can be tested on nets. The second drops the indexing altogether and works with the **filter** of sets through which a family is eventually contained; convergence becomes the inclusion of the neighbourhood filter, and the two operations of passing to a cofinal piece and of passing to a larger filter are the same. This article develops both languages, proves the dictionary between them, and ends by describing the category of convergence spaces, in which convergence is the primitive datum and the open sets are derived from it.

The general theory of topological spaces, with its open sets, closures, products, quotients and the convergence used in passing, is that of the written article *Topological Spaces*; the metric case, where sequences do suffice, is that of *Metric, Uniform and Complete Spaces*. Nothing here uses a measure, an integral or a limit of analysis: the convergence treated is that of a net or a filter in a topology, and the only order-theoretic input is the existence of upper bounds in a directed set. The ultrafilters of the third section rest on the axiom of choice, stated where it occurs.

## Directed Sets and Nets

### Directed Sets

**Definition.** A **directed set** is a nonempty set $D$ with a relation $\leq$ that is reflexive and transitive, and such that every pair $\alpha, \beta \in D$ has an upper bound: there is $\gamma \in D$ with $\alpha \leq \gamma$ and $\beta \leq \gamma$. A subset $D' \subseteq D$ is **cofinal** if for every $\alpha \in D$ there is $\alpha' \in D'$ with $\alpha \leq \alpha'$.

A directed set need not be linearly ordered, and this is the whole point of the notion. The examples used below are the following.

**Example.** The natural numbers with their usual order are directed, and a directed set with a countable cofinal subset is **countably directed**. The finite subsets $\mathcal{P}_{\mathrm{fin}}(X)$ of a set $X$, ordered by inclusion, are directed since the union of two finite sets is finite, and they have no countable cofinal subset when $X$ is uncountable.

**Example.** The neighbourhoods $\mathcal{N}_x$ of a point of a topological space, ordered by **reverse inclusion**, are directed because $U \cap V$ is an upper bound; this directed set is countable exactly when the space is first countable at $x$. The product $D \times E$ of two directed sets, ordered coordinatewise, is directed, and it indexes the double nets of the next sections.

### Nets and their Convergence

**Definition.** A **net** in a set $X$ is a function $x : D \to X$ from a directed set $D$ into $X$. It is written $(x_\alpha)_{\alpha \in D}$, or $(x_\alpha)$ when the index set is clear, and its value at $\alpha$ is $x_\alpha$. A net indexed by $\mathbb{N}$ is a sequence, and a net indexed by $\mathcal{N}_x$ ordered by reverse inclusion is a **neighbourhood net** at $x$.

**Definition.** Let $(x_\alpha)_{\alpha \in D}$ be a net in a topological space $X$. It **converges to** $x \in X$, written $x_\alpha \to x$ or $\lim_\alpha x_\alpha = x$, if for every neighbourhood $U$ of $x$ there is $\alpha_0 \in D$ such that $x_\alpha \in U$ for every $\alpha \geq \alpha_0$:
$$
x_\alpha \to x \iff \forall\, U \in \mathcal{N}_x\ \ \exists\, \alpha_0 \in D\ \ \forall\, \alpha \geq \alpha_0 : \ x_\alpha \in U ,
$$
and one says that the net is **eventually** in $U$. A point $x$ is a **cluster point** of the net if for every neighbourhood $U$ of $x$ and every $\alpha_0 \in D$ there is $\alpha \geq \alpha_0$ with $x_\alpha \in U$:
$$
x \text{ is a cluster point of } (x_\alpha) \iff \forall\, U \in \mathcal{N}_x\ \ \forall\, \alpha_0 \in D\ \ \exists\, \alpha \geq \alpha_0 : \ x_\alpha \in U ,
$$
and one says that the net is **frequently** in $U$.

Convergence is tested on a neighbourhood base, by the definition of the neighbourhood filter: if $x_\alpha \to x$ and $\mathcal{N}_x$ is a neighbourhood base at $x$, it suffices to check eventual containment in the members of $\mathcal{N}_x$. When the topology is given by a metric, $x_\alpha \to x$ means that for every $\epsilon > 0$ there is $\alpha_0$ with $d(x_\alpha, x) < \epsilon$ for $\alpha \geq \alpha_0$, which is the usual definition for sequences written for a general index set.

**Proposition.** A net converges to $x$ if and only if every neighbourhood of $x$ contains a tail of the net. A point $x$ is a cluster point of the net if and only if every neighbourhood of $x$ meets every tail.

**Proof.** A tail is a set of the form $\{x_\alpha : \alpha \geq \alpha_0\}$; the first statement is the definition of eventual containment. For the second, the defining condition says that no neighbourhood $U$ and no $\alpha_0$ have $x_\alpha \notin U$ for all $\alpha \geq \alpha_0$, that is, $U$ meets the tail over $\alpha_0$. $\square$

**Example.** Every sequence in a metric space whose terms approach $x$ is a net converging to $x$; conversely a convergent net in a metric space need not be a sequence. Let $\psi$ assign to each finite set $F \subseteq \mathbb{R}$ the least integer not in $F$, a point outside $F$. The net $(\psi(F))$ over the directed set of finite subsets has no limit in $\mathbb{R}$: if $U$ is a bounded neighbourhood of a point and $F_0$ an index, then for any integer $N$ above $U$ the finite set $F = F_0 \cup \{\, k \in \mathbb{Z} : k \leq N \,\}$ has $\psi(F) > N$ and hence $\psi(F) \notin U$, so no tail is contained in $U$. Every integer $m$ is a cluster point, since $\psi(F) = m$ for the finite sets $F$ containing every integer below $m$ and not $m$, so the net is frequently in every neighbourhood of $m$; the non-integral points with a neighbourhood containing no integer are not cluster points. A net therefore separates the two notions that coincide for sequences in a metric space.

**Remark.** A net is a generalisation of a sequence and not of a convergent series; the directed set need not be countable and need not have a smallest element. The neighbourhood net of a point of a non-first-countable space is of this kind, and it is the net that witnesses the failure of sequential arguments.

### Subnets

A sequence passes to a subsequence by composing with a strictly increasing map $\mathbb{N} \to \mathbb{N}$; the corresponding notion for nets must allow the index set to change and must ensure that the new net runs to the end of the old one.

**Definition.** Let $(x_\alpha)_{\alpha \in D}$ be a net and let $(y_\beta)_{\beta \in E}$ be a net in the same set. Then $(y_\beta)$ is a **subnet** of $(x_\alpha)$ if there is a map $\varphi : E \to D$ with $y_\beta = x_{\varphi(\beta)}$ for all $\beta$, and $\varphi$ is **monotone and cofinal**: $\beta \leq \beta'$ implies $\varphi(\beta) \leq \varphi(\beta')$, and for every $\alpha \in D$ there is $\beta_0 \in E$ with $\alpha \leq \varphi(\beta)$ whenever $\beta \geq \beta_0$.

A subnet of a sequence indexed by a directed set $E$ need not be a sequence, and a sequence that is a subnet of a sequence is exactly a subsequence. The definitions of limit and cluster point are related by subnets in the expected way.

**Proposition.** If $x_\alpha \to x$ and $(y_\beta)$ is a subnet of $(x_\alpha)$, then $y_\beta \to x$. If $x$ is a cluster point of $(x_\alpha)$, there is a subnet of $(x_\alpha)$ converging to $x$.

**Proof.** Given a neighbourhood $U$ of $x$, choose $\alpha_0$ with $x_\alpha \in U$ for $\alpha \geq \alpha_0$ and then $\beta_0$ with $\varphi(\beta) \geq \alpha_0$ for $\beta \geq \beta_0$; then $y_\beta = x_{\varphi(\beta)} \in U$ for $\beta \geq \beta_0$. For the second statement let $E$ be the set of the pairs $(\alpha, U)$ with $\alpha \in D$, $U$ a neighbourhood of $x$ and $x_\alpha \in U$, ordered componentwise and directed by clusterhood: given $(\alpha, U)$ and $(\alpha', U')$ choose $\gamma \geq \alpha, \alpha'$ and $V \subseteq U \cap U'$, and a $\delta \geq \gamma$ with $x_\delta \in V$. The projection $(\alpha, U) \mapsto \alpha$ is monotone and cofinal, since $(\delta, X)$ lies above every prescribed index, and $y_{(\alpha,U)} = x_\alpha$ converges to $x$ because for a given $U$ and $\alpha_0$ one takes $\delta \geq \alpha_0$ with $x_\delta \in U$, and then $y_{(\alpha,V)} \in U$ for all $(\alpha, V) \geq (\delta, U)$. $\square$

**Corollary.** A net has a convergent subnet if and only if it has a cluster point: passing to a subnet is exactly the operation of selecting a piece of the net that accumulates at a prescribed point.

## Filters

### Filters and Filter Bases

**Definition.** A **filter** on a set $X$ is a nonempty family $\mathcal{F}$ of subsets of $X$ such that

**(F1)** $\emptyset \notin \mathcal{F}$;

**(F2)** if $A, B \in \mathcal{F}$ then $A \cap B \in \mathcal{F}$;

**(F3)** if $A \in \mathcal{F}$ and $A \subseteq B \subseteq X$ then $B \in \mathcal{F}$.

A family $\mathcal{B}$ of nonempty subsets of $X$ is a **filter base** if for all $A, B \in \mathcal{B}$ there is $C \in \mathcal{B}$ with $C \subseteq A \cap B$; the family of all supersets of members of $\mathcal{B}$ is then a filter, the filter **generated** by $\mathcal{B}$.

Every filter is a filter base, and a filter base generates its filter by (F3). The intersection of a nonempty family of filters is a filter, so the filters on $X$ form a complete lattice under inclusion; the filter generated by a family is the intersection of the filters containing it.

**Example (principal filters).** For a nonempty $A \subseteq X$ the family $\{B : A \subseteq B \subseteq X\}$ is a filter, the **principal filter** at $A$, generated by the one-element base $\{A\}$.

**Example (the Fréchet filter).** On an infinite set $X$ the family of **cofinite** subsets, those whose complement is finite, is a filter base and generates a filter containing no finite set; it is not principal. On a finite set the cofinite sets are all the nonempty sets and generate the principal filter at $X$.

**Example (the neighbourhood filter).** For $x \in X$ the family $\mathcal{N}_x$ of neighbourhoods of $x$ is a filter, the **neighbourhood filter**. Its members need not be open; the open neighbourhoods form a base for it, and if $X$ is first countable the filter has a countable base.

**Definition.** A filter $\mathcal{F}$ is **finer** than a filter $\mathcal{G}$, and $\mathcal{G}$ is **coarser** than $\mathcal{F}$, if $\mathcal{G} \subseteq \mathcal{F}$. Two filters are **comparable** if one is finer than the other. The lattice of filters on $X$ has a largest element, the filter of all nonempty subsets of $X$, and its finest principal members are the filters $\dot x = \{\, A \subseteq X : x \in A \,\}$ at the points $x \in X$, each of them an ultrafilter and called the **principal ultrafilter** at $x$.

A family of sets with the finite intersection property generates a filter, by (F2); the maximal filters under inclusion are the ultrafilters of the next section. Finer filters contain more sets and therefore give more information, which is why convergence will be tested by being finer than the neighbourhood filter.

### Convergence of Filters

**Definition.** Let $\mathcal{F}$ be a filter on a topological space $X$. It **converges to** $x \in X$, written $\mathcal{F} \to x$, if $\mathcal{N}_x \subseteq \mathcal{F}$, that is, if every neighbourhood of $x$ belongs to $\mathcal{F}$. A point $x$ is a **cluster point** of $\mathcal{F}$ if $x \in \overline{A}$ for every $A \in \mathcal{F}$, equivalently if every neighbourhood of $x$ meets every member of $\mathcal{F}$.

**Proposition.** A filter $\mathcal{F}$ converges to $x$ if and only if it is finer than the neighbourhood filter $\mathcal{N}_x$. A point $x$ is a cluster point of $\mathcal{F}$ if and only if the filter generated by $\{\,U \cap A : U \in \mathcal{N}_x,\ A \in \mathcal{F}\,\}$ is a filter, equivalently if there is a filter finer than both $\mathcal{N}_x$ and $\mathcal{F}$.

**Proof.** The first statement is the definition. For the second, $x$ is a cluster point exactly when no neighbourhood of $x$ is disjoint from a member of $\mathcal{F}$, which is the condition that the displayed family has no empty member and has the finite intersection property; that family is then a filter base generating a filter finer than both $\mathcal{N}_x$ and $\mathcal{F}$. Conversely a filter finer than both contains $U \cap A$ for all $U \in \mathcal{N}_x$, $A \in \mathcal{F}$, so none of these is empty. $\square$

**Example.** The neighbourhood filter $\mathcal{N}_x$ itself converges to $x$, and the filter of all nonempty subsets converges to every point, so a limit need not be unique. On $\mathbb{R}$ the Fréchet filter of the cofinite sets converges to no point, since a bounded open interval is a neighbourhood of a point and is not cofinite, so it is not a member of the filter; an ultrafilter finer than the Fréchet filter likewise converges to no point, because a convergent filter contains a bounded neighbourhood of its limit, the cofinite sets contain no bounded set, and an ultrafilter cannot contain two disjoint sets.

## Ultrafilters

### Definition and Existence

**Definition.** An **ultrafilter** on a set $X$ is a filter maximal under inclusion: the only filter finer than it is itself. An ultrafilter is **principal** if it is the principal filter at some $A \subseteq X$, and **free** otherwise.

**Theorem (ultrafilter lemma).** Every filter on a set $X$ is contained in an ultrafilter.

**Proof.** The family of filters finer than a given filter $\mathcal{F}$, ordered by inclusion, is nonempty and is closed under unions of chains: the union of a chain of filters satisfies (F1)–(F3), since a finite intersection of members of the union involves only finitely many filters of the chain and a chain is linearly ordered, so all members lie in the largest of them. By Zorn's lemma the family has a maximal element, which is an ultrafilter containing $\mathcal{F}$. $\square$

The proof uses the axiom of choice, and this is unavoidable: the existence of a free ultrafilter on $\mathbb{N}$ is not provable in set theory without it.

**Theorem.** A filter $\mathcal{U}$ is an ultrafilter if and only if for every $A \subseteq X$ exactly one of $A$ and $X \setminus A$ lies in $\mathcal{U}$. It is then an ultrafilter if and only if $A \cup B \in \mathcal{U}$ implies $A \in \mathcal{U}$ or $B \in \mathcal{U}$.

**Proof.** If $\mathcal{U}$ is an ultrafilter and $A \notin \mathcal{U}$, put $\mathcal{U}' = \{B : A \cup B \in \mathcal{U}\}$. Then $\mathcal{U}'$ is a filter finer than $\mathcal{U}$ — it is nonempty, $\emptyset \notin \mathcal{U}'$ because $A \notin \mathcal{U}$, and it is closed under the finite intersections and the supersets — so $\mathcal{U}' = \mathcal{U}$ by maximality, and $X \setminus A \in \mathcal{U}'$ because $A \cup (X \setminus A) = X \in \mathcal{U}$; hence $X \setminus A \in \mathcal{U}$. At least one of $A$ and $X \setminus A$ therefore lies in $\mathcal{U}$, and they cannot both, by (F1) and (F2). Conversely let a filter $\mathcal{U}$ decide every complementary pair and let $\mathcal{V} \supseteq \mathcal{U}$ contain $A$; if $A \notin \mathcal{U}$ then $X \setminus A \in \mathcal{U} \subseteq \mathcal{V}$ and $\emptyset = A \cap (X \setminus A) \in \mathcal{V}$, a contradiction, so $A \in \mathcal{U}$ and $\mathcal{U} = \mathcal{V}$. The characterisation by the unions follows from the complement form: if $A, B \notin \mathcal{U}$ then $X \setminus A, X \setminus B \in \mathcal{U}$, hence $X \setminus (A \cup B) \in \mathcal{U}$. $\square$

**Corollary.** On an infinite set there exist free ultrafilters: extend the Fréchet filter, which contains no finite set, to an ultrafilter. A principal ultrafilter is determined by its one-point generator, and the ultrafilters on a finite set are exactly the principal ones.

### Ultrafilters and Compactness

Ultrafilters are the tool that makes compactness algebraic: a space is compact when every ultrafilter converges, and the property is preserved by every product.

**Theorem.** A topological space $X$ is compact if and only if every ultrafilter on $X$ converges.

**Proof.** Suppose $X$ compact and let $\mathcal{U}$ be an ultrafilter with no limit. For each $x \in X$ there is a neighbourhood $U_x \notin \mathcal{U}$, hence $X \setminus U_x \in \mathcal{U}$ by the characterisation above. The sets $U_x$ cover $X$; by compactness finitely many cover, say $U_{x_1}, \ldots, U_{x_n}$. Then $\bigcap_i (X \setminus U_{x_i}) = \emptyset \in \mathcal{U}$, a contradiction. Conversely let $\mathcal{U}$ converge and let $\{F_i\}$ be a family of closed sets with the finite intersection property. Extend the filter they generate to an ultrafilter $\mathcal{V}$; by hypothesis $\mathcal{V} \to x$ for some $x$, and each $F_i \in \mathcal{V}$ is closed, so $x \in \overline{F_i} = F_i$ for every $i$ by the cluster-point criterion. Hence $\bigcap_i F_i \neq \emptyset$ and $X$ is compact by the finite intersection property. $\square$

**Theorem (Tychonoff, by ultrafilters).** An arbitrary product of compact spaces is compact.

**Proof.** Let $X = \prod_{i \in I} X_i$ with the $X_i$ compact and let $\mathcal{U}$ be an ultrafilter on $X$. The image $\pi_i(\mathcal{U}) = \{\,B \subseteq X_i : \pi_i^{-1}(B) \in \mathcal{U}\,\}$ is an ultrafilter on $X_i$, because the preimages preserve the boolean operations, so by compactness it converges to some $x_i \in X_i$; let $x = (x_i)_{i \in I}$. A basic neighbourhood $\prod_i V_i$ of $x$ has $V_i = X_i$ for all but finitely many $i$, and $\pi_i^{-1}(V_i) \in \mathcal{U}$ at each of the finitely many exceptional indices; these finitely many preimages, and with them their intersection $\prod_i V_i$, therefore lie in $\mathcal{U}$. Hence every basic neighbourhood of $x$ belongs to $\mathcal{U}$ and $\mathcal{U} \to x$; every ultrafilter on $X$ converges, so $X$ is compact. $\square$

**Remark.** The ultrafilter lemma and the Tychonoff theorem for the arbitrary products are equivalent over the axioms of set theory without the axiom of choice, and both are strictly weaker than it; this is the ultrafilter argument by which an inverse system of finite sets has a limit.

## The Dictionary between Nets and Filters

The two languages are not merely analogous; there is a bijective correspondence between the convergence data they carry. The translation is straightforward in one direction and requires the correct notion of subnet in the other.

### From a Net to a Filter

**Definition.** Let $(x_\alpha)_{\alpha \in D}$ be a net in $X$. The **tail filter** of the net is the filter generated by the filter base $\{\,T_\alpha : \alpha \in D\,\}$ of tails $T_\alpha = \{x_\beta : \beta \geq \alpha\}$.

**Proposition.** A net converges to $x$ if and only if its tail filter converges to $x$, and $x$ is a cluster point of the net if and only if it is a cluster point of its tail filter.

**Proof.** The net is eventually in a set $A$ exactly when some tail is contained in $A$, that is, exactly when $A$ belongs to the tail filter. Thus $x_\alpha \to x$ if and only if every neighbourhood of $x$ belongs to the tail filter $\mathcal{F}$, that is $\mathcal{N}_x \subseteq \mathcal{F}$. For the cluster statement, $x$ is a cluster point of the net exactly when every neighbourhood of $x$ meets every tail, and the tails generate $\mathcal{F}$, so this is exactly the condition that every neighbourhood of $x$ meets every member of $\mathcal{F}$. $\square$

**Proposition.** If $(y_\beta)$ is a subnet of $(x_\alpha)$, the tail filter of $(y_\beta)$ is finer than the tail filter of $(x_\alpha)$.

**Proof.** Given $\alpha$ choose $\beta_0$ with $\varphi(\beta) \geq \alpha$ for $\beta \geq \beta_0$; then the $\beta$-tail of $y$ is contained in the $\alpha$-tail of $x$, so every tail of $x$ lies in the tail filter of $y$, which is therefore finer. $\square$

### From a Filter to a Net

**Definition.** Let $\mathcal{F}$ be a filter on $X$. The **associated net** is the net indexed by the directed set

$$
D_{\mathcal{F}} = \{\,(a, A) : a \in A,\ A \in \mathcal{F}\,\}, \qquad (a, A) \leq (b, B) \iff A \supseteq B,
$$

and defined by $\xi_{(a,A)} = a$. It is directed because $\mathcal{F}$ is closed under finite intersections and nonempty.

**Proposition.** A filter $\mathcal{F}$ converges to $x$ if and only if its associated net converges to $x$, and $x$ is a cluster point of one exactly when it is a cluster point of the other.

**Proof.** If $\mathcal{F} \to x$ and $U$ is a neighbourhood of $x$, then $U \in \mathcal{F}$ and $\xi_{(a,A)} = a \in A \subseteq U$ whenever $A \subseteq U$, which holds for all $(a, A) \geq (a_0, U)$. Conversely if the associated net converges to $x$ and $U$ is a neighbourhood of $x$, there is $(a_0, A_0)$ with $\xi_{(a,A)} \in U$ for $(a,A) \geq (a_0, A_0)$. For every $b \in A_0$ the pair $(b, A_0)$ is above $(a_0, A_0)$, so $b = \xi_{(b,A_0)} \in U$; hence $A_0 \subseteq U$ and $U \in \mathcal{F}$, so $\mathcal{N}_x \subseteq \mathcal{F}$. The cluster statements are proved in the same way from the definition of "frequently" and the fact that the tails of the associated net are the members of $\mathcal{F}$. $\square$

**Theorem (the dictionary).** The two assignments are inverse to one another on the convergence data: for every filter $\mathcal{F}$ the tail filter of its associated net is $\mathcal{F}$, and for every net $(x_\alpha)$ with tail filter $\mathcal{F}$ the net associated to $\mathcal{F}$ is a subnet of $(x_\alpha)$ up to the choice of representatives. Consequently, for a topological space $X$, for a map $f : X \to Y$ and for a subset $A \subseteq X$, every statement expressed with nets has a translation expressed with filters and conversely, with limits and cluster points corresponding to limits and cluster points and passage to a finer filter corresponding to passage to a subnet.

**Proof.** Let $\mathcal{F}$ be a filter and let $\xi$ be its associated net. The tail over $(a_0, A_0)$ is $\{a \in A : A \subseteq A_0\} = A_0$, so the tails of $\xi$ are exactly the members of $\mathcal{F}$ and the tail filter is $\mathcal{F}$. Conversely let $(x_\alpha)$ be a net with tail filter $\mathcal{F}$; each $A \in \mathcal{F}$ contains a tail $T_{\alpha(A)}$ of the original net, and the assignment $A \mapsto \alpha(A)$ may be chosen monotone, since $A \supseteq A'$ allows $\alpha(A) \geq \alpha(A')$, and cofinal, since the members of $\mathcal{F}$ are cofinal in the directed set of the net. The net $(x_{\alpha(A)})$ is therefore a subnet of $(x_\alpha)$ whose tails are contained in the members of $\mathcal{F}$, and the limits and cluster points of $(x_\alpha)$ are those of $\mathcal{F}$ by the two propositions above, as are those of $\xi$, which has the tails $\mathcal{F}$ by the first part. $\square$

**Remark.** The translation explains why some statements are easier for nets and others for filters: compactness is a statement about ultrafilters, which decide every subset and need no limiting process, while the generation of the topologies is a statement about filters, whose operations are the boolean and the order operations.

## Convergence and Topological Properties

**Theorem.** Let $A \subseteq X$. Then
$$
x \in \overline{A} \iff x_\alpha \to x \text{ for some net } (x_\alpha) \text{ in } A \iff \mathcal{F} \to x \text{ for some filter } \mathcal{F} \text{ with } A \in \mathcal{F} .
$$

**Proof.** If $x \in \overline{A}$, the family $\{U \cap A : U \in \mathcal{N}_x\}$ has the finite intersection property and generates a filter containing $A$ and converging to $x$. If a net in $A$ converges to $x_1$, every neighbourhood of $x_1$ contains a point of $A$, so $x_1 \in \overline{A}$; the filter statement is the same finite-intersection argument. $\square$

**Theorem.** A map $f : X \to Y$ is continuous if and only if $x_\alpha \to x$ implies $f(x_\alpha) \to f(x)$ for every net in $X$, and if and only if $\mathcal{F} \to x$ implies $f(\mathcal{F}) \to f(x)$ for every filter, where $f(\mathcal{F})$ is the filter generated by $\{f(A) : A \in \mathcal{F}\}$.

**Proof.** Continuity gives the preservation of convergence. Conversely suppose every convergent net is preserved and let $x \in X$; if $f$ were not continuous at $x$ there would be a neighbourhood $V$ of $f(x)$ whose preimage is not a neighbourhood of $x$, so that $U \setminus f^{-1}(V) \neq \emptyset$ for every neighbourhood $U$ of $x$. Choosing $x_U$ in that set and indexing by $\mathcal{N}_x$ ordered by reverse inclusion gives a net $x_U \to x$ with $f(x_U) \notin V$, a contradiction; the filter version is the same argument. $\square$

**Corollary.** Let $X$ be first countable. Then $f$ is continuous if and only if it preserves limits of sequences, and $x \in \overline{A}$ if and only if some sequence in $A$ converges to $x$. In a general space the preservation of sequential limits is necessary for continuity but not sufficient.

**Proof.** A first countable point has a countable neighbourhood base, which can be taken decreasing, so the nets of the previous proofs can be replaced by sequences. For the failure in general, let $X$ carry the cocountable topology, whose open sets are the sets with countable complement, and let $Y$ be $\mathbb{R}$ with its usual topology; the identity $X \to Y$ carries every convergent sequence to a convergent sequence, since a sequence converging in the cocountable topology is eventually constant, but it is not continuous, because $(-1, 1)$ is open in $Y$ and its preimage has uncountable complement in $X$. $\square$

**Theorem.** $X$ is Hausdorff if and only if every net has at most one limit, and if and only if every filter has at most one limit. If every ultrafilter on $X$ has at most one limit, then $X$ is Hausdorff.

**Proof.** If $x \neq y$ are not separated, the sets $U \cap V$, with $U$ a neighbourhood of $x$ and $V$ one of $y$, form a filter base generating a filter that converges to both points; a net converges to the same points as its tail filter, which gives the net statement, and an ultrafilter finer than that filter converges to both points, which gives the last statement. $\square$

## Convergence Spaces

The dictionary of the last section suggests a change of viewpoint: take convergence as primitive and recover the topology from it. The category obtained contains the topological spaces as a full subcategory, is cartesian closed, and is the home of several constructions — the function spaces among them — that fail to be topological.

### Convergence Structures

**Definition.** A **convergence structure** on a set $X$ is an assignment to every $x \in X$ of a family $\Lambda(x)$ of filters on $X$, called the filters **converging to** $x$, written $\mathcal{F} \to x$, such that

**(C1)** the principal filter $\dot x$ at $x$ converges to $x$;

**(C2)** if $\mathcal{F} \to x$ and $\mathcal{F} \subseteq \mathcal{G}$, then $\mathcal{G} \to x$;

**(C3)** if $\mathcal{F} \to x$ and $\mathcal{G} \to x$, then $\mathcal{F} \cap \mathcal{G} \to x$.

A **convergence space** is a pair $(X, \Lambda)$. A map $f : X \to Y$ between convergence spaces is **continuous** if $\mathcal{F} \to x$ in $X$ implies $f(\mathcal{F}) \to f(x)$ in $Y$.

Axioms (C1)–(C3) say that $\Lambda(x)$ is upward closed and closed under the binary intersections; the intersection $\mathfrak{N}(x) = \bigcap \Lambda(x)$ of all the filters converging to $x$ is then itself a filter, and $\Lambda(x)$ consists of the filters finer than $\mathfrak{N}(x)$ exactly when $\mathfrak{N}(x) \in \Lambda(x)$.

**Definition.** A convergence structure is **pretopological** if for every $x$ the family $\Lambda(x)$ has a least member under inclusion, denoted $\mathcal{N}(x)$ and called the **neighbourhood filter**; then $\mathcal{F} \to x$ if and only if $\mathcal{N}(x) \subseteq \mathcal{F}$. It is **topological** if it is pretopological and the neighbourhood filters arise from a topology, that is

**(T)** for every $U \in \mathcal{N}(x)$ there is $V \in \mathcal{N}(x)$ with $V \subseteq U$ and $U \in \mathcal{N}(y)$ for every $y \in V$.

For a topological convergence structure the family of sets $U$ with $U \in \mathcal{N}(x)$ for every $x \in U$ is a topology on $X$, and the filters converging to $x$ are exactly the filters containing the neighbourhood filter of the topology. Conversely every topology determines a convergence structure, and the topology is recovered by (T). The two passages are inverse, so topological spaces are identified with the topological convergence structures.

### Initial and Final Structures

**Definition.** Let $(X, \Lambda)$ be a convergence space, $\{Y_i\}$ convergence spaces and $f_i : X \to Y_i$ maps. The **initial** structure on $X$ for the family is the coarsest making every $f_i$ continuous: $\mathcal{F} \to x$ if and only if $f_i(\mathcal{F}) \to f_i(x)$ for every $i$. Dually, for $g_i : Y_i \to X$, the **final** structure is the finest making every $g_i$ continuous: $\mathcal{F} \to x$ if and only if there are $i$, $y \in Y_i$ and $\mathcal{G} \to y$ in $Y_i$ with $x = g_i(y)$ and $g_i(\mathcal{G}) \subseteq \mathcal{F}$.

Initial and final structures exist and are unique, are the analogues of the subspace and product topologies and of the quotient topology, and supply the category with all limits and colimits: the product is the initial structure for the projections and the quotient is the final structure for the quotient map.

**Proposition.** The convergence spaces form a complete and cocomplete category, and the passage from a topological space to its convergence structure is a full embedding preserving limits and colimits.

**Proof.** The limits and the colimits are the initial and final structures on the underlying sets of the diagrams; the embedding is full by the identification of the continuous maps with the continuous maps of the convergence structures, and it preserves the limits and the colimits because the initial and final structures generated by the continuous maps of topological spaces are again topological, which is checked from (T). $\square$

### The Categorical Description

**Theorem (topological reflection).** The full subcategory of the topological convergence spaces is reflective and coreflective in the category of the convergence spaces: the embedding has a left and a right adjoint, both fixing the topological spaces.

The left adjoint is the **topological modification**, the topological structure generated by the same convergent filters, obtained by iterating the passage to the neighbourhood filters until (T) holds; the right adjoint is the **topological coreflection**, the finest topological structure coarser than the given one. A map out of a convergence space into a topological space is continuous exactly when its composite with the reflection is, and dually through the coreflection. The decisive categorical property is not shared with the topological spaces.

**Theorem.** The category of convergence spaces is cartesian closed, and the topological modification of the product of two topological spaces is their ordinary product. The category of topological spaces is not cartesian closed.

The internal hom is the set of the continuous maps with the **continuous convergence structure**: a filter $\mathcal{F}$ of maps converges to $f$ if for every $x \in X$ and every $\mathcal{G} \to x$ the filter generated by the sets $g(G)$ with $g \in F \in \mathcal{F}$, $G \in \mathcal{G}$ converges to $f(x)$. For the topological spaces this structure need not be topological, which is exactly the failure of the cartesian closure, repaired by the convergence spaces.

**Theorem (Manes, in outline).** The category of compact Hausdorff spaces and continuous maps is equivalent to the category of algebras for the **ultrafilter monad** $\beta$ on the category of sets, whose functor sends a set to the set of its ultrafilters; the algebras are the sets with a choice of limit for every ultrafilter subject to the axioms of a compact Hausdorff convergence structure, and the theorem is the cleanest statement that convergence, and not openness, is the primitive notion.

**Remark.** Restricting the convergence structures to the filters generated by the sequences gives the **sequential spaces**, a full subcategory of the topological spaces strictly containing the Fréchet–Urysohn spaces and strictly contained in the convergence spaces. The cocountable topology of the example above is not sequential: its convergent sequences are eventually constant, so every subset is sequentially closed, while its closed sets are the countable ones and the whole space.

## Summary

A **directed set** is an ordered set in which every two elements have an upper bound, and a **net** is a function on a directed set; it converges to $x$ when it is eventually in every neighbourhood of $x$, and $x$ is a cluster point when it is frequently in every neighbourhood. A **subnet** is obtained by a monotone cofinal reindexing; limits pass to subnets, and a net has a convergent subnet exactly when it has a cluster point. Nets test every topological property: $x \in \overline{A}$ exactly when some net in $A$ converges to $x$, and a map is continuous exactly when it preserves convergent nets.

A **filter** is an upward-closed family of nonempty sets closed under finite intersections; a **filter base** generates one, the **neighbourhood filter** is the canonical example, and a filter converges to $x$ when it contains the neighbourhood filter. **Ultrafilters** are the maximal filters; every filter is contained in one, by the axiom of choice, an ultrafilter contains exactly one of every complementary pair, and a space is compact exactly when every ultrafilter on it converges, which gives the ultrafilter proof of Tychonoff's theorem for arbitrary products. The **dictionary** between the two languages assigns to a net its tail filter and to a filter its associated net, and it matches limits, cluster points and passage to finer filters with passage to subnets.

Topological properties are read off both languages: Hausdorff means unique limits, compactness means every ultrafilter converges, and continuity means preservation of convergence. Taking convergence as primitive gives the category of **convergence spaces**, in which the topological spaces embed fully as the structures satisfying the neighbourhood axiom, initial and final structures give all limits and colimits, and the category is cartesian closed with the continuous convergence structure on function spaces — a property the category of topological spaces lacks. The category of compact Hausdorff spaces is recovered as the category of algebras for the ultrafilter monad, which is the precise sense in which these spaces are convergence structures rather than families of open sets.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X, Y$ | Topological or convergence spaces |
| $(D, \leq)$ | Directed set; $\alpha, \beta, \gamma$ its elements |
| $(x_\alpha)_{\alpha \in D}$, $x_\alpha \to x$ | Net and its convergence; eventually in every neighbourhood |
| Cluster point | Frequently in every neighbourhood; limits of subnets |
| $\varphi : E \to D$ | Monotone cofinal reindexing defining a subnet |
| $\mathcal{F}, \mathcal{G}$ | Filters on a set $X$ |
| $\mathcal{B}$ | Filter base |
| $\mathcal{N}_x$, $\mathcal{N}(x)$ | Neighbourhood filter at $x$ |
| $\mathcal{F} \to x$ | Filter convergence, $\mathcal{N}_x \subseteq \mathcal{F}$ |
| Finer, coarser | $\mathcal{G} \subseteq \mathcal{F}$; inclusion of filters |
| $\dot x$ | Principal ultrafilter at $x$ |
| $\mathcal{U}$ | An ultrafilter |
| $\beta X$ | Set of ultrafilters on $X$; the ultrafilter monad |
| $f(\mathcal{F})$ | Image filter generated by $\{f(A) : A \in \mathcal{F}\}$ |
| $T_\alpha$ | Tail $\{x_\beta : \beta \geq \alpha\}$ of a net |
| $\Lambda(x)$ | Filters converging to $x$; a convergence structure |
| $\mathfrak{N}(x)$ | Intersection of the filters converging to $x$ |
| $(C1)$–$(C3)$ | Axioms of a convergence structure |
| $(T)$ | Axiom making a pretopological structure topological |
| $\overline{A}$, $A^\circ$ | Closure and interior, as in *Topological Spaces* |
| $\prod_i X_i$, $\pi_i$ | Product and projections; the ultrafilter proof of Tychonoff |

## Further Reading

- John L. Kelley, *General Topology* (Van Nostrand, 1955; reprinted Springer, 1975), for nets as the primary convergence notion and the ultrafilter proof of Tychonoff's theorem.
- Nicolas Bourbaki, *General Topology*, Chapters 1–4 (Springer, 1995), for filters, ultrafilters and the filter-theoretic form of compactness.
- James R. Munkres, *Topology* (Prentice Hall, 2nd ed. 2000), for the elementary treatment of nets and filters alongside sequences.
- Stephen Willard, *General Topology* (Addison-Wesley, 1970; reprinted Dover, 2004), for subnets, the net–filter dictionary and the convergence of ultrafilters.
- Ryszard Engelking, *General Topology* (Heldermann, revised ed. 1989), for the systematic use of filters in compactness and product theorems.
- Ernst Binz, *Continuous Convergence on $C(X)$* (Springer Lecture Notes in Mathematics 469, 1975), for the continuous convergence structure and function spaces.
- D. C. Kent and W. K. Min, "A Uniform Approach to Convergence Spaces" (in *Convergence Structures and Applications*, Springer, 1980), for convergence structures and the categorical description.
- Ernest Manes, "Compact Hausdorff Objects", *General Topology and its Applications* 4 (1974), 341–360, for the ultrafilter monad and its algebras.
