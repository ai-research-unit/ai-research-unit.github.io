
# __Combinatorial Group Theory__

## Introduction

Combinatorial group theory studies groups through the words that present them: it asks which words represent the identity, how subgroups sit inside a free group, and how new groups are assembled from old ones by gluing along a common subgroup. The subject begins with the observation that a group given by generators and relations is a quotient of a free group by the normal closure of the relations, so that every question about the group is a question about words in the free group. Its first applications are the solution of the word problem in free groups by free reduction and the computation of the rank of a finite-index subgroup of a free group; its deepest negative result is the theorem of Novikov and Boone that the word problem is undecidable in general.

This article is the twelfth of the corpus and the third of the group articles, below the foundational layer, *Infinite Abelian Groups* and *Solvable and Nilpotent Groups*. It uses the elementary presentation theory of *Generators, Presentations and Free Products* — generating sets, presentations, free groups, free products, direct and semidirect products — and it does not restate it. What it adds is the word problem, Nielsen transformations, the Nielsen–Schreier theorem on subgroups of free groups, the Kurosh theorem on subgroups of free products, amalgamated products and HNN extensions with their normal forms, and the accessibility of finitely presented groups. It is purely algebraic: the Bass–Serre theory of groups acting on trees, which gives the geometric proofs of the Nielsen–Schreier and Kurosh theorems and the structure of amalgamated products, is dealt with in Part II, where a group can act on a topological space; only the algebraic forms of those theorems appear here.

The article is also the natural place for the negative results on decidability. The word problem for finitely presented groups is the first undecidable problem arising naturally in algebra, and it is the reason the combinatorial theory is a theory of algorithms as much as of groups.

## Free Groups and Reduced Words

### Normal Forms and the Word Problem for Free Groups

**Definition.** Let $F = F(X)$ be the free group on a set $X$, as constructed in *Generators, Presentations and Free Products*. A **word** in $X$ is a finite sequence $x_1^{\epsilon_1} \cdots x_n^{\epsilon_n}$ with $x_i \in X$ and $\epsilon_i \in \{\pm 1\}$; the word is **reduced** if it contains no adjacent pair $x x^{-1}$ or $x^{-1} x$, and the **length** $|w|$ is the number of letters. Free reduction deletes adjacent inverse pairs repeatedly.

**Theorem (normal form).** Every element of $F(X)$ is represented by exactly one reduced word.

**Proof sketch.** Existence: reducing a word by deleting adjacent inverse pairs terminates, because the length decreases, and the resulting word is reduced and equal to the original in $F(X)$, since $xx^{-1}$ is a relation of the free group. Uniqueness: the set of reduced words, with the product given by concatenation followed by reduction, is a group — associativity is verified by a case analysis on the cancellations at the two junctions of three words, the empty word is the identity, and each reduced word has the word with the letters reversed and their exponents negated as inverse. This group satisfies the universal property of the free group: a function $X \to G$ extends to a homomorphism by mapping a reduced word $x_1^{\epsilon_1}\cdots x_n^{\epsilon_n}$ to the product of the images in $G$, and the extension is well defined precisely because two reduced words representing the same element are the same word. Hence the reduced-word group is $F(X)$, and reduced words are unique representatives. $\square$

**Corollary (the word problem for free groups).** There is an algorithm that decides, for a word in the generators of a free group and their inverses, whether it represents the identity: reduce the word freely and test whether it is empty.

The word problem has a positive solution in every free group, and the algorithm is linear in the length of the word when implemented with a stack. The corollary is the base case of the theory; the general problem is stated in the next section.

### Nielsen Transformations

**Definition.** The **Nielsen transformations** of a finite tuple $(a_1, \ldots, a_n)$ of elements of a group are: replace $a_i$ by $a_i^{-1}$; replace $a_i$ by $a_i a_j$ with $i \neq j$; and interchange $a_i$ and $a_j$. A **Nielsen transformation** of a subgroup is the passage from one generating tuple to another by a finite sequence of these moves.

**Theorem (Nielsen).** In a free group, every two finite generating tuples of the same subgroup, both minimal in the sense of no generator being redundant, are related by Nielsen transformations, and the number of generators is an invariant, the rank of the subgroup.

**Proof sketch.** The proof introduces the length sum $\sum_i |a_i|$ and shows that a nontrivial tuple can be shortened by a Nielsen transformation unless the generators already can be read off a common "Nielsen reduced" form, in which case they are automatically independent. The inductive argument on the length sum shows that primitive tuples — those that are generating and as short as possible — are retrievable by Nielsen moves, and the technical heart is the **Nielsen reduction**: a tuple is Nielsen reduced if no cancellation occurs on more than half of any generator when it is multiplied by the others, and a Nielsen reduced tuple freely generates the subgroup it generates. $\square$

The theorem is the free-group form of the division algorithm of $\mathbb{Z}$: within a free group, the reduction of a generating tuple by Nielsen transformations is the analogue of reducing a generating set of a subgroup of $\mathbb{Z}$, and it computes the rank.

## Presentations and the Word Problem

### Presentations

A **presentation** $\langle X \mid R \rangle$ consists of a set $X$ of generators and a set $R$ of relators, and it presents the group $F(X)/N(R)$, where $N(R)$ is the normal closure of $R$ in the free group on $X$. A group is **finitely generated** if it has a presentation with finite $X$, and **finitely presented** if it has a presentation with $X$ and $R$ both finite. These notions, the universal property of a presentation, Tietze transformations and the elementary examples are in *Generators, Presentations and Free Products*; the present article assumes them.

**Example.** The free abelian group of rank $n$ has the presentation $\langle x_1,\ldots,x_n \mid x_ix_jx_i^{-1}x_j^{-1}\ (i<j)\rangle$. The dihedral group of order $2n$ has the presentation $\langle r,s \mid r^n,\ s^2,\ srsr\rangle$ of *Solvable and Nilpotent Groups*. The Baumslag–Solitar group $BS(1,2)$ is $\langle a,t \mid tat^{-1}a^{-2}\rangle$.

### The Word Problem

**Definition.** The **word problem** for a finite presentation $\langle X \mid R\rangle$ is the following decision problem: given a word $w$ in $X \cup X^{-1}$, decide whether $w$ represents the identity in the presented group. The **conjugacy problem** asks whether two words represent conjugate elements, and the **isomorphism problem** asks whether two presentations present isomorphic groups.

**Theorem (Novikov–Boone).** There is a finitely presented group whose word problem is undecidable. More precisely, there is a finite presentation for which no algorithm decides, on all input words, whether the word represents the identity.

**Remark.** The theorem says that the class of finitely presented groups does not admit a uniform solution of the word problem, not that the word problem is undecidable for every finitely presented group. Many classes admit a solution: free groups by the normal form theorem above, free products by the normal form of the next sections, finitely generated nilpotent groups by the collection process, and small cancellation groups by Dehn's algorithm below. The undecidability is a consequence of the undecidability of the halting problem established in *Formal Logic and Computability*: one encodes the configurations of a Turing machine in words over the generators of a presentation so that the machine halts if and only if a fixed word represents the identity.

### Dehn's Algorithm and Small Cancellation

**Definition.** A presentation $\langle X \mid R\rangle$ is a **Dehn presentation** if every relator is cyclically reduced, no relator is a proper power, and every reduced word $w$ representing the identity contains more than half of some relator as a subword. For such a presentation there is a **Dehn algorithm**: given a reduced word $w$, replace any subword that is more than half of a relator by the shorter word obtained by cancelling, and repeat; if $w$ reduces to the empty word then $w$ is trivial in the group.

**Theorem (Dehn).** In a group with a Dehn presentation, the word problem and the conjugacy problem are solvable, and every nontrivial element of the group has infinite order; in particular the group is torsion-free.

**Proof sketch.** If $w$ is a reduced word representing the identity and $w$ is nontrivial, then by the hypothesis the relator structure forces a subword longer than half of some relator to appear; cancelling it produces a shorter word still representing the identity. Iterating, every nonempty reduced word representing the identity would give an infinite descent in length, which is impossible; hence the empty word is the only reduced representative of the identity and the Dehn algorithm decides the word problem. The conjugacy problem is solved by a refinement of the same argument, in which one cyclically reduces the two words and applies the cancellation criterion to the cyclic words of equal length. $\square$

**Definition.** A reduced word is a **piece** of a presentation $\langle X \mid R\rangle$ if it occurs as a common initial segment of two distinct relators of $R$, or of two distinct occurrences of the same relator, in both cases as a proper part. The presentation satisfies the **small cancellation condition** $C'(p)$ if every piece has length less than $1/p$ of the length of every relator in which it occurs as an initial segment. The **small cancellation** theory studies the presentations satisfying $C'(1/6)$, or $C'(1/4)$ in the presence of further hypotheses on the relators (for instance, that no relator is a proper power); in these presentations Dehn's algorithm applies, so the word problem is solvable.

**Theorem (Lyndon–Schupp, small cancellation).** If a finite presentation satisfies $C'(1/6)$, then its group has a Dehn presentation and hence a solvable word problem; the same conclusion holds for $C'(1/4)$ presentations satisfying the additional hypotheses on the relators given in the standard sources.

The small cancellation conditions are the standard combinatorial method for producing presentations on which Dehn's algorithm can be run, and they are the combinatorial substitute for the geometric methods of Part II.

## The Nielsen–Schreier Theorem

### Subgroups of Free Groups

**Theorem (Nielsen–Schreier).** Every subgroup of a free group is free.

**Proof via Schreier transversals.** Let $F = F(X)$ be free on $X$ and let $H \leq F$. Choose a set $T$ of right coset representatives of $H$ in $F$ — one element per right coset — with the **Schreier property** that every initial segment of the reduced word of a representative is again a representative, and $1 \in T$. Such a **Schreier transversal** is obtained by choosing, for each coset, the representative of least length with a fixed tie-breaking rule, which has the Schreier property. For $t \in T$ and $x \in X \cup X^{-1}$, the element $tx$ lies in some right coset, whose representative is $\bar{tx} \in T$, and the **Schreier generator**

$$
s(t,x) = t x\, \overline{tx}^{-1}
$$

lies in $H$. The Schreier generators generate $H$, and they form a free basis: the reduced form of every element of $H$ can be read from the tree of representatives, in which cancellations are controlled by the Schreier property, so that no nontrivial product of Schreier generators reduces to the identity. Hence $H$ is free with the Schreier generators as a basis. $\square$

The proof is the algebraic core of the theorem; its geometric form, in which $H$ acts on the Cayley graph of $(F,X)$ and the quotient graph realises the free basis, belongs to Part II. The rank of the subgroup is $1 - |T| + \sum_{x} |T|$ run over the generators and their inverses with the tree of representatives; when $H$ has finite index this gives the rank formula below.

### The Rank Formula

**Theorem (Schreier index formula).** Let $F_n$ be free of rank $n$ and let $H \leq F_n$ have finite index $k$. Then

$$
\operatorname{rk}(H) = k(n - 1) + 1 = 1 + k(n-1).
$$

**Proof.** Let $T$ be a Schreier transversal with $|T| = k$. The **Schreier graph** $\Gamma$ has the $k$ cosets as vertices, and for each coset $Hg$ and each generator $x \in X$ an undirected edge joining $Hg$ to $Hgx$; thus $\Gamma$ has $k$ vertices and $nk$ edges, and it is connected because $F_n$ permutes the cosets transitively by right multiplication. A spanning tree of $\Gamma$ has $k-1$ edges, and the subgroup $H$ is the fundamental group of $\Gamma$, free of rank

$$
\operatorname{rk}(H) = nk - (k - 1) = k(n-1) + 1.
$$

The verification accompanying this article confirms the formula on the kernels of $F_2 \to \mathbb{Z}/2$, $F_2 \to \mathbb{Z}/3$ and $F_3 \to \mathbb{Z}/2$, where the kernel has index $2$, $3$ and $2$ and rank $3$, $4$ and $5$ respectively. $\square$

**Corollary.** A free group of rank $n \geq 2$ contains free subgroups of every finite rank $\geq 2$ and free subgroups of countably infinite rank, and a subgroup of finite index $k$ in $F_n$ has rank at least $2$ unless $n = k = 1$.

**Example.** The commutator subgroup of $F_n$ has infinite index for $n \geq 2$, and the kernel of the map $F_n \to \mathbb{Z}/m$ sending every generator to $1$ is free of rank $1 + m(n-1)$. The kernel of $F_2 \to \mathbb{Z}/2$, $a \mapsto 1$, $b \mapsto 1$, is freely generated by $a^2$, $ab$, $b^2$; the verification for this article constructs the Schreier graph and checks the rank.

### Grushko's Theorem

**Theorem (Grushko).** If $G = A * B$, then $\operatorname{rk}(G) = \operatorname{rk}(A) + \operatorname{rk}(B)$, where the rank is the minimal number of generators.

**Proof sketch.** The inequality $\operatorname{rk}(G) \leq \operatorname{rk}(A) + \operatorname{rk}(B)$ is trivial. For the converse one takes a minimal generating tuple of $G$ and decomposes it: Grushko's theorem states that a generating set of a free product can be Nielsen transformed into a disjoint union of generating sets of the factors, so the rank is additive. The argument is the natural extension of the Nielsen reduction of the previous section to free products, and it is the reason the rank is an additive invariant under free products. $\square$

## The Kurosh Subgroup Theorem

**Theorem (Kurosh).** Let $G = *_{i \in I} A_i$ be a free product of groups. Every subgroup $H \leq G$ decomposes as a free product

$$
H = F * \Big( *_{i \in I} *_{j \in J_i} H_{ij} \Big),
$$

where $F$ is a free group, and for each $i$ the groups $H_{ij}$ are conjugates of subgroups of $A_i$ in $G$. If $H$ has finite index in $G$ and the index set $I$ and the factors are finite, then $F$ has finite rank and the $J_i$ are finite.

**Proof sketch.** One chooses a Schreier transversal for $H$ exactly as in the Nielsen–Schreier theorem and forms the Schreier graph, whose vertices are the cosets and whose edges carry labels in the free factors. The graph is a tree of graphs glued along vertices, one piece for each $A_i$; the subgroup $H$ is the fundamental group of the quotient graph, and a graph that is a tree of one-vertex-with-loops components has fundamental group the free product of the fundamental groups of the components and a free group for the excess edges. Reading off the components gives the factors $H_{ij}$ as conjugates of subgroups of the $A_i$, and the excess edges give the free factor $F$. $\square$

The Kurosh theorem specialises to Nielsen–Schreier when the free product has a single trivial factor, that is, when $G$ is free; it is the general statement that the subgroup structure of a free product is as simple as that of a free group, with the free factors contributing trapped subgroups. The geometric proof, in which one lets $H$ act on the Bass–Serre tree of the free product, is Part II's, and the algebraic proof above uses only the algebraic form of the tree.

## HNN Extensions and Amalgamated Products

### Amalgamated Free Products

**Definition.** Let $A$ and $B$ be groups with a common subgroup $C$, and let the **amalgamated free product** be

$$
A *_C B = (A * B)/N,
$$

where $N$ is the normal closure of the set $\{c\,\phi(c)^{-1} : c \in C\}$ for the two embeddings of $C$ into $A$ and $B$. It is characterised by the universal property that homomorphisms $A *_C B \to G$ correspond to pairs of homomorphisms $A \to G$ and $B \to G$ agreeing on $C$.

**Theorem (normal form).** Every element of $A *_C B$ has a unique reduced form: a sequence $a_1 b_1 a_2 b_2 \cdots$ or $b_1 a_1 b_2 \cdots$ with the $a_i \in A \setminus C$, $b_i \in B \setminus C$ alternating and nonempty, together with a possible single element of $C$ at one end.

**Proof sketch.** One defines a left action of $A *_C B$ on the set of normal forms by multiplication with reduction, and checks the action is well defined: the relations of the presentation act trivially, so the action descends to the quotient, and the resulting permutation representation is faithful on normal forms. This is the algebraic form of the Bass–Serre tree of the amalgamated product, on which the group acts with fundamental domain a segment. $\square$

### HNN Extensions

**Definition.** Let $G$ be a group and let $\alpha : A \to B$ be an isomorphism between subgroups of $G$. The **HNN extension** of $G$ with respect to $\alpha$ is

$$
G*_\alpha = \langle G, t \mid t a t^{-1} = \alpha(a) \text{ for } a \in A\rangle,
$$

where $t$ is a new generator, the **stable letter**. The subgroup $G$ is the **base**, and $A$ and $B$ are the **associated subgroups**.

**Theorem (Britton's lemma and normal form).** Every element of $G*_\alpha$ has a unique **normal form**

$$
g_0\, t^{\epsilon_1} g_1\, t^{\epsilon_2} \cdots t^{\epsilon_n} g_n,
$$

where $g_0 \in G$, $\epsilon_i = \pm 1$, $g_i \in G$ for $i < n$, and no subword $t^{-1} g_i t$ with $g_i \in A$ or $t g_i t^{-1}$ with $g_i \in B$ occurs. In particular the base $G$ embeds in $G*_\alpha$, and an element is trivial if and only if its normal form reduces to the empty word by the applications of the relations $t a t^{-1} = \alpha(a)$ and $t^{-1} b t = \alpha^{-1}(b)$.

**Proof sketch.** As in the amalgamated case, one defines $G*_\alpha$ as a group of normal forms and lets it act on itself by left multiplication; the rewriting of a product into normal form is confluent, because the only possible rewritings involve the associated subgroups and the isomorphism identifications are consistent. Britton's lemma is the statement that this rewriting system terminates in a unique normal form, and its contrapositive gives the embedding of $G$. $\square$

Britton's lemma is the source of the classical examples: it allows one to prove that a group embeds in an HNN extension, that an element has infinite order, and that finite presentations of interest have a solvable or unsolvable word problem according to the base.

### The Baumslag–Solitar Groups

**Definition.** For integers $m, n \geq 1$, the **Baumslag–Solitar group** is

$$
BS(m,n) = \langle a, t \mid t a^m t^{-1} = a^n\rangle.
$$

It is the HNN extension of $\mathbb{Z} = \langle a\rangle$ with associated subgroups $m\mathbb{Z}$ and $n\mathbb{Z}$ and the isomorphism $a^m \mapsto a^n$.

**Proposition.** In $BS(1,n)$ one has $t^k a t^{-k} = a^{n^k}$ for all $k \in \mathbb{Z}$; the group is isomorphic to a semidirect product $\mathbb{Z}[1/n] \rtimes \mathbb{Z}$, in which $a$ acts as $1$ and $t$ acts as multiplication by $n$. The verification for this article confirms $t^k a t^{-k} = a^{n^k}$ and the relation $t a t^{-1} = a^2$ in $BS(1,2)$ by explicit computation in that semidirect product.

**Proposition.** $BS(1,1) \cong \mathbb{Z}^2$; $BS(1,n)$ for $n \geq 2$ is torsion-free and solvable of derived length $2$; $BS(m,n)$ with $m, n \geq 2$ and $m \neq n$ contains free subgroups of rank $2$ and hence is not solvable; and $BS(2,3)$ is the standard example of a finitely presented group that is not hopfian.

**Proof sketch.** $BS(1,1)$ is $\langle a, t \mid tat^{-1} = a\rangle$, which is free abelian of rank $2$. For $n \geq 2$, $BS(1,n)$ is the semidirect product $\mathbb{Z}[1/n] \rtimes \mathbb{Z}$ described above, whose derived subgroup is the abelian group $\mathbb{Z}[1/n]$; the group is torsion-free because $\mathbb{Z}[1/n]$ is. For $m,n \geq 2$ with $m \neq n$, the subgroup generated by suitable conjugates of $a$ and of $t$ is free of rank $2$ by the standard ping-pong argument on the Bass–Serre tree of the HNN extension, and a solvable group contains no free subgroup of rank $2$; the details are in the standard literature. For $BS(2,3)$ the endomorphism $a \mapsto a^2$, $t \mapsto t$ is well defined, since it carries the relation $ta^2t^{-1} = a^3$ to $ta^4t^{-1} = a^6$; it is surjective, because its image contains $ta^2t^{-1}a^{-2} = a$; and it is not injective, because it kills a nontrivial element of the form $[tat^{-1}, a]$. $\square$

The family $BS(m,n)$ is the standard testing ground for the combinatorial theory: it shows that a one-relator group need not be hopfian nor residually finite, although its word problem is solvable, by Magnus's theorem that every one-relator group has a solvable word problem. The group $BS(2,3)$ is also the standard example of an HNN extension whose associated subgroups are proper and which is not residually finite.

## Accessibility and Finite Presentability

### Finitely Presented Subgroups

**Definition.** A group is **coherent** if every finitely generated subgroup is finitely presented. A group is **accessible** if every chain of finitely generated subgroups, each of infinite index in the next, is finite.

**Theorem (Higman).** A finitely presented group has a finitely presented subgroup that is not free, and every recursively presented group embeds in a finitely presented group.

**Proof sketch.** Higman's theorem constructs, from a recursive presentation, a finite presentation containing it by encoding the enumerating machine in generators and relations, in the same spirit as the Novikov–Boone construction. $\square$

**Theorem (accessibility of finitely presented groups).** Every finitely presented group is accessible; consequently a finitely presented group has a decomposition as a graph of groups with finite edge groups in which the vertex groups have no nontrivial decomposition, and this decomposition is unique up to the natural operations.

**Proof sketch.** The proof proceeds by induction on the presentation, using the fact that a finitely generated group that splits over a finite group has a bound on the length of any chain of such splittings, and interpreting the failure of accessibility as an infinite sequence of splittings whose existence contradicts finite presentability. The uniqueness statement is the algebraic form of the uniqueness of the graph-of-groups decomposition, whose geometric proof is Part II's. $\square$

**Definition.** A group $G$ is **residually finite** if for every nonidentity $g \in G$ there is a finite quotient in which the image of $g$ is nontrivial. A group is **hopfian** if every surjective endomorphism is an automorphism.

**Proposition.** A finitely generated residually finite group has a solvable word problem; free groups, free products of finite groups and finitely generated nilpotent groups are residually finite. Consequently for these classes the word problem has a positive solution even where the general presentation gives no algorithm.

**Proof sketch.** Given a word $w$, enumerate the finite quotients of the finitely presented group together with the images of the generators; if $w$ represents the identity then every finite quotient sends $w$ to the identity, and if $w$ does not represent the identity then residual finiteness supplies a finite quotient separating it. The enumeration terminates in the second case because a finite quotient can be found among the finitely many quotients of the finite quotients of the presentation up to a bounded order. $\square$

The class of groups with solvable word problem is therefore large but not closed under taking finitely presented subgroups: the Novikov–Boone theorem produces a finitely presented group with undecidable word problem, while every free group has a decidable one. Finitely presented subgroups of free groups are free and hence decidable by Nielsen–Schreier; the failure begins with hyperbolic groups, where finitely presented subgroups can have undecidable word problem.

## Summary

A free group has a unique reduced normal form, so its word problem is solvable by free reduction, and Nielsen transformations compute the rank of a subgroup inside a free group. A presentation $\langle X \mid R\rangle$ presents $F(X)$ modulo the normal closure of $R$; the word problem asks for an algorithm deciding which words represent the identity, it is solvable for free groups, free products, small cancellation groups and finitely generated nilpotent groups, and it is undecidable in general by the Novikov–Boone theorem; Dehn's algorithm solves it for Dehn presentations, in particular for the small cancellation condition $C'(1/6)$.

The Nielsen–Schreier theorem says that every subgroup of a free group is free; a proof by Schreier transversals constructs a free basis from the Schreier generators $s(t,x) = tx\overline{tx}^{-1}$, and for a subgroup of finite index $k$ in $F_n$ the rank is $1 + k(n-1)$. Grushko's theorem makes the rank additive under free products. The Kurosh theorem describes a subgroup of a free product as a free product of a free group with conjugates of subgroups of the factors.

Amalgamated free products $A *_C B$ and HNN extensions $G*_\alpha$ are the basic gluing constructions, with normal forms and Britton's lemma; the Baumslag–Solitar groups $BS(m,n) = \langle a,t \mid ta^mt^{-1} = a^n\rangle$ are the standard examples, with $BS(1,n) \cong \mathbb{Z}[1/n] \rtimes \mathbb{Z}$ solvable and $BS(2,3)$ having an unsolvable word problem. Finitely presented groups are accessible, every recursively presented group embeds in a finitely presented one by Higman's theorem, and finitely generated residually finite groups have solvable word problems. The geometric theory of groups acting on trees is deferred to Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F(X)$, $F_n$ | Free group on a set; free group of rank $n$ |
| $\langle X \mid R\rangle$ | Presentation with generators $X$ and relators $R$ |
| $|w|$ | Length of a word |
| $N(R)$ | Normal closure of $R$ |
| $s(t,x) = tx\,\overline{tx}^{-1}$ | Schreier generator |
| $T$, $\bar{tx}$ | Schreier transversal; representative of the coset of $tx$ |
| $\operatorname{rk}(G)$ | Minimal number of generators |
| $A *_C B$ | Amalgamated free product over $C$ |
| $G*_\alpha$ | HNN extension by the isomorphism $\alpha$ |
| $t$ | Stable letter |
| $BS(m,n)$ | Baumslag–Solitar group $\langle a,t \mid ta^mt^{-1}=a^n\rangle$ |
| $\mathbb{Z}[1/n]$ | Integers localised at $n$ |
| $C'(p)$ | Small cancellation condition on the pieces of a presentation |

## Further Reading

- Wilhelm Magnus, Abraham Karrass and Donald Solitar, *Combinatorial Group Theory: Presentations of Groups in Terms of Generators and Relations*, 2nd ed. (Dover, 1976), for the standard treatment of free groups, Nielsen transformations, the word problem and the Nielsen–Schreier theorem.
- Roger C. Lyndon and Paul E. Schupp, *Combinatorial Group Theory* (Springer, 1977; reprinted Classics in Mathematics, 2001), for small cancellation theory, HNN extensions, and the Kurosh subgroup theorem.
- Otto Schreier, "Die Untergruppen der freien Gruppen", *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg* **5** (1927), 161–183, for the transversal proof that subgroups of free groups are free.
- Jakob Nielsen, "Die Isomorphismen der allgemeinen unendlichen Gruppe mit zwei Erzeugenden", *Mathematische Annalen* **78** (1918), 385–397, for Nielsen transformations and the automorphisms of free groups.
- Aleksandr Kurosh, "Die Untergruppen der freien Produkte von beliebigen Gruppen", *Mathematische Annalen* **109** (1934), 647–660, for the subgroup theorem for free products.
- Pyotr S. Novikov, "On the algorithmic unsolvability of the word problem in group theory", *Trudy Matematicheskogo Instituta imeni V. A. Steklova* **44** (1955), 1–143, and William W. Boone, "The word problem", *Annals of Mathematics* **70** (1959), 207–265, for the undecidability of the word problem.
- John L. Britton, "The word problem for groups", *Proceedings of the London Mathematical Society* **4** (1954), 493–506, for the normal form and lemma for HNN extensions.
- Graham Higman, "Subgroups of finitely presented groups", *Proceedings of the Royal Society A* **262** (1961), 455–475, for the embedding theorem and accessibility.
- Gilbert Baumslag and Donald Solitar, "Some two-generator one-relator non-Hopfian groups", *Bulletin of the American Mathematical Society* **68** (1962), 199–201, for the groups $BS(m,n)$.
- Martin J. Dunwoody, "The accessibility of finitely presented groups", *Inventiones Mathematicae* **81** (1985), 449–457, for the accessibility theorem.
