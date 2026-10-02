
# __Inner Conjugation and the Class Operator__

## Introduction

The conjugation action of a group on itself produces, for every element $g$, the operator $c_g(x)=gxg^{-1}$. It is the first operator of the category that is neither a left nor a right translation but the product of the two, and it is the operator from which the conjugacy classes, the centralisers and the class equation are read. This article treats that operator as an object: it fixes it, derives the identities it satisfies, identifies its orbits with the conjugacy classes, follows it to the subgroup lattice, and attaches to each conjugacy class the operator that sums the conjugations by its elements.

The article assumes the elementary theory of groups, the conjugation action, the conjugacy classes, the class equation and the normal subgroups from *Groups*, and the language of actions, orbits, stabilisers, faithful actions and the permutation representation from *Transformation Groups*. The conjugacy classes and the class equation are not re-derived; they are cited, and what is established here is the operator that produces them, the factorisation $c_g=L_gR_{g^{-1}}$ that places it in the operator layer, the composition law $c_gc_h=c_{gh}$, the action on the lattice of subgroups, and the class operator. The interpretation of $g\mapsto c_g$ as a homomorphism into the automorphism group, the inner automorphisms and the outer quotient, is *The Conjugation Representation*; the two-sided operators with a fixed left and right factor are *Left and Right Multiplication in a Group* and *The Signed Sandwich on a Group*; the inversion of a group and the involutions it carries are *Involutive Groups*; and the class sums, their centrality and the centre of the group algebra are *Group Algebras*. Nothing of those entries is repeated.

The article reasons with no distance, no norm and no form. Its operators act on the set $G$; where a sum of operators is needed, the operators are extended linearly to the group algebra $k[G]$, whose elements are finite $k$-linear combinations of the group elements.

## The Inner Conjugation Operator

**Definition.** For $g \in G$ the **inner conjugation by $g$** is the map

$$
c_g : G \longrightarrow G, \qquad c_g(x) = gxg^{-1}.
$$

**Proposition (it is an automorphism).** For every $g$ the map $c_g$ is an automorphism of $G$, with inverse $c_{g^{-1}}$; and $c_e = \mathrm{id}$.

**Proof.** It is bijective, because $c_{g^{-1}}(c_g(x)) = g^{-1}(gxg^{-1})g = x$ and symmetrically. It is a homomorphism, because

$$
c_g(xy) = gxyg^{-1} = (gxg^{-1})(gyg^{-1}) = c_g(x)\,c_g(y).
$$

The statements $c_gc_{g^{-1}}=\mathrm{id}=c_{g^{-1}}c_g$ and $c_e=\mathrm{id}$ are immediate.

**Proposition (the composition law).** For all $g, h \in G$,

$$
c_g \circ c_h = c_{gh}.
$$

**Proof.** For every $x$, $c_g(c_h(x)) = g(hxh^{-1})g^{-1} = (gh)x(gh)^{-1} = c_{gh}(x)$. The law says that the assignment $g\mapsto c_g$ is multiplicative, a fact whose interpretation as a homomorphism into $\operatorname{Aut}(G)$ belongs to *The Conjugation Representation*.

**Proposition (the factorisation into one-sided translations).** Let $L_g(x)=gx$ and $R_h(x)=xh$ be the left and the right translation by $g$ and $h$. Then

$$
c_g = L_g \circ R_{g^{-1}} = R_{g^{-1}} \circ L_g .
$$

**Proof.** $L_g(R_{g^{-1}}(x)) = g\,x\,g^{-1} = R_{g^{-1}}(L_g(x))$, so the two orders agree because the inner conjugation computes both. That the two orders agree is the statement that left and right translations commute, taken up in *Left and Right Multiplication in a Group*.

The factorisation records the position of the inner conjugation in the operator layer of the category: it is the two-sided operator whose left factor and right factor are the single element $g$ and its inverse $g^{-1}$. A general two-sided operator with independent factors is the subject of *The Signed Sandwich on a Group*, and the one-sided factors themselves are the subject of *Left and Right Multiplication in a Group*.

**Proposition (the inversion is an involution on the operators).** Composition of inner conjugations is inner conjugation; inversion of the conjugating element inverts the operator, $c_g^{-1}=c_{g^{-1}}$; and $c_g$ depends only on the coset of $g$ modulo the centre.

**Proof.** The first two statements restate the propositions above. For the last, if $z \in Z(G)$ then $c_{gz}(x) = gzxz^{-1}g^{-1} = gxg^{-1} = c_g(x)$ because $z$ is central; hence $c_{gz}=c_g$ for every $z \in Z(G)$.

## The Orbits: the Conjugacy Classes

The inner conjugations act on the set $G$: the assignment $(g,x)\mapsto c_g(x)$ satisfies $c_e=\mathrm{id}$ and $c_{gh}=c_gc_h$, so it is a left action of $G$ on itself. Its orbits are the **conjugacy classes** of *Groups*: two elements $x,y$ lie in the same orbit exactly when $y=gxg^{-1}$ for some $g$, which is the definition of conjugacy. The class of $x$ is written $\chi(x)$, and the classes partition $G$.

**Proposition (the stabiliser is the centraliser).** For $x \in G$ the stabiliser of $x$ under the conjugation action is the centraliser

$$
C_G(x) = \{ g \in G : gx = xg \},
$$

and the orbit–stabiliser theorem of *Transformation Groups* gives $|\chi(x)| = [G:C_G(x)]$, so the size of a class divides $|G|$ when $G$ is finite.

**Proof.** $c_g(x)=x$ is equivalent to $gx=xg$. The orbital statement is the orbit–stabiliser theorem applied to the action of $G$ on itself by conjugation.

**Proposition (the fixed points are the centre).** The elements whose conjugacy class is a singleton are exactly the elements of the centre $Z(G)$.

**Proof.** $c_g(x)=x$ for all $g$ is the definition of $x\in Z(G)$.

The orbit decomposition of the conjugation action is the **class equation** of *Groups*: for a finite group, the classes of size greater than $1$ contribute $[G:C_G(x_i)]$ and the singleton classes contribute the centre,

$$
|G| = |Z(G)| + \sum_{i} [G:C_G(x_i)],
$$

each index being an integer greater than $1$ that divides $|G|$. The equation is stated and used in *Groups*; its content here is only that it is the orbit decomposition of the operator $c_g$.

## The Action on the Subgroups

The operator $c_g$ is a bijection of $G$, so it carries a subset to a subset of the same cardinality, and it carries a subgroup to a subgroup.

**Proposition.** If $H \leq G$ then $c_g(H) = gHg^{-1} \leq G$, of the same order as $H$; and $c_g$ preserves inclusion, intersection and generation, so $H\mapsto gHg^{-1}$ is an automorphism of the lattice of subgroups of $G$.

**Proof.** $gHg^{-1}$ is closed under multiplication, contains $e$, and is closed under inversion because $(ghg^{-1})^{-1}=gh^{-1}g^{-1}$; its cardinality equals that of $H$ because $x\mapsto gxg^{-1}$ is a bijection. The preservation of inclusion and intersection is immediate from bijectivity, and generation is preserved because the image of a generating set generates the image.

**Proposition (normality is preserved).** If $H \trianglelefteq G$ then $c_g(H)=H$ for every $g$, and conversely a subgroup fixed by every inner conjugation is normal; hence the normal subgroups of $G$ are exactly the fixed points of the conjugation action on the subgroup lattice.

**Proof.** Normality says $gHg^{-1}=H$ for every $g$, which is $c_g(H)=H$; and conversely if $c_g(H)=H$ for all $g$ then $H$ is normal by the definition of normality.

**Proposition (the orbit of a subgroup).** The orbit of $H$ under the conjugation action is its conjugacy class $\{gHg^{-1}: g \in G\}$, its stabiliser is the normaliser $N_G(H)=\{g \in G : gHg^{-1}=H\}$, and its size is $[G:N_G(H)]$; in particular $H$ is normal exactly when its orbit is a single point.

**Proof.** The action on subgroups is the restriction of the conjugation action, so the orbit and stabiliser statements are those of the orbit–stabiliser theorem; the stabiliser of $H$ is by definition the normaliser, and the fixed points are the normal subgroups by the proposition above.

Because $c_g$ preserves the order, the index, the normality, the cyclicity, the commutativity and the derived subgroup of a subgroup, it permutes the subgroups of any fixed order and the normal subgroups of any fixed order. The normal subgroups are the fixed points of that permuted set; this is what makes the conjugation action the tool by which the normal subgroups of a finite group are counted.

## The Class Operator

Let $\chi$ be a conjugacy class of $G$. The class carries an operator formed by summing the conjugations by its elements.

**Definition.** The **class operator** of $\chi$ is the linear operator on the group algebra,

$$
\mathrm{Ad}_\chi = \sum_{g \in \chi} c_g : k[G] \longrightarrow k[G],
$$

the sum of the linear extensions of the inner conjugations by the elements of $\chi$. For a single element write $\mathrm{Ad}_g$ for $c_g$ extended linearly.

The operator $\mathrm{Ad}_g$ is the inner automorphism of the algebra $k[G]$ induced by the unit $g$; the class operator is the sum of these inner automorphisms over a conjugacy class.

**Proposition (it commutes with every inner conjugation).** For every $h \in G$,

$$
\mathrm{Ad}_h \circ \mathrm{Ad}_\chi = \mathrm{Ad}_\chi \circ \mathrm{Ad}_h .
$$

**Proof.** Because $c_h c_g c_h^{-1} = c_{hgh^{-1}}$ for every $g$, by the composition law and the inverse statement, and because $g\mapsto hgh^{-1}$ permutes the class $\chi$,

$$
\mathrm{Ad}_h \,\mathrm{Ad}_\chi\, \mathrm{Ad}_h^{-1} = \sum_{g\in\chi} c_{hgh^{-1}} = \sum_{g'\in\chi} c_{g'} = \mathrm{Ad}_\chi .
$$

Multiplying on the right by $\mathrm{Ad}_h$ gives the claim, since $\mathrm{Ad}_h^{-1}=\mathrm{Ad}_{h^{-1}}$.

**Proposition (its value on the centre).** An element $z \in k[G]$ fixed by every inner conjugation is central, and the class operator acts on it by the scalar $|\chi|$:

$$
\mathrm{Ad}_\chi(z) = |\chi|\, z .
$$

**Proof.** An element is fixed by every $\mathrm{Ad}_g$ exactly when its coefficients are constant on conjugacy classes, which is the centrality statement of *Group Algebras*. For such a $z$ each term of the sum sends $z$ to itself, because $gzg^{-1}=z$ when $z$ is central, and there are $|\chi|$ terms.

In particular, for the **class sum** $C_\psi=\sum_{h\in\psi} h$ of a conjugacy class $\psi$, the class sums being a basis of the centre of $k[G]$ by *Group Algebras*, the proposition gives $\mathrm{Ad}_\chi(C_\psi)=|\chi|\,C_\psi$. The class operators therefore act on the centre diagonally with the class sizes as eigenvalues. The product of two class operators on the centre, and the algebra of the centre that the product defines, are the class algebra of the representation theory and belong to the later categories; what is fixed here is the operator attached to a class and its commutation with the inner conjugations.

## Summary

The **inner conjugation** by $g$ is the operator $c_g(x)=gxg^{-1}$. It is an automorphism of $G$ with inverse $c_{g^{-1}}$, it satisfies the composition law $c_gc_h=c_{gh}$ so that $g\mapsto c_g$ is a multiplicative assignment, and it factors as the two-sided operator $c_g=L_gR_{g^{-1}}=R_{g^{-1}}L_g$ into a left and a right translation. It depends only on the coset of $g$ modulo the centre.

The orbits of the conjugation action are the **conjugacy classes** of *Groups*, the stabiliser of $x$ is the centraliser $C_G(x)$, so the size of a class is $[G:C_G(x)]$, and the fixed points are the elements of the centre. The orbit decomposition is the **class equation**, cited from *Groups*.

On the lattice of subgroups the operator $H\mapsto gHg^{-1}$ is an order-preserving bijection that preserves the order, the index, the normality, the cyclicity and the derived subgroup; the orbit of $H$ is its conjugacy class, its stabiliser is the normaliser $N_G(H)$, its orbit size is $[G:N_G(H)]$, and the normal subgroups are exactly the fixed points.

The **class operator** of a conjugacy class $\chi$ is the sum $\mathrm{Ad}_\chi=\sum_{g\in\chi}c_g$ of the inner conjugations by its elements, extended linearly to the group algebra. It commutes with every inner conjugation, and it acts on the centre of $k[G]$ — the space of central elements, whose basis is formed by the class sums — by the scalar $|\chi|$. In particular the class sum of any class is an eigenvector of every class operator with eigenvalue the size of the operator's class.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $c_g$ | inner conjugation by $g$, $c_g(x)=gxg^{-1}$ |
| $L_g$, $R_h$ | left translation $L_g(x)=gx$ and right translation $R_h(x)=xh$ |
| $c_g=L_gR_{g^{-1}}$ | factorisation of the inner conjugation into one-sided translations |
| $c_gc_h=c_{gh}$ | the composition law of the inner conjugations |
| $\chi(x)$ | the conjugacy class of $x$, the orbit of $x$ under conjugation |
| $C_G(x)$ | centraliser of $x$, the stabiliser of $x$; $|\chi(x)|=[G:C_G(x)]$ |
| $Z(G)$ | centre, the set of singleton orbits |
| $N_G(H)$ | normaliser of $H$, the stabiliser of $H$ in the action on subgroups |
| $\mathrm{Ad}_g$ | the linear extension of $c_g$ to $k[G]$, the inner automorphism of the algebra |
| $\mathrm{Ad}_\chi=\sum_{g\in\chi}c_g$ | class operator of the conjugacy class $\chi$ |
| $C_\psi=\sum_{h\in\psi}h$ | class sum of $\psi$, central in $k[G]$ by *Group Algebras* |
| $k[G]$ | group algebra of finite $k$-linear combinations of the group elements |

## Further Reading

- Derek J. S. Robinson, *A Course in the Theory of Groups* (Springer, second edition, 1996), for the conjugation action, the conjugacy classes, the centraliser and the action on the subgroup lattice.
- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, fourth edition, 1995), for the orbit decomposition and the class equation of a finite group.
- I. Martin Isaacs, *Character Theory of Finite Groups* (Academic Press, 1976), for the class sums as a basis of the centre of the group algebra and the class multiplication coefficients.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Wiley, 1962), for the inner automorphisms of the group algebra and the centre as the fixed space of the conjugation action.
- Donald S. Passman, *The Algebraic Structure of Group Rings* (Wiley, 1977), for the centrality of the class sums in the infinite case and the algebra they generate.
