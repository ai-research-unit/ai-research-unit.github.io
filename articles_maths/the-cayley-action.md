
# __The Cayley Action__

## Introduction

The action of a group on itself by left translation is the action that realises the group: read as a permutation action it is faithful, so it embeds the group into the symmetric group of its own underlying set, and read through the group algebra it linearises to the regular representation. This article treats that single action as the canonical realisation, isolating the two consequences — the canonical embedding $G\hookrightarrow\operatorname{Sym}(G)$, which is Cayley's theorem, and the linearisation of the action that is the regular representation. The action of the product group on $G$, its kernel and its restrictions are *The Action of a Group on Itself*; the translation operators for themselves are *Left and Right Multiplication in a Group*; the algebra of the linearised action is *Group Algebras*; and the general theory of actions, the coset actions, the kernels and the orbit decomposition are *Transformation Groups*.

The article assumes the elementary theory of groups from *Groups*, the definition of an action, the permutation representation, faithfulness, the orbit–stabiliser theorem and Cayley's theorem from *Transformation Groups*, and the group algebra with its left regular representation from *Group Algebras*. It uses no distance, no norm and no form.

## The Action

**Definition.** The **Cayley action** of $G$ is the left translation action of $G$ on its own underlying set,

$$
G\times G \longrightarrow G, \qquad (a,x) \longmapsto a\cdot x = ax .
$$

**Proposition.** The Cayley action is an action, and it is **free**: for $a\neq e$ and every $x$ one has $a\cdot x\neq x$. It is **transitive**: every $x$ is $x\cdot e$, so there is a single orbit. An action that is free and transitive is **sharply transitive**, and then the stabiliser of every point is trivial.

**Proof.** The action axioms are associativity and the identity law. If $a\cdot x=x$ then $a=e$ by cancellation, so no non-identity element fixes a point, which is freeness; and $a\cdot e=a$ gives transitivity. A free transitive action has trivial stabilisers, and the orbit–stabiliser theorem of *Transformation Groups* then gives a single orbit of size $|G|$.

**Proposition (the permutation representation).** The permutation representation of the Cayley action is

$$
\rho_L : G \longrightarrow \operatorname{Sym}(G), \qquad \rho_L(a)(x) = ax ,
$$

a homomorphism; and it is injective.

**Proof.** An action is a homomorphism into the symmetric group by *Transformation Groups*; here $\rho_L(a)=L_a$, and $L_aL_b=L_{ab}$ is the composition law of *Left and Right Multiplication in a Group*. Injectivity: if $\rho_L(a)=\mathrm{id}$ then $a=a\cdot e=e$.

The injectivity is the triviality of the kernel of the action: the kernel is the set of $a$ fixing every point, and it is $\{e\}$. A free action has trivial kernel by definition, and so is faithful.

## The Canonical Embedding

**Theorem (Cayley).** The Cayley action embeds $G$ as a subgroup of $\operatorname{Sym}(G)$; explicitly $\rho_L$ is an isomorphism of $G$ onto the subgroup $L(G)=\{L_a:a\in G\}$. If $G$ is finite of order $n$, composing with a labelling of $G$ by $\{1,\dots,n\}$ gives an embedding $G\hookrightarrow S_n$.

**Proof.** The map $\rho_L$ is an injective homomorphism by the propositions above, so it is an isomorphism onto its image, and the image is $L(G)$. A labelling of $G$ is a bijection $G\to\{1,\dots,n\}$, which induces an isomorphism $\operatorname{Sym}(G)\to S_n$ by *Transformation Groups*.

The embedding is canonical in the sense that it uses no labelling of the elements: it is defined by the group law alone. A labelling is needed only to compare the image with the standard symmetric group $S_n$. This is the precise sense in which an abstract group is a transformation group of its own underlying set, and it is the reason a statement about groups that can be phrased in terms of permutations may be proved by passing to the symmetric group.

**Remark (the left regular subgroup).** The image $L(G)$ is the **left regular subgroup** of $\operatorname{Sym}(G)$. The right translations form a second copy $R(G)$, commuting with $L(G)$, and the two meet in the central translations; the details are *Left and Right Multiplication in a Group*. The Cayley action is the one-sided member of the family of actions of $G$ on itself, and the two-sided member, with its kernel the diagonal centre, is *The Action of a Group on Itself*.

## The Linearisation

The Cayley action linearises, and the linearisation is the regular representation.

**Definition.** The **left regular representation** of $G$ is the algebra map

$$
\lambda : k[G] \longrightarrow \operatorname{End}_k(k[G]), \qquad \lambda(x)(y) = xy ,
$$

the $k$-linear extension of the left translations $L_a$ to the group algebra.

**Proposition.** The map $\lambda$ is an injective algebra homomorphism; its restriction to $G$ is the linear extension of the permutation representation $\rho_L$, so the Cayley action is the set-level shadow of the left regular representation.

**Proof.** That $\lambda$ is an injective algebra homomorphism and that its image is described by the commutant of the right translations are the content of *Group Algebras*, where the left regular representation is introduced. Its restriction to $G\subseteq k[G]$ sends $a$ to the linear operator $L_a$, extended by linearity, which is the linearisation of the permutation $\rho_L(a)$.

**Remark.** The linearisation is the passage from the symmetric group to the general linear group: the permutation $\rho_L(a)$ becomes the linear operator $\lambda(a)$ on the algebra, and the two carry the same information about $G$ because both are injective. The module-theoretic use of the action — that $k[G]$-modules are the representations of $G$ — belongs to *Group Algebras* and to the representation theory of the later parts.

**Remark (the coset actions).** The Cayley action is the extreme case of the family of actions of $G$ on the coset spaces $G/H$, obtained by taking $H=\{e\}$; the action of $G$ on $G/H$ has kernel the **core** $\bigcap_{a\in G}aHa^{-1}$, the largest normal subgroup of $G$ contained in $H$, so the action is faithful exactly when the core is trivial. The family and its kernels are *Transformation Groups*.

**Remark (the two cautions).** The degree of the action is $|G|$, which is large, and a smaller faithful action often exists; the least degree of a faithful permutation representation is an invariant of $G$. And because the action is free, it uses no structure of $G$: it forgets the internal structure entirely, which is why it proves general facts but computes nothing. Both cautions are recorded in *Transformation Groups* and are the reason the action is used as a universal embedding rather than as a computational tool.

## Summary

The **Cayley action** is the left translation action of $G$ on its own underlying set. It is free and transitive, hence sharply transitive, and its permutation representation $\rho_L:a\mapsto L_a$ is injective, so its kernel is trivial. Cayley's theorem is the resulting isomorphism of $G$ onto the left regular subgroup $L(G)\leq\operatorname{Sym}(G)$, and, after a labelling of the $n$ elements, an embedding $G\hookrightarrow S_n$ for finite $G$. The embedding is canonical: it uses the group law and no labelling.

The linearisation of the Cayley action is the **left regular representation** $\lambda(x)(y)=xy$, an injective algebra homomorphism of $k[G]$ into its endomorphism algebra; its restriction to $G$ is the linear extension of $\rho_L$. The Cayley action is the member $H=\{e\}$ of the family of coset actions $G/H$, whose kernel is the core of $H$, and its two cautions are its large degree and its freedom, which forgets the structure of the group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $a\cdot x=ax$ | the Cayley action, left translation of $G$ on itself |
| free | no non-identity element fixes a point |
| sharply transitive | free and transitive, so all point stabilisers trivial |
| $\rho_L(a)=L_a$ | permutation representation of the Cayley action, injective |
| $L(G)=\{L_a:a\in G\}$ | the left regular subgroup of $\operatorname{Sym}(G)$, isomorphic to $G$ |
| $G\hookrightarrow S_n$ | Cayley's embedding for a finite group of order $n$ |
| $\lambda(x)(y)=xy$ | the left regular representation, the linearisation of the action |
| core of $H$ | $\bigcap_{a\in G}aHa^{-1}$, the kernel of the action on $G/H$ |

## Further Reading

- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, fourth edition, 1995), for Cayley's theorem and the regular representation.
- Derek J. S. Robinson, *A Course in the Theory of Groups* (Springer, second edition, 1996), for the canonical embedding and the cohomological interpretation of group extensions.
- John D. Dixon and Brian Mortimer, *Permutation Groups* (Springer, Graduate Texts in Mathematics 163, 1996), for faithful actions of least degree and the regular permutation groups.
- Marshall Hall, *The Theory of Groups* (Macmillan, 1959), for the classical proof of Cayley's theorem and the coset actions.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Wiley, 1962), for the regular representation as the linearisation of the regular action.
