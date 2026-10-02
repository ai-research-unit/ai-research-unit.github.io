
# __The Conjugation Representation__

## Introduction

The assignment that sends an element $g$ to the inner automorphism $c_g$ is a homomorphism from the group into its own automorphism group. This article treats that homomorphism as a representation: it fixes its kernel and its image, so that the inner automorphisms are a quotient of the group by its centre; it separates the inner automorphisms from the outer ones, which are the quotient by the inner ones; and it follows the representation to the action of the automorphism group on the set of conjugacy classes, which is the one place where the outer automorphisms are visible as permutations.

The article assumes the definition of the automorphism group and the centre from *Groups*, the automorphism group of a structure, its inner automorphisms and the identity $\operatorname{Inn}(G)\cong G/Z(G)$ from *Transformation Groups*, and the inner conjugation operator $c_g$, its composition law and the conjugacy classes from *Inner Conjugation and the Class Operator*. The action of the group on itself by conjugation is *The Action of a Group on Itself*; the linearisation of the representation on the group algebra is mentioned only to be pointed at. No distance, no norm and no form is used.

## The Representation

**Definition.** The **conjugation representation** of $G$ is

$$
\rho : G \longrightarrow \operatorname{Aut}(G), \qquad \rho(g) = c_g, \quad c_g(x)=gxg^{-1}.
$$

**Proposition.** $\rho$ is a homomorphism of groups, with

$$
\ker\rho = Z(G), \qquad \operatorname{im}\rho = \operatorname{Inn}(G), \qquad \operatorname{Inn}(G) \cong G/Z(G).
$$

**Proof.** The composition law $c_gc_h=c_{gh}$ and $c_e=\mathrm{id}$ from *Inner Conjugation and the Class Operator* say that $\rho$ is a homomorphism. An element $g$ lies in the kernel exactly when $gxg^{-1}=x$ for every $x$, which is $g\in Z(G)$. The image is by definition the group of inner automorphisms, and the isomorphism is the first isomorphism theorem. The identity $\operatorname{Inn}(G)\cong G/Z(G)$ is also stated in *Transformation Groups*, where the conjugation action is introduced.

**Corollary (faithfulness).** The conjugation representation is injective exactly when $Z(G)=\{e\}$; in that case $G$ is isomorphic to its group of inner automorphisms.

**Proof.** Immediate from the kernel statement.

**Remark.** The representation is the discrete form of the adjoint representation of a Lie group; here it is a homomorphism of abstract groups, and no differentiability is involved. The linearisation of the representation, in which the group algebra is acted on by the inner automorphisms of the algebra induced by the units of $G$, is *Group Algebras* together with the representation theory of the later parts.

## Inner and Outer Automorphisms

**Definition.** The **outer automorphism group** of $G$ is the quotient

$$
\operatorname{Out}(G) = \operatorname{Aut}(G)/\operatorname{Inn}(G).
$$

Its elements are the **outer automorphisms**: they are cosets of inner automorphisms, and no single representative of a nontrivial coset is itself inner.

**Proposition (normality).** $\operatorname{Inn}(G)$ is a normal subgroup of $\operatorname{Aut}(G)$. Indeed, for $\varphi\in\operatorname{Aut}(G)$ and $g\in G$,

$$
\varphi\, c_g\, \varphi^{-1} = c_{\varphi(g)} .
$$

**Proof.** For every $x$, $(\varphi c_g \varphi^{-1})(x) = \varphi\bigl(g\,\varphi^{-1}(x)\,g^{-1}\bigr) = \varphi(g)\,x\,\varphi(g)^{-1} = c_{\varphi(g)}(x)$, using the multiplicativity of $\varphi$ and $\varphi^{-1}$. The right-hand side is inner, so the conjugate of an inner automorphism is inner.

**Proposition (the two exact sequences).** There are exact sequences of groups

$$
1 \longrightarrow Z(G) \longrightarrow G \xrightarrow{\ \rho\ } \operatorname{Aut}(G) \longrightarrow \operatorname{Out}(G) \longrightarrow 1 ,
$$

and, if $\operatorname{Inn}(G)$ is identified with $G/Z(G)$,

$$
1 \longrightarrow \operatorname{Inn}(G) \longrightarrow \operatorname{Aut}(G) \longrightarrow \operatorname{Out}(G) \longrightarrow 1 .
$$

**Proof.** The kernel of $\rho$ is $Z(G)$ and its image is $\operatorname{Inn}(G)$; the quotient map $\operatorname{Aut}(G)\to\operatorname{Out}(G)$ is surjective with kernel $\operatorname{Inn}(G)$. Gluing the two statements at $\operatorname{Inn}(G)$ gives the first sequence, and the second is the definition of $\operatorname{Out}(G)$.

**Corollary (the semidirect decomposition when the centre is trivial).** If $Z(G)=\{e\}$ then $G\cong\operatorname{Inn}(G)\trianglelefteq\operatorname{Aut}(G)$, so $G$ sits inside its automorphism group as a normal subgroup, and $\operatorname{Aut}(G)$ is an extension of $\operatorname{Out}(G)$ by $G$.

**Proof.** The isomorphism $G\cong\operatorname{Inn}(G)$ is the corollary on faithfulness, normality is the proposition above, and an extension is a group with a normal subgroup and a quotient, which is what the second exact sequence exhibits. Whether the extension splits is a question about the existence of a complement; the semidirect products themselves are *Generators, Presentations and Free Products*, and the cohomological obstruction to splitting is *Group Cohomology*.

The inner automorphisms are those that come from elements; the outer ones measure what is left when they are divided out. The quotient is trivial exactly when every automorphism is inner, and this is the property that makes a group **complete** — centreless with all automorphisms inner — a notion that recurs in the study of the symmetric groups and is not pursued here.

## The Action on the Conjugacy Classes

Every automorphism carries a conjugacy class to a conjugacy class, so the automorphism group acts on the set of classes.

**Proposition (the action is well defined).** For $\varphi\in\operatorname{Aut}(G)$ and $x\in G$,

$$
\varphi\bigl(\chi(x)\bigr) = \chi\bigl(\varphi(x)\bigr),
$$

so $\varphi$ induces a permutation of the set $\operatorname{Cl}(G)$ of conjugacy classes, and the assignment $\operatorname{Aut}(G)\to\operatorname{Sym}(\operatorname{Cl}(G))$ is an action.

**Proof.** For $g\in G$, $\varphi(gxg^{-1}) = \varphi(g)\varphi(x)\varphi(g)^{-1}$, so the image of the class of $x$ is the class of $\varphi(x)$. The assignment is compatible with composition and sends the identity to the identity, hence is an action in the sense of *Transformation Groups*.

**Proposition (the kernel of the action on the classes).** Let

$$
K = \{\varphi\in\operatorname{Aut}(G) : \varphi(x) \text{ is conjugate to } x \text{ for every } x\} .
$$

Then $K$ is a normal subgroup of $\operatorname{Aut}(G)$, it contains $\operatorname{Inn}(G)$, and it is the kernel of the action of $\operatorname{Aut}(G)$ on $\operatorname{Cl}(G)$. Hence the action factors through $\operatorname{Aut}(G)/K$, and $\operatorname{Out}(G)$ maps onto that quotient with kernel $K/\operatorname{Inn}(G)$.

**Proof.** The set $K$ is the kernel of a homomorphism, hence normal. An inner automorphism carries $x$ to $gxg^{-1}$, which is conjugate to $x$ by definition, so $\operatorname{Inn}(G)\subseteq K$. Conversely a representative of the kernel carries every $x$ to a conjugate, so it lies in $K$. The factorisation is the first isomorphism theorem applied to the action, and the identification of the quotient $\operatorname{Out}(G)/(K/\operatorname{Inn}(G))$ with $\operatorname{Aut}(G)/K$ is the third isomorphism theorem. The automorphisms in $K$ are the **class-preserving** automorphisms.

**Corollary (the group acts trivially on its own classes).** The restriction of the action to the inner automorphisms is trivial: for every $g$ and every class $\chi$, $c_g(\chi)=\chi$. Consequently the conjugation action of $G$ on $\operatorname{Cl}(G)$ factors through the trivial action, and it is the outer automorphisms that permute the classes nontrivially.

**Proof.** By the first of the two propositions above with $\varphi=c_g$, the image of $\chi(x)$ is $\chi(gxg^{-1})=\chi(x)$, because $gxg^{-1}$ is conjugate to $x$. So each $c_g$ fixes every class, and the action of $G$ through $\rho$ is trivial. The action of $\operatorname{Aut}(G)$ is the only one that can move a class, and it does so through the quotient $\operatorname{Aut}(G)/K$.

The corollary is the sense in which the outer automorphisms are invisible in the group's own conjugation and visible only in its symmetries: an inner automorphism cannot move a class, because moving a class requires leaving the group, and an automorphism that is class-preserving cannot move it either. The class-preserving automorphisms can be strictly larger than the inner ones, and then the action carries strictly less information than $\operatorname{Out}(G)$; the general study of that gap is a theorem of the finite-group literature and is cited rather than reproduced.

## Summary

The **conjugation representation** is the homomorphism $\rho : G\to\operatorname{Aut}(G)$, $\rho(g)=c_g$, $c_g(x)=gxg^{-1}$. Its kernel is the centre and its image is the group of inner automorphisms, so $\operatorname{Inn}(G)\cong G/Z(G)$ and the representation is faithful exactly when $Z(G)$ is trivial. The inner automorphisms are normal in $\operatorname{Aut}(G)$, because $\varphi c_g\varphi^{-1}=c_{\varphi(g)}$; the quotient is the **outer automorphism group** $\operatorname{Out}(G)=\operatorname{Aut}(G)/\operatorname{Inn}(G)$, and the two fit the exact sequences $1\to Z(G)\to G\to\operatorname{Aut}(G)\to\operatorname{Out}(G)\to1$ and $1\to\operatorname{Inn}(G)\to\operatorname{Aut}(G)\to\operatorname{Out}(G)\to1$. When the centre is trivial, $G\cong\operatorname{Inn}(G)\trianglelefteq\operatorname{Aut}(G)$ and $\operatorname{Aut}(G)$ is an extension of $\operatorname{Out}(G)$ by $G$.

Every automorphism permutes the conjugacy classes, $\varphi(\chi(x))=\chi(\varphi(x))$, so $\operatorname{Aut}(G)$ acts on the set of classes; the kernel of that action is the normal subgroup $K$ of **class-preserving** automorphisms, which contains $\operatorname{Inn}(G)$. The group $G$ itself acts trivially on its own classes, since each inner automorphism fixes every class, and the nontrivial part of the action is carried by $\operatorname{Aut}(G)/K$, a quotient of $\operatorname{Out}(G)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho : G\to\operatorname{Aut}(G)$ | the conjugation representation, $\rho(g)=c_g$ |
| $c_g(x)=gxg^{-1}$ | the inner conjugation by $g$ |
| $Z(G)$ | the centre, the kernel of $\rho$ |
| $\operatorname{Inn}(G)$ | the inner automorphisms, the image of $\rho$; $\operatorname{Inn}(G)\cong G/Z(G)$ |
| $\operatorname{Out}(G)=\operatorname{Aut}(G)/\operatorname{Inn}(G)$ | the outer automorphism group |
| $1\to Z(G)\to G\to\operatorname{Aut}(G)\to\operatorname{Out}(G)\to1$ | the exact sequence of the representation |
| $\operatorname{Cl}(G)$ | the set of conjugacy classes of $G$ |
| $\varphi(\chi(x))=\chi(\varphi(x))$ | the action of an automorphism on the classes |
| $K$ | the class-preserving automorphisms, the kernel of the action on $\operatorname{Cl}(G)$ |
| complete | centreless with every automorphism inner |

## Further Reading

- Derek J. S. Robinson, *A Course in the Theory of Groups* (Springer, second edition, 1996), for the inner automorphism group, its normality and the exact sequences of the automorphism group.
- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, fourth edition, 1995), for $\operatorname{Inn}(G)\cong G/Z(G)$, the outer automorphism group and the automorphisms of the standard families.
- I. Martin Isaacs, *Finite Group Theory* (American Mathematical Society, Graduate Studies in Mathematics 92, 2008), for class-preserving automorphisms and their relation to the inner ones in a finite group.
- G. E. Wall, "Finite groups with class-preserving outer automorphisms", *Journal of the London Mathematical Society* **22** (1947), 315–320, for the existence of class-preserving automorphisms outside the inner ones.
- John D. Dixon and Brian Mortimer, *Permutation Groups* (Springer, Graduate Texts in Mathematics 163, 1996), for the automorphism group acting on the conjugacy classes and the completeness of the symmetric groups.
