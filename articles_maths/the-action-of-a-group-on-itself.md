
# __The Action of a Group on Itself__

## Introduction

Every group carries actions on its own underlying set, and the simplest of them — translation on the left, translation on the right, and both at once — are the source of the regular representations and of the embedding of the group into a symmetric group. This article treats those actions as actions: the left translation action of $G$ on $G$, the two-sided action of $G\times G$ on $G$, the permutation representation each of them defines, the kernel of each and its triviality, and the two immediate consequences, that the group realises itself faithfully in its own symmetric group and that the two-sided action realises a quotient of $G\times G$. The one-sided multiplication operators themselves, their algebra and their commutation are *Left and Right Multiplication in a Group*; the faithfulness of the left translation action and the linearisation of it that gives the regular representation are *The Cayley Action*.

The article assumes the definition and the elementary theory of groups from *Groups*, the notion of an action, the associated permutation representation, the kernel of an action, faithfulness and the orbit–stabiliser theorem from *Transformation Groups*, and the factorisation $c_g=L_gR_{g^{-1}}$ of the inner conjugation from *Inner Conjugation and the Class Operator*. It uses no distance, no norm and no form: all the actions here are actions on a set.

## The Left Translation Action

**Definition.** The **left translation action** of $G$ on itself is

$$
G \times G \longrightarrow G, \qquad (a,x) \longmapsto a\cdot x = ax .
$$

**Proposition.** The left translation action is an action, and the permutation representation it defines is the map $\rho_L : G \to \operatorname{Sym}(G)$, $\rho_L(a)(x)=ax$.

**Proof.** The identity acts trivially, $e\cdot x=x$, and associativity gives $(ab)\cdot x = (ab)x = a(bx) = a\cdot(b\cdot x)$. The permutation representation is the homomorphism attached to an action by *Transformation Groups*, and here it is left multiplication by $a$.

**Proposition (the kernel, and faithfulness).** The kernel of the left translation action is trivial; hence the action is faithful and $\rho_L$ is injective.

**Proof.** If $a\cdot x=x$ for all $x$ then taking $x=e$ gives $a=e$. The kernel is the set of such $a$ by the definition in *Transformation Groups*, so it is $\{e\}$, and an action with trivial kernel is faithful.

The faithfulness is the content of Cayley's theorem, and it is taken up as such in *The Cayley Action*; here it is recorded as the statement that the kernel of this particular action is trivial.

**Remark (free and sharply transitive).** The left translation action is **free**: a non-identity element moves every point, because $ax=x$ forces $a=e$. It is also transitive, because $a\cdot e=a$ for every $a$; an action that is both is **sharply transitive**, and its orbits are singletons in the stabiliser sense: $\operatorname{Stab}(x)=\{e\}$ for every $x$.

## The Right Translation Action

**Definition.** The **right translation action** of $G$ on itself is

$$
G \times G \longrightarrow G, \qquad (a,x) \longmapsto x\cdot a = xa ,
$$

read as an action written on the right. Equivalently, it is the left action of the opposite group $G^{\mathrm{op}}$ given by $a\cdot x = xa$, the multiplication of $G^{\mathrm{op}}$ being $a\cdot^{\mathrm{op}}b=ba$.

**Proposition.** The right translation action is a right action, $(x\cdot a)\cdot b = x\cdot(ab)$, and it is faithful, with permutation representation $\rho_R : G \to \operatorname{Sym}(G)$ the anti-homomorphism $\rho_R(a)(x)=xa$, so that $\rho_R(ab)=\rho_R(b)\circ\rho_R(a)$.

**Proof.** $(x a)b=x(ab)$ is associativity, and the kernel is trivial because $xa=x$ for all $x$ forces $a=e$ on taking $x=e$. The reversal $\rho_R(ab)=\rho_R(b)\rho_R(a)$ is the general fact that a right action is a left action of the opposite group, as in *Transformation Groups*.

## The Two-Sided Action

The left and the right translation can be performed together.

**Definition.** The **two-sided action** of the product $G\times G$ on $G$ is

$$
(G\times G)\times G \longrightarrow G, \qquad \bigl((a,b),x\bigr) \longmapsto (a,b)\cdot x = a\,x\,b^{-1}.
$$

The right factor is inverted so that the assignment is a left action.

**Proposition.** The two-sided action is a left action of $G\times G$, and the permutation representation it defines is

$$
\rho : G\times G \longrightarrow \operatorname{Sym}(G), \qquad \rho(a,b)(x) = a\,x\,b^{-1} .
$$

**Proof.** $((e,e)\cdot x)=x$, and

$$
(a,b)\cdot\bigl((c,d)\cdot x\bigr) = a\,(c\,x\,d^{-1})\,b^{-1} = (ac)\,x\,(bd)^{-1} = (ac,bd)\cdot x ,
$$

which is the multiplication of the product group; the statement about $\rho$ is the correspondence between actions and homomorphisms of *Transformation Groups*.

**Proposition (the kernel of the two-sided action).** The kernel of $\rho$ is the diagonal copy of the centre,

$$
\ker\rho = \{(z,z) : z \in Z(G)\} \cong Z(G),
$$

so the two-sided action is faithful if and only if $G$ has trivial centre; in general it is a faithful action of the quotient $(G\times G)/Z(G)$, where $Z(G)$ is embedded diagonally.

**Proof.** $(a,b)$ lies in the kernel exactly when $a x b^{-1}=x$ for every $x$, that is $ax=xb$ for every $x$. Taking $x=e$ gives $a=b$; substituting back gives $ax=xa$ for every $x$, so $a\in Z(G)$. Conversely a diagonal pair $(z,z)$ with $z$ central satisfies $zx=xz$ and so acts trivially. The identification of the image with the quotient is the first isomorphism theorem, and an action with kernel $K$ gives a faithful action of $G/K$ by *Transformation Groups*.

**Proposition (the inner conjugation is a restriction).** The conjugation action of $G$ on itself is the restriction of the two-sided action to the **diagonal**

$$
\Delta = \{(g,g) : g \in G\} \leq G\times G ,
$$

which is a subgroup isomorphic to $G$: for every $x$,

$$
(g,g)\cdot x = g\,x\,g^{-1} = c_g(x).
$$

**Proof.** The diagonal is closed under the componentwise multiplication, $(g,g)(h,h)=(gh,gh)$, and it is isomorphic to $G$ by the first projection. The computation is the definition of the two-sided action with $a=b=g$. The restriction of $\rho$ to it is the map $g\mapsto c_g$ of *Inner Conjugation and the Class Operator*.

The two-sided action therefore organises the actions on the underlying set: the left translation is the restriction to $G\times\{e\}$, the right translation is the restriction to $\{e\}\times G$, and the conjugation is the restriction to the diagonal $\Delta$. The other subgroups of $G\times G$ give their own restrictions, and the one along $\{(g,g^{-1})\}$ — which is a subgroup only when $G$ is abelian — sends $x$ to $gxg$.

## The Associated Permutation Representation

The permutation representation $\rho : G\times G\to\operatorname{Sym}(G)$ and the two one-sided representations $\rho_L,\rho_R$ are related by the factorisation of a two-sided element.

**Proposition.** For every $(a,b)$,

$$
\rho(a,b) = \rho_L(a)\circ\rho_R(b^{-1}) = \rho_R(b^{-1})\circ\rho_L(a).
$$

**Proof.** On $x$, both sides give $axb^{-1}$; the two orders agree because $\rho_L(a)\rho_R(c)=\rho_R(c)\rho_L(a)$ for all $a,c$, each side sending $x$ to $axc$.

The factorisation exhibits the image of $\rho$ inside the symmetric group: it is the set of products of a left and a right translation. The subgroup of $\operatorname{Sym}(G)$ that this image generates, the commutation of the two one-sided families and the two regular representations they define are *Left and Right Multiplication in a Group*; here the point is only that the two-sided representation is assembled from the one-sided ones.

**Proposition (the image and its one-sided subgroups).** The image of $\rho$ is generated by the two commuting subgroups $\rho(G\times\{e\})=\{L_a : a\in G\}$ and $\rho(\{e\}\times G)=\{R_b : b\in G\}$, each isomorphic to $G$; their intersection is $\{L_z : z\in Z(G)\}$, the image of the centre; and the image is isomorphic to $(G\times G)/Z(G)$ with $Z(G)$ embedded diagonally.

**Proof.** Every $\rho(a,b)=L_aR_{b^{-1}}$ is a product of one element of each family, so the two subgroups generate the image, and they commute because $L_aR_b(x)=axb=R_bL_a(x)$. If $L_a=R_b$ then $ax=xb$ for every $x$; taking $x=e$ gives $a=b$ and then $ax=xa$ gives $a\in Z(G)$, so the intersection is the image of the centre. The last statement is the kernel proposition together with the first isomorphism theorem.

## Summary

The group $G$ acts on its own underlying set in three standard ways. The **left translation action** $a\cdot x=ax$ is free and transitive, hence sharply transitive, its kernel is trivial, and its permutation representation $\rho_L$ is the injective map $a\mapsto L_a$. The **right translation action** $x\cdot a=xa$ is a right action, equivalently a left action of the opposite group $G^{\mathrm{op}}$, faithful, with representation the anti-homomorphism $\rho_R : a\mapsto R_a$.

The **two-sided action** $((a,b),x)\mapsto axb^{-1}$ is a left action of the product $G\times G$, with permutation representation $\rho(a,b)=L_aR_{b^{-1}}=R_{b^{-1}}L_a$. Its kernel is the diagonal copy of the centre, $\{(z,z): z\in Z(G)\}$, so it is faithful exactly when the centre is trivial, and its image is isomorphic to $(G\times G)/Z(G)$. It is generated by the two commuting one-sided subgroups $\rho_L(G)=\{L_a\}$ and $\rho_R(G)=\{R_b\}$, whose intersection is the image of the centre. The left translation, the right translation and the inner conjugation are its restrictions to $G\times\{e\}$, $\{e\}\times G$ and the diagonal $\Delta=\{(g,g):g\in G\}$ respectively.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $a\cdot x=ax$ | left translation action of $G$ on itself |
| $x\cdot a=xa$ | right translation action, a left action of $G^{\mathrm{op}}$ |
| $\rho_L : G\to\operatorname{Sym}(G)$ | permutation representation of the left translation action, $a\mapsto L_a$ |
| $\rho_R : G\to\operatorname{Sym}(G)$ | permutation representation of the right translation action, $a\mapsto R_a$, an anti-homomorphism |
| $((a,b),x)\mapsto axb^{-1}$ | two-sided action of $G\times G$ on $G$ |
| $\rho : G\times G\to\operatorname{Sym}(G)$ | permutation representation of the two-sided action |
| $\ker\rho=\{(z,z):z\in Z(G)\}$ | kernel of the two-sided action, the diagonal centre |
| $\{(g,g^{-1}):g\in G\}$ | twisted diagonal, on which the action is the inner conjugation |
| $\{(g,g):g\in G\}$ | diagonal, on which the action is trivial |

## Further Reading

- Derek J. S. Robinson, *A Course in the Theory of Groups* (Springer, second edition, 1996), for the regular actions, the two-sided action and the diagonal embeddings of the centre.
- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, fourth edition, 1995), for the left and right regular actions and Cayley's theorem.
- John D. Dixon and Brian Mortimer, *Permutation Groups* (Springer, Graduate Texts in Mathematics 163, 1996), for free and sharply transitive actions and the degree of a faithful representation.
- Marshall Hall, *The Theory of Groups* (Macmillan, 1959), for the classical treatment of the regular representations and their kernels.
- Helmut Wielandt, *Finite Permutation Groups* (Academic Press, 1964), for the permutation representations attached to a group's action on itself and on its cosets.
